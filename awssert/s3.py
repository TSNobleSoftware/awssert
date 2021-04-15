from awssert.prefixes import positives, negatives


class BucketAssertions:

    attaches_to = "s3.Bucket"

    @positives(["should", "does"])
    @negatives(["should_not", "does_not"])
    def contain(self, bucket, key):
        objects = bucket.objects.filter(Prefix=key)
        return any([key == object.key for object in objects])

    @positives(["should_be"])
    @negatives(["should_not_be"])
    def empty(self, bucket):
        return len(list(bucket.objects.all())) == 0

    @positives(["should", "does"])
    @negatives(["should_not", "does_not"])
    def exist(self, bucket):
        return bucket.creation_date is not None
