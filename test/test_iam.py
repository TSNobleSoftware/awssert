import json

import pytest
import moto
import boto3
import freezegun


@pytest.fixture
def generate_policy():
    def generate(name, description=None):
        description = description or "Nothing"
        document = {
            "Version": "2012-10-17",
            "Statement": [{"Effect": "Allow", "Action": "*", "Resource": "*"}],
        }
        response = boto3.client("iam").create_policy(
            PolicyName=name,
            PolicyDocument=json.dumps(document),
            Description=description,
        )
        return response["Policy"]["Arn"]

    return generate


@pytest.fixture
def generate_role():
    def generate(name):
        document = {
            "Version": "2012-10-17",
            "Statement": [{"Effect": "Allow", "Action": "*", "Resource": "*"}],
        }
        boto3.client("iam").create_role(
            RoleName=name, AssumeRolePolicyDocument=json.dumps(document)
        )

    return generate


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


@moto.mock_iam
def test_iam_policy_has_name_assertion(generate_policy):
    policy_arn = generate_policy("foo")
    policy = boto3.resource("iam").Policy(policy_arn)
    assert policy.has.name("foo")
    assert policy.does_not_have.name("bar")


@moto.mock_iam
def test_iam_policy_has_description_assertion(generate_policy):
    policy_arn = generate_policy("foo", description="description")
    policy = boto3.resource("iam").Policy(policy_arn)
    assert policy.has.description("description")
    assert policy.does_not_have.description("not the description")


@freezegun.freeze_time("01/02/2021 10:00:00+00:00")
@moto.mock_iam
def test_iam_policy_was_created_at_assertion(generate_policy):
    policy_arn = generate_policy("foo")
    policy = boto3.resource("iam").Policy(policy_arn)
    assert policy.was.created_at("01/02/2021 10:00:00+00:00")
    assert policy.was_not.created_at("02/02/2021 10:00:00+00:00")
    assert policy.was_not.created_at("01/02/2021 10:00:01+00:00")


@freezegun.freeze_time("01/02/2021 10:00:00+00:00")
@moto.mock_iam
def test_iam_policy_was_last_updated_at_assertion(generate_policy):
    policy_arn = generate_policy("foo")
    policy = boto3.resource("iam").Policy(policy_arn)
    assert policy.was.last_updated_at("01/02/2021 10:00:00+00:00")
    assert policy.was_not.last_updated_at("02/02/2021 10:00:00+00:00")


@moto.mock_iam
def test_iam_policy_should_be_attached_to_assertion_with_user(generate_policy):
    policy_arn = generate_policy("foo")
    policy = boto3.resource("iam").Policy(policy_arn)
    good_user = boto3.resource("iam").User("good").create()
    policy.attach_user(UserName=good_user.name)
    assert policy.should_be.attached_to(good_user)
    bad_user = boto3.resource("iam").User("bad").create()
    assert policy.should_not_be.attached_to(bad_user)


@moto.mock_iam
def test_iam_policy_should_be_attached_to_assertion_with_role(
    generate_policy, generate_role
):
    policy_arn = generate_policy("foo")
    policy = boto3.resource("iam").Policy(policy_arn)
    generate_role("good")
    good_role = boto3.resource("iam").Role("good")
    policy.attach_role(RoleName=good_role.name)
    assert policy.should_be.attached_to(good_role)
    generate_role("bad")
    bad_role = boto3.resource("iam").Role("bad")
    assert policy.should_not_be.attached_to(bad_role)


@moto.mock_iam
def test_iam_policy_should_be_attached_to_assertion_with_group(generate_policy):
    policy_arn = generate_policy("foo")
    policy = boto3.resource("iam").Policy(policy_arn)
    good_group = boto3.resource("iam").Group("good").create()
    policy.attach_group(GroupName=good_group.name)
    assert policy.should_be.attached_to(good_group)
    bad_group = boto3.resource("iam").Group("bad").create()
    assert policy.should_not_be.attached_to(bad_group)


@moto.mock_iam
def test_iam_policy_should_be_attached_to_assertion_with_multiple(
    generate_policy, generate_role
):
    policy_arn = generate_policy("foo")
    policy = boto3.resource("iam").Policy(policy_arn)
    good_user = boto3.resource("iam").User("good").create()
    good_group = boto3.resource("iam").Group("good").create()
    generate_role("good")
    good_role = boto3.resource("iam").Role("good")
    policy.attach_user(UserName=good_user.name)
    policy.attach_role(RoleName=good_role.name)
    policy.attach_group(GroupName=good_group.name)
    assert policy.should_be.attached_to(good_group, good_user, good_role)
    bad_user = boto3.resource("iam").User("bad").create()
    assert policy.should_not_be.attached_to(good_group, bad_user, good_role)


@moto.mock_iam
def test_iam_group_has_name_assertion():
    group = boto3.resource("iam").Group("foo")
    assert group.has.name("foo")
    assert group.does_not_have.name("bar")


@freezegun.freeze_time("01/02/2021 10:00:00+00:00")
@moto.mock_iam
def test_iam_group_was_created_at_assertion():
    group = boto3.resource("iam").Group("foo").create()
    assert group.was.created_at("01/02/2021 10:00:00+00:00")
    assert group.was_not.created_at("02/02/2021 10:00:00+00:00")
    assert group.was_not.created_at("01/02/2021 10:00:01+00:00")


@moto.mock_iam
def test_iam_group_should_contain_assertion():
    group = boto3.resource("iam").Group("foo").create()
    user = boto3.resource("iam").User("bar").create()
    assert group.should_not.contain(user)
    group.add_user(UserName=user.name)
    assert group.should.contain(user)


@moto.mock_iam
def test_iam_group_has_policy_assertion(generate_policy):
    group = boto3.resource("iam").Group("foo").create()
    policy_arn = generate_policy("bar")
    policy = boto3.resource("iam").Policy(policy_arn)
    assert group.does_not_have.policy(policy)
    policy.attach_group(GroupName=group.name)
    assert group.has.policy(policy)

