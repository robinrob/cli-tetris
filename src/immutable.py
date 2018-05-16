class Immutable(object):

    def __init__(self, attrs_dict=None):
        if attrs_dict is not None:
            object.__setattr__(self, 'thing', attrs_dict)
        else:
            object.__setattr__(self, 'thing', {})

    # Setting is prevented if attribute is already set
    def __setattr__(self, attr, val):
        if attr in object.__getattribute__(self, 'thing'):
            raise AttributeError(f"Attribute '{attr}' of {self.__class__.__name__} object is not writable'")
        object.__getattribute__(self, 'thing')[attr] = val

    # None is returned if attr is not set
    def __getattribute__(self, attr):
        if attr in object.__getattribute__(self, 'thing'):
            return object.__getattribute__(self, 'thing')[attr]

        else:
            try:
                return object.__getattribute__(self, attr)

            except AttributeError:
                return None

    def to_dict(self):
        return object.__getattribute__(self, 'thing')