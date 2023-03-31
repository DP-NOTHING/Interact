from django.contrib import admin
from .models import Profile
# class ProfileAdmin(admin.ModelAdmin):
#     list_filter = ('creator', 'normal_user')

# class PackagePriceAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug":("package_name",)}

admin.site.register(Profile)
