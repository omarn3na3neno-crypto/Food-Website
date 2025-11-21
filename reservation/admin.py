from django.contrib import admin
from .models import Booking,Message
# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'guests', 'date', 'time', 'created_at')
    list_filter = ('date',)



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name_user', 'email_user', 'subject_user', 'created_time')
    list_filter = ('created_time',)
    search_fields = ('name_user', 'email_user', 'subject_user', 'content_user')
