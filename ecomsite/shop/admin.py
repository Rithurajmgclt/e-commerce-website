from django.contrib import admin
from.models import Products,Orders

# Register your models here.
class ProductManage(admin.ModelAdmin):
    list_display = ('title','category','description')
    search_fields = ('title',)

admin.site.register(Products,ProductManage)
admin.site.register(Orders)
admin.site.site_header='E-commerce website'
admin.site.site_title ='MY cart'
admin.site.index_title='manage the cart'

