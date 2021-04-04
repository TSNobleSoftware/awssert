import functools

from awssert.keywords import Keywords, POSITIVE
from awssert.exceptions import MethodDoesNotSupportKeywordError


class BotoObjectProxyRegister(object):
    def __init__(self, *args, **kwargs):
        super(BotoObjectProxyRegister, self).__init__(*args, **kwargs)
        self.proxy.reference = self


class BotoObjectProxy:
    def __init__(self):
        self.reference = None


class KeywordRouter:

    def __init__(self, keyword, assertions_class, proxy):
        self.keyword = keyword
        self.route_to = assertions_class
        self.proxy = proxy
        self.routable_methods = self._setup_routable_methods()

    def _setup_routable_methods(self):
        routable_methods = Keywords.get_methods_allowing(
            self.route_to.__class__, self.keyword
        )
        all_methods = [
            method for method in dir(self.route_to)
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
            return result if self.keyword in POSITIVE else not result
        else:
            raise MethodDoesNotSupportKeywordError(
                f"Method '{method}' cannot be used with keyword '{self.keyword}'"
            )
