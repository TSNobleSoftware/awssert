from datetime import datetime

import dateutil

from awssert.prefixes import prefixes, AssertionPrefixes
from awssert.core import AssertionPrefixRouter, BotoObjectProxyRegister, BotoObjectProxy


class UserAssertions:

    attaches_to = "iam.User"

    @prefixes(["has", "does_not_have"])
    def name(self, user, name):
        return name == user.name

    @prefixes(["was", "was_not"])
    def created_at(self, user, date):
        if not isinstance(date, datetime):
            date = dateutil.parser.parse(date)
        return date == user.create_date

    @prefixes(["belongs_to", "does_not_belong_to", "is_part_of", "is_not_part_of"])
    def group(self, user, group):
        return group in user.groups.all()


class PolicyAssertions:

    attaches_to = "iam.Policy"

    @prefixes(["has", "does_not_have"])
    def name(self, policy, name):
        return name == policy.policy_name

    @prefixes(["has", "does_not_have"])
    def id(self, policy, id):
        return id == policy.policy_id

    @prefixes(["has", "does_not_have"])
    def description(self, policy, description):
        return description == policy.description

    @prefixes(["was", "was_not"])
    def created_at(self, policy, date):
        if not isinstance(date, datetime):
            date = dateutil.parser.parse(date)
        return date == policy.create_date

    @prefixes(["was", "was_not"])
    def last_updated_at(self, policy, date):
        if not isinstance(date, datetime):
            date = dateutil.parser.parse(date)
        return date == policy.update_date

    @prefixes(["should_be", "should_not_be"])
    def attached_to(self, policy, *entities):
        attached = {
            "iam.Group": policy.attached_groups.all(),
            "iam.Role": policy.attached_roles.all(),
            "iam.User": policy.attached_users.all(),
        }
        return all([entity in attached[type(entity).__name__] for entity in entities])
