from modeltranslation.translator import register, TranslationOptions
from .models import Shops, ShopsComm, ShopsGroup, Tag


@register(Shops)
class ShopsTranslationOption(TranslationOptions):
    fields = ('title', 'description')


@register(ShopsGroup)
class ShopsGroupTranslationOption(TranslationOptions):
    fields = ('name', 'description')


@register(ShopsComm)
class ShopsGroupTranslationOption(TranslationOptions):
    fields = ('comm', )


@register(Tag)
class ShopsGroupTranslationOption(TranslationOptions):
    fields = ('title', )
