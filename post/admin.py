from django.contrib import admin
from post.models import *
from django.utils.safestring import mark_safe

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug':('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug':('title',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'author', 'views', 'get_photo')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'author', 'category', 'content', 'tags', 'views', 'photo',)
    list_filter = ('author', 'category', 'created_at')
    readonly_fields = ('views','get_photo',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'