from django.contrib import admin
from .models import Editor,Article,tags

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filer_horizontal=('tags',)


admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)
