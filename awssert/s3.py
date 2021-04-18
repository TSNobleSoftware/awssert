from awssert.prefixes import positives, negatives


class BucketAssertions:

    attaches_to = "s3.Bucket"

    @positives("should", "does")
    @negatives("should_not", "does_not")
    def contain(self, bucket, context, object):
        key = object if isinstance(object, str) else object.key
        objects = bucket.objects.filter(Prefix=key)
        context["result"] = any([key == obj.key for obj in objects])

    @positives("should_be")
    @negatives("should_not_be")
    def empty(self, bucket, context):
        context["result"] = len(list(bucket.objects.all())) == 0

    @positives("should", "does")
    @negatives("should_not", "does_not")
    def exist(self, bucket, context):
        context["result"] = bucket.creation_date is not None
