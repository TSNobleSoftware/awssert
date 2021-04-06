import pytest
import moto
import boto3


@pytest.fixture
def mock_ddb():
    with moto.mock_dynamodb2():
        yield


def test_table_empty_assertion(mock_ddb):
    boto3.client("dynamodb").create_table(
        AttributeDefinitions=[{"AttributeName": "mock", "AttributeType": "S"}],
        TableName="mock",
        KeySchema=[{"AttributeName": "mock", "KeyType": "HASH"}],
    )
    table = boto3.resource("dynamodb").Table("mock")
    assert table.should_be.empty()
    table.put_item(Item={"mock": "foo"})
    assert table.should_not_be.empty()


def test_table_has_item_assertion(mock_ddb):
    boto3.client("dynamodb").create_table(
        AttributeDefinitions=[{"AttributeName": "mock", "AttributeType": "S"}],
        TableName="mock",
        KeySchema=[{"AttributeName": "mock", "KeyType": "HASH"}],
    )
    table = boto3.resource("dynamodb").Table("mock")
    assert table.should_not_have.item({"mock": "foo"})
    assert table.does_not_have.item({"mock": "foo"})
    assert table.does_not_have.item({"mock": "bar"})
    table.put_item(Item={"mock": "foo"})
    assert table.should_have.item({"mock": "foo"})
    assert table.has.item({"mock": "foo"})
    assert table.does_not_have.item({"mock": "bar"})


def test_table_has_key_assertion(mock_ddb):
    boto3.client("dynamodb").create_table(
        AttributeDefinitions=[{"AttributeName": "mock", "AttributeType": "S"}],
        TableName="mock",
        KeySchema=[{"AttributeName": "mock", "KeyType": "HASH"}],
    )
    table = boto3.resource("dynamodb").Table("mock")
    assert table.should_have.key("mock")
    assert table.has.key("mock")
    assert table.should_not_have.key("foo")
    assert table.does_not_have.key("foo")
