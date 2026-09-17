from django.contrib import admin

from .models import GalleryCategory, GalleryImage, ContactMessage


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):

    list_display = ('name','slug',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):

    list_display = ('title','category','is_active','created_at',)
    list_filter = ('category','is_active','created_at',)
    search_fields = ('title','description',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = ('name','email','phone','subject','is_read','created_at',)

    list_filter = ('is_read','created_at',)

    search_fields = ('name','email','phone','subject','message',)

    readonly_fields = ('created_at',)

    ordering = ('-created_at',)