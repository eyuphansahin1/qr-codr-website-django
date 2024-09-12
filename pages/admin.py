from django.contrib import admin

from .models import Category,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "isActive",)  # 'slug' eklendi
    list_display_links = ("name", "slug",) 
    prepopulated_fields = {"slug" : ("name",),}
    list_filter = ("isActive",)
    list_editable = ("isActive",)
    


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "isActive",)  
    list_display_links = ("name",) 
    list_filter = ("isActive","category",)
    list_editable = ("isActive",)
    search_fields = ("name",)