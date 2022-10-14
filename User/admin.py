from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from User.models import User
# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Información Personal"), {"fields": ("first_name", "last_name",'movil', "email","image")}),
        (
            ("Permisos"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Datos Imporantes"), {"fields": ("last_login", "date_joined")}),
    )
admin.site.register(User,CustomUserAdmin)
