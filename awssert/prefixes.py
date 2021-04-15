class AssertionPrefixes:

    _positives = {}
    _negatives = {}

    @classmethod
    def register_positives(cls, method, allowed_prefixes):
        class_of_method = method.__qualname__.split(".")[0]
        if class_of_method not in cls._positives:
            cls._register_class(class_of_method, cls._positives)
        for prefix in allowed_prefixes:
            cls._register_class_method(class_of_method, prefix, method, cls._positives)

    @classmethod
    def register_negatives(cls, method, allowed_prefixes):
        class_of_method = method.__qualname__.split(".")[0]
        if class_of_method not in cls._negatives:
            cls._register_class(class_of_method, cls._negatives)
        for prefix in allowed_prefixes:
            cls._register_class_method(class_of_method, prefix, method, cls._negatives)

    @classmethod
    def get_methods_allowing_prefix(cls, on_class, prefix):
        positives = cls._positives[on_class.__name__].get(prefix, {})
        negatives = cls._negatives[on_class.__name__].get(prefix, {})
        return {**positives, **negatives}

    @classmethod
    def get_prefixes(cls, on_class):
        return cls.get_positives(on_class) + cls.get_negatives(on_class)

    @classmethod
    def get_positives(cls, on_class):
        return list(cls._positives[on_class.__name__].keys())

    @classmethod
    def get_negatives(cls, on_class):
        return list(cls._negatives[on_class.__name__].keys())

    @classmethod
    def _register_class(cls, class_name, register):
        register[class_name] = {}

    @classmethod
    def _register_class_method(cls, class_name, keyword, method, register):
        if keyword not in register[class_name]:
            register[class_name][keyword] = {}
        register[class_name][keyword][method.__name__] = method


def positives(*allowed_prefixes):
    def registrar(method):
        AssertionPrefixes.register_positives(method, allowed_prefixes)
        return method

    return registrar


def negatives(*allowed_prefixes):
    def registrar(method):
        AssertionPrefixes.register_negatives(method, allowed_prefixes)
        return method

    return registrar
