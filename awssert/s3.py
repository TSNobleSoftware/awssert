from awssert.prefixes import prefixes, AssertionPrefixes
from awssert.core import AssertionPrefixRouter, BotoObjectProxyRegister, BotoObjectProxy


class BucketAssertions:
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


def register_s3_assertions(class_attributes, base_classes, **kwargs):
    proxy = BotoObjectProxy()
    base_classes.insert(0, BotoObjectProxyRegister)
    class_attributes["proxy"] = proxy
    for prefix in AssertionPrefixes.all:
        class_attributes[prefix] = AssertionPrefixRouter(
            prefix, BucketAssertions(), proxy
        )
