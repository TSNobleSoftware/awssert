import moto
import boto3


@moto.mock_sns
def test_topic_should_receive_message_assertion():
    arn = boto3.client("sns").create_topic(Name="foo")["TopicArn"]
    topic = boto3.resource("sns").Topic(arn)
    with topic.should.receive("foo"):
        topic.publish(Message="foo")
    with topic.should_not.receive("bar"):
        topic.publish(Message="foo")
