from django.contrib import admin

from .models import AuthLibrary, Category, Reaction, Comment,CodeSnippet


# Register your models here.

admin.site.register(CodeSnippet)
admin.site.register(AuthLibrary)
admin.site.register(Reaction)
admin.site.register(Comment)
admin.site.register(Category)

