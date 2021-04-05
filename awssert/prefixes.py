from awssert.exceptions import PrefixNotSupportedError


class AssertionPrefixes:

    _register = {}
    positive = ["should", "does", "should_be", "should_have", "has"]
    negative = [
        "should_not",
        "does_not",
        "does_not_have",
        "should_not_be",
        "should_not_have",
    ]
    all = positive + negative

    @classmethod
    def register_method(cls, method, allowed_prefixes):
        class_of_method = method.__qualname__.split(".")[0]
        if class_of_method not in cls._register:
            cls._register_class(class_of_method)
        for prefix in allowed_prefixes:
            cls._register_class_method(class_of_method, prefix, method)

    @classmethod
    def get_methods_allowing_prefix(cls, on_class, prefix):
        return cls._register[on_class.__name__][prefix]

    @classmethod
    def _register_class(cls, class_name):
        cls._register[class_name] = {prefix: {} for prefix in cls.all}

    @classmethod
    def _register_class_method(cls, class_name, keyword, method):
        try:
            cls._register[class_name][keyword][method.__name__] = method
        except KeyError:
            raise PrefixNotSupportedError(f"Keyword '{keyword}' is not supported")


def prefixes(allowed_prefixes):
    def registrar(method):
        AssertionPrefixes.register_method(method, allowed_prefixes)
        return method

    return registrar
