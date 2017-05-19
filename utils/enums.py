# EnumeratedEnumMeta, LabeledEnum and StructuredEnum classes were taken from:
# https://gist.github.com/jsatt/54db7dadc068a4a52910

from enum import Enum, EnumMeta


class EnumeratedEnumMeta(EnumMeta):
    def __new__(metacls, *args):
        enum_class = super().__new__(metacls, *args)
        enum_class._value2member_map_ = {m.value: m for v, m in enum_class._value2member_map_.items()}
        return enum_class


class LabeledEnum(Enum, metaclass=EnumeratedEnumMeta):
    def __init__(self, value, label):
        self._value_ = value
        self.label = label


class StructuredEnum(Enum, metaclass=EnumeratedEnumMeta):
    def __init__(self, value, kwargs):
        self._value_ = value
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def choices(cls):
        return [(choice.value, choice.label) for choice in cls]

    @classmethod
    def key(cls, value):
        return next((kind.name.lower() for kind in cls if kind.value == value), None)

    @classmethod
    def keys(cls):
        return [state.value for state in cls]

    @classmethod
    def labels(cls):
        return [event.label for event in cls]

    @classmethod
    def display_label(cls, value):
        return next((item.label for item in cls if item.value == int(value)), '')

    @classmethod
    def display_name(cls, value):
        return next((item.first_name for item in cls if item.value == int(value)), '')

    @classmethod
    def reverse(cls, label):
        return next((item for item in cls if item.label == label), None)

    @classmethod
    def find(cls, name):
        return next((item for item in cls if item.name == name), None)


class AutoNumberStructuredEnum(Enum, metaclass=EnumeratedEnumMeta):
    def __new__(cls, *args):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, value, kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


##################################################################################
#                               CUSTOM ENUMERATORS                               #
##################################################################################

class BLOG_POST_STATE(StructuredEnum):
    DRAFT = 1, {'label': 'Draft'}
    PUBLISHED = 2, {'label': 'Published'}


class FAMILY_MEMBER(StructuredEnum):
    SAMARDZICI = 0, {'label': 'Samardzici', 'first_name': 'Samardzici'}
    SVETLANA = 19760525, {'label': 'Ceca', 'first_name': 'Svetlana'}
    NENAD = 19760702, {'label': 'Nenad', 'first_name': 'Nenad'}
    NOVAK = 20110913, {'label': 'Nole', 'first_name': 'Novak'}
    LUNA = 20150102, {'label': 'Luna', 'first_name': 'Luna'}
