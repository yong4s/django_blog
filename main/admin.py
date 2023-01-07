from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", "date")
    list_display = ("title", "author", "date")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)