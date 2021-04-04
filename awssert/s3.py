from awssert.keywords import keywords
from awssert.core import KeywordRouter, BotoObjectProxyRegister, BotoObjectProxy


class BucketAssertions:

    @keywords(["should", "does"])
    def contain(self, bucket, key):
        objects = bucket.objects.filter(Prefix=key)
        assert any([key == object.key for object in objects])


def register_s3_assertions(class_attributes, base_classes, **kwargs):
    proxy = BotoObjectProxy()
    base_classes.insert(0, BotoObjectProxyRegister)
    class_attributes['proxy'] = proxy
    class_attributes['should'] = KeywordRouter("should", BucketAssertions(), proxy)
