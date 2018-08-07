from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'Workshop HTML'

admin_site = MyAdminSite(name='myadmin')