from django.contrib import admin
from .models import category
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ['category_name','slug']    # giev suggestion for slug
    list_display_links = ['category_name','slug']  # to make it clickable
admin.site.register(category,categoryAdmin)
