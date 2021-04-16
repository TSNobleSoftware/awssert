from awssert.prefixes import positives, negatives


class TableAssertions:

    attaches_to = "dynamodb.Table"

    @positives("should_be")
    @negatives("should_not_be")
    def empty(self, table):
        assert table.item_count == 0

    @positives("should_have", "has")
    @negatives("should_not_have", "does_not_have")
    def item(self, table, key):
        assert "Item" in table.get_item(Key=key)

    @positives("should_have", "has")
    @negatives("should_not_have", "does_not_have")
    def key(self, table, key):
        keys = [key["AttributeName"] for key in table.key_schema]
        assert key in keys
