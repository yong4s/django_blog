from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("tags", "date")
    list_display = ("title", "date", 'user')
    search_fields = ("title",)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
