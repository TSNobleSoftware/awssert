from datetime import datetime

import dateutil

from awssert.prefixes import positives, negatives


class UserAssertions:

    attaches_to = "iam.User"

    @positives(["has"])
    @negatives(["does_not_have"])
    def name(self, user, name):
        return name == user.name

    @positives(["was"])
    @negatives(["was_not"])
    def created_at(self, user, date):
        if not isinstance(date, datetime):
            date = dateutil.parser.parse(date)
        return date == user.create_date

    @positives(["belongs_to", "is_part_of"])
    @negatives(["does_not_belong_to", "is_not_part_of"])
    def group(self, user, group):
        return group in user.groups.all()


class PolicyAssertions:

    attaches_to = "iam.Policy"

    @positives(["has"])
    @negatives(["does_not_have"])
    def name(self, policy, name):
        return name == policy.policy_name

    @positives(["has"])
    @negatives(["does_not_have"])
    def description(self, policy, description):
        return description == policy.description

    @positives(["was"])
    @negatives(["was_not"])
    def created_at(self, policy, date):
        if not isinstance(date, datetime):
            date = dateutil.parser.parse(date)
        return date == policy.create_date

    @positives(["was"])
    @negatives(["was_not"])
    def last_updated_at(self, policy, date):
        if not isinstance(date, datetime):
            date = dateutil.parser.parse(date)
        return date == policy.update_date

    @positives(["should_be"])
    @negatives(["should_not_be"])
    def attached_to(self, policy, *entities):
        attached = {
            "iam.Group": policy.attached_groups.all(),
            "iam.Role": policy.attached_roles.all(),
            "iam.User": policy.attached_users.all(),
        }
        return all([entity in attached[type(entity).__name__] for entity in entities])


class GroupAssertions:

    attaches_to = "iam.Group"

    @positives(["has"])
    @negatives(["does_not_have"])
    def name(self, group, name):
        return name == group.group_name

    @positives(["was"])
    @negatives(["was_not"])
    def created_at(self, group, date):
        if not isinstance(date, datetime):
            date = dateutil.parser.parse(date)
        return date == group.create_date

    @positives(["should"])
    @negatives(["should_not"])
    def contain(self, group, user):
        return user in group.users.all()

    @positives(["has"])
    @negatives(["does_not_have"])
    def policy(self, group, policy):
        return policy in group.attached_policies.all()
