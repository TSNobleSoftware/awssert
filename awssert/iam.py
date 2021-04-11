from datetime import datetime

import dateutil

from awssert.prefixes import prefixes, AssertionPrefixes
from awssert.core import AssertionPrefixRouter, BotoObjectProxyRegister, BotoObjectProxy


class UserAssertions:
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


def register_iam_assertions(class_attributes, base_classes, **kwargs):
    proxy = BotoObjectProxy()
    base_classes.insert(0, BotoObjectProxyRegister)
    class_attributes["proxy"] = proxy
    for prefix in AssertionPrefixes.all:
        class_attributes[prefix] = AssertionPrefixRouter(
            prefix, UserAssertions(), proxy
        )