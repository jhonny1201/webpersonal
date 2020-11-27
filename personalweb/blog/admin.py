from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_filds = ('created_at', 'updated_at')
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

