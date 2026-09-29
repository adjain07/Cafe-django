from django.contrib import admin
from django.utils.html import format_html

from .models import Category, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = (
        'image_preview',
        'name',
        'category',
        'price',
        'is_available',
        'is_featured',
    )

    list_filter = (
        'category',
        'is_available',
        'is_featured',
    )

    search_fields = (
        'name',
        'description',
    )

    list_editable = (
        'price',
        'is_available',
        'is_featured',
    )

    @admin.display(description='Image')
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" '
                'style="'
                'width:100px;'
                'height:75px;'
                'object-fit:cover;'
                'object-position:center;'
                'border-radius:8px;'
                'display:block;'
                '" />',
                obj.image.url
            )

        return 'No image'