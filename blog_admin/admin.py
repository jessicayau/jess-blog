from django.contrib import admin

# Register your models here.
class BlogAdmin(admin.AdminSite):
    site_header = "Jess's Blog"
    site_title = "Blog Admin"
    index_title = "Blog administration"

