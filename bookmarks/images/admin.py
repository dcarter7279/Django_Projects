from django.contrib import admin
from .models import Image
@admin.register(Image)

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']