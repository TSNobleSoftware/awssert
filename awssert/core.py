from contextlib import _GeneratorContextManager, contextmanager
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
        self.context = {}
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

    @contextmanager
    def _context_manager_wrapper(self, manager, method, *args, **kwargs):
        with manager:
            yield
        result = self.context["result"]
        self._process_prefix(result, method, args, kwargs)

    def _route(self, method, *args, **kwargs):
        if method not in self.routable_methods:
            raise DisallowedPrefixOnMethodError(
                f"Method '{method}' cannot be used with prefix '{self.prefix}'"
            )
        result = getattr(self.route_to, method)(
            self.proxy.reference, self.context, *args, **kwargs
        )
        if isinstance(result, _GeneratorContextManager):
            return self._context_manager_wrapper(result, method, *args, **kwargs)
        self._process_prefix(self.context["result"], method, *args, **kwargs)

    def _process_prefix(self, result, method, *args, **kwargs):
        result_matches_prefix = (self._is_prefix_positive() and result) or not (
            self._is_prefix_positive() or result
        )
        if not result_matches_prefix:
            f_args = [str(arg) for arg in args]
            f_kwargs = [f"{k}={str(v)}" for k, v in kwargs.items()]
            f_params = ", ".join(f_args + f_kwargs)
            f_assertion = f"{self.proxy.reference}.{self.prefix}.{method}({f_params})"
            raise AssertionError(f"Assertion {f_assertion} was False")

    def _is_prefix_positive(self):
        return self.prefix in AssertionPrefixes.get_positives(type(self.route_to))
