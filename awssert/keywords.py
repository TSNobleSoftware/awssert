from awssert.exceptions import UnsupportedKeywordError

POSITIVE = ["should", "does", "is"]
NEGATIVE = ["shouldnt", "should_not", "doesnt", "does_not", "isnt", "is_not"]


class Keywords:

    _register = {}

    @staticmethod
    def register_method(method, allowed_keywords):
        method_class = method.__qualname__.split(".")[0]
        if method_class not in Keywords._register:
            Keywords._register_class(method_class)
        for keyword in allowed_keywords:
            Keywords._register_class_method(method_class, keyword, method)

    @staticmethod
    def get_methods_allowing(class_name, keyword):
        class_name = class_name if isinstance(class_name, str) else class_name.__name__
        return Keywords._register[class_name][keyword]

    @staticmethod
    def _register_class(class_name):
        Keywords._register[class_name] = {keyword: {} for keyword in POSITIVE+NEGATIVE}

    @staticmethod
    def _register_class_method(class_name, keyword, method):
        try:
            Keywords._register[class_name][keyword][method.__name__] = method
        except KeyError:
            raise UnsupportedKeywordError(f"Keyword '{keyword}' is not supported")


def keywords(allowed_keywords):
    def registrar(method):
        Keywords.register_method(method, allowed_keywords)
        return method
    return registrar
