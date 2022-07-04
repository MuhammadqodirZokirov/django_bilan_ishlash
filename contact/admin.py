from django.contrib import admin

from .models import Contact, Category, RegisterTable, Add_Product


class ContactAdmin(admin.ModelAdmin):
    list_display = ['fullName', 'email', 'phone', 'feedback', 'date']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_name', 'description', 'added_date']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RegisterTable)
admin.site.register(Add_Product)
