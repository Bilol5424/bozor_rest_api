from django.contrib import admin
from bozor_beta.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    model = User
    list_display = ("id", "first_name", "last_name", "full_name", "username", "email", "phone", "created_at")
    list_filter = ("id", "first_name", "last_name", "username", "email", "phone", "created_at")
    search_fields = ("first_name", "last_name", "username", "email", "phone")
    list_display_links = ("id", "username")
    list_per_page = 12
    date_hierarchy = "created_at"
    
    def full_name(self, instance):
        return instance.first_name + instance.last_name
    full_name.short_description = "ФИО"
