from awssert.prefixes import prefixes, AssertionPrefixes
from awssert.core import AssertionPrefixRouter, BotoObjectProxyRegister, BotoObjectProxy


class TableAssertions:

    attaches_to = "dynamodb.Table"

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
