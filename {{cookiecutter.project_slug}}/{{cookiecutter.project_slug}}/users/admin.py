# Django
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ["email", "first_name", "last_name", "username", "is_superuser"]
    list_display_links = ["email", "first_name"]
    # list_filter = []
    # search_fields = []

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": (("first_name", "last_name"), "email")}),
        (
            _("Permissions"),
            {
                "classes": ("collapse",),
                "fields": (("is_active",), ("is_staff",), ("is_superuser",), ("groups"), ("user_permissions")),
            },
        ),
        (_("Important dates"), {"classes": ("collapse",), "fields": ("last_login", "date_joined")}),
        (_("Creación y actualización"), {"classes": ("collapse",), "fields": ("created", "modified")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )

    readonly_fields = ("last_login", "date_joined", "created", "modified")
