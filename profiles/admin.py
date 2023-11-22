from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile


# Register your models here.
class ProfileInline(admin.StackedInline):

    model = UserProfile
    readonly_fields = ('physical_health', 'emotional_health',
    'social_health', 'professional_health')


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ("username", "first_name", "last_name", "email")
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
