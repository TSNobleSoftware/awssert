from awssert.keywords import keywords, ALL_KEYWORDS
from awssert.core import KeywordRouter, BotoObjectProxyRegister, BotoObjectProxy


class BucketAssertions:

    @keywords(["should", "should_not", "does", "does_not"])
    def contain(self, bucket, key):
        objects = bucket.objects.filter(Prefix=key)
        return any([key == object.key for object in objects])

    @keywords(["should_be", "should_not_be"])
    def empty(self, bucket):
        return len(list(bucket.objects.all())) == 0


def register_s3_assertions(class_attributes, base_classes, **kwargs):
    proxy = BotoObjectProxy()
    base_classes.insert(0, BotoObjectProxyRegister)
    class_attributes['proxy'] = proxy
    for keyword in ALL_KEYWORDS:
        class_attributes[keyword] = KeywordRouter(keyword, BucketAssertions(), proxy)
