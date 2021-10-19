from django.contrib import admin
from .models import ShopsGroup, Shops, ShopsComm, Tag
import datetime
from admin_numeric_filter.admin import RangeNumericFilter
from modeltranslation.admin import TranslationAdmin


class ShopInLine(admin.TabularInline):
    model = Shops


class CommInLine(admin.TabularInline):
    model = ShopsComm


class TagAdmin(admin.ModelAdmin):
    pass


# class ShopsGroupAdmin(admin.ModelAdmin):
#     list_display = ['name', 'short_description']
#     inlines = [ShopInLine, CommInLine]
#     search_fields = ['name']

# @admin.register(ShopsComm)
class ShopsGroupAdmin(TranslationAdmin):
    list_display = ['name', 'short_description']
    inlines = [ShopInLine, CommInLine]
    search_fields = ['name']


class CommAdmin(admin.ModelAdmin):
    list_display = ['author', 'grade', 'status']
    actions = ['mark_as_published', 'mark_as_review']

    def mark_as_published(self, request, queryset):
        queryset.update(status='p')

    def mark_as_review(self, request, queryset):
        queryset.update(status='r')
        queryset.update(grade=0)

    mark_as_published.short_description = 'Перевести в статус Опубликовано'
    mark_as_review.short_description = 'Перевести в статус Удалено администратором'


# @admin.register(Shops)
class ShopsAdmin(TranslationAdmin):
    list_display = ['title', 'code_thing', 'price', 'short_description', 'status']
    search_fields = ['title']
    list_filter = (
        ('price', RangeNumericFilter),
    )
    actions = ['mark_as_published', 'mark_as_draft', 'mark_as_review']

    def mark_as_published(self, request, queryset):
        queryset.update(status='p')

    def mark_as_draft(self, request, queryset):
        queryset.update(status='d')

    def mark_as_review(self, request, queryset):
        queryset.update(status='r')
        queryset.update(finish_at=datetime.datetime.now().date())

    mark_as_published.short_description = 'Выставить на продажу'
    mark_as_draft.short_description = 'Черновик'
    mark_as_review.short_description = 'Снято с продажи'


# class ShopsAdmin(admin.ModelAdmin):
#     list_display = ['title', 'code_thing', 'price', 'short_description', 'status']
#     search_fields = ['title']
#     list_filter = (
#         ('price', RangeNumericFilter),
#     )
#     actions = ['mark_as_published', 'mark_as_draft', 'mark_as_review']
#
#     def mark_as_published(self, request, queryset):
#         queryset.update(status='p')
#
#     def mark_as_draft(self, request, queryset):
#         queryset.update(status='d')
#
#     def mark_as_review(self, request, queryset):
#         queryset.update(status='r')
#         queryset.update(finish_at=datetime.datetime.now().date())
#
#     mark_as_published.short_description = 'Выставить на продажу'
#     mark_as_draft.short_description = 'Черновик'
#     mark_as_review.short_description = 'Снято с продажи'


admin.site.register(Tag, TagAdmin)
admin.site.register(ShopsGroup, ShopsGroupAdmin)
admin.site.register(Shops, ShopsAdmin)
admin.site.register(ShopsComm, CommAdmin)
