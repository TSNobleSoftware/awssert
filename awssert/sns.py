import json
from contextlib import contextmanager

import moto
import boto3

from awssert.prefixes import positives, negatives


class TopicAssertions:

    attaches_to = "sns.Topic"

    @positives("should")
    @negatives("should_not")
    @contextmanager
    def receive(self, topic, context, message):
        region = topic.meta.client.meta.region_name
        is_topic_mocked = topic.arn in moto.sns.sns_backends[region].topics
        mock_sqs = moto.mock_sqs() if is_topic_mocked else None
        if is_topic_mocked:
            mock_sqs.start()
        sqs = boto3.client("sqs")
        url = sqs.create_queue(QueueName="awssert-archive")["QueueUrl"]
        attributes = sqs.get_queue_attributes(QueueUrl=url, AttributeNames=["QueueArn"])
        queue_arn = attributes["Attributes"]["QueueArn"]
        subscription = topic.subscribe(Protocol="sqs", Endpoint=queue_arn)
        yield
        messages = sqs.receive_message(QueueUrl=url)["Messages"]
        context["result"] = message == json.loads(messages[0]["Body"])["Message"]
        subscription.delete()
        sqs.delete_queue(QueueUrl=url)
        if is_topic_mocked:
            mock_sqs.stop()
