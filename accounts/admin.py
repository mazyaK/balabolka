from django.contrib import admin
from django.conf import settings
from .models import User

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['avatar_tag',]

    fields = [
        'username', 'slug', 'avatar_tag', 'first_name', 'last_name', 'email',
    ]

    list_display = ('username', 'avatar_tag', 'first_name', 'last_name', 'email',)
    prepopulated_fields = {'slug': ('username',)}

    def avatar_tag(self, obj):
        return obj.avatar_tag()


admin.site.register(User, UserAdmin)

