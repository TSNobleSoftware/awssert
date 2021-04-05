from awssert.prefixes import prefixes, AssertionPrefixes
from awssert.core import AssertionPrefixRouter, BotoObjectProxyRegister, BotoObjectProxy


class TableAssertions:
    @prefixes(["should_be", "should_not_be"])
    def empty(self, table):
        return table.item_count == 0

    @prefixes(["should_have", "has", "should_not_have", "does_not_have"])
    def item(self, table, key):
        return "Item" in table.get_item(Key=key)

    @prefixes(["should_have", "has", "should_not_have", "does_not_have"])
    def key(self, table, key):
        keys = [key["AttributeName"] for key in table.key_schema]
        return key in keys


def register_dynamodb_assertions(class_attributes, base_classes, **kwargs):
    proxy = BotoObjectProxy()
    base_classes.insert(0, BotoObjectProxyRegister)
    class_attributes["proxy"] = proxy
    for prefix in AssertionPrefixes.all:
        class_attributes[prefix] = AssertionPrefixRouter(
            prefix, TableAssertions(), proxy
        )
