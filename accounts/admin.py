from django.contrib import admin
from .models import UserProfile, ProfileLinks

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'professional_headline')

    def get_username(self, obj):
        return obj.user.username

    get_username.admin_order_field = 'id'
    get_username.short_description = 'Username'  #Renames column head


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ProfileLinks)