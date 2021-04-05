import functools

from awssert.prefixes import AssertionPrefixes
from awssert.exceptions import DisallowedPrefixOnMethodError


class BotoObjectProxyRegister(object):
    def __init__(self, *args, **kwargs):
        super(BotoObjectProxyRegister, self).__init__(*args, **kwargs)
        self.proxy.reference = self


class BotoObjectProxy:
    def __init__(self):
        self.reference = None


class AssertionPrefixRouter:
    def __init__(self, prefix, assertions_class, proxy):
        self.prefix = prefix
        self.route_to = assertions_class
        self.proxy = proxy
        self.routable_methods = self._setup_routable_methods()

    def _setup_routable_methods(self):
        routable_methods = AssertionPrefixes.get_methods_allowing_prefix(
            self.route_to.__class__, self.prefix
        )
        all_methods = [
            method
            for method in dir(self.route_to)
            if callable(getattr(self.route_to, method)) and not method.startswith("__")
        ]
        for method in all_methods:
            self.__setattr__(method, functools.partial(self._route, method))
        return routable_methods.keys()

    def _route(self, method, *args, **kwargs):
        if method in self.routable_methods:
            result = getattr(self.route_to, method)(
                self.proxy.reference, *args, **kwargs
            )
            return result if self.prefix in AssertionPrefixes.positive else not result
        else:
            raise DisallowedPrefixOnMethodError(
                f"Method '{method}' cannot be used with prefix '{self.prefix}'"
            )
