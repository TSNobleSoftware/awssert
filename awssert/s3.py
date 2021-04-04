from awssert.keywords import keywords


class BucketAssertions:

    @keywords(["should", "shouldnt", "should_not", "does", "doesnt", "does_not"])
    def contain(self, bucket, object):
        return object in bucket.objects.filter(object)

    @keywords(["is", "isnt", "is_not"])
    def empty(self, bucket):
        return not bucket.objects.all()
