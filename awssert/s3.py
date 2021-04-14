from awssert.prefixes import prefixes


class BucketAssertions:

    attaches_to = "s3.Bucket"

    @prefixes(["should", "should_not", "does", "does_not"])
    def contain(self, bucket, key):
        objects = bucket.objects.filter(Prefix=key)
        return any([key == object.key for object in objects])

    @prefixes(["should_be", "should_not_be"])
    def empty(self, bucket):
        return len(list(bucket.objects.all())) == 0

    @prefixes(["should", "should_not", "does", "does_not"])
    def exist(self, bucket):
        return bucket.creation_date is not None
