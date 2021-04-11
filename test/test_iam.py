import moto
import boto3
import freezegun


@moto.mock_iam
def test_iam_user_has_name_assertion():
    user = boto3.resource("iam").User("foo")
    assert user.has.name("foo")
    assert user.does_not_have.name("bar")


@freezegun.freeze_time("01/02/2021 10:00:00+00:00")
@moto.mock_iam
def test_iam_user_was_created_at_assertion():
    user = boto3.resource("iam").User("foo").create()
    assert user.was.created_at("01/02/2021 10:00:00+00:00")
    assert user.was_not.created_at("02/02/2021 10:00:00+00:00")
    assert user.was_not.created_at("01/02/2021 10:00:01+00:00")


@moto.mock_iam
def test_iam_user_belongs_to_group_assertion():
    user = boto3.resource("iam").User("foo").create()
    group = boto3.resource("iam").Group("bar").create()
    assert user.does_not_belong_to.group(group)
    assert user.is_not_part_of.group(group)
    group.add_user(UserName=user.name)
    assert user.belongs_to.group(group)
    assert user.is_part_of.group(group)
