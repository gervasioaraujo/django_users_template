from django.contrib.admin import AdminSite
from django.contrib import admin
from django.contrib.auth.models import Group, User

class CustomAdminSite(AdminSite):
    login_template = None

admin_site = CustomAdminSite()
admin.site = admin_site

admin.site.register(Group)
admin.site.register(User)