from enum import Enum


class Choices(Enum):
    @classmethod
    def choices(cls):
        return tuple((item.name, item.value) for item in cls)

    @classmethod
    def country_choices(cls, country):
        return next(item.value for item in cls if item.name == country)


class OriginCodes(Choices):
    C = 'Commercial (C)'
    L = 'Library music (L)'
    P = 'Live performance (P)'
    V = 'Music video (V)'
    X = 'Specially commissioned score (X)'


class UsageCodes(Choices):
    GB = (
        ('B', 'Background'),
        ('F', 'Foreground')
    )

    US = (
        ('BI', 'Background instrumental'),
        ('BV', 'Background vocal'),
        ('ET', 'End title theme'),
        ('L', 'Logo'),
        ('MT', 'Main title theme'),
        ('VI', 'Visual instrumentation'),
        ('VV', 'Visual vocal')
    )


class Roles(Choices):
    A = 'Arranger of musical composition'
    C = 'Composer/Writer'
    P = 'Publisher. Individual or corporation'
