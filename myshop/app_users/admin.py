from django.contrib import admin

from .models import Profile


class PrifileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, PrifileAdmin)
