from django.contrib import admin
from .models import CustomUser, Course, Event, GalleryItem, ContactMessage,AboutUs
from django.contrib.auth.admin import UserAdmin

admin.site.register(AboutUs)
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Course)
admin.site.register(Event)
admin.site.register(GalleryItem)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'email', 'subject', 'sent_at')
    
    # Fields that can be searched
    search_fields = ('name', 'email', 'subject', 'message')
    
    # Filters in the sidebar
    list_filter = ('sent_at',)
    
    # Make all fields read-only in the form view
    readonly_fields = ('name', 'email', 'subject', 'message', 'sent_at')
    
    # Optional: Order by latest first
    ordering = ('-sent_at',)