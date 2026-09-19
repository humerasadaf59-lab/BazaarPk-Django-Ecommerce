from django.contrib import admin
from .models import Category, Product, Order, OrderItem
admin.site.site_header='BazaarPK Store Admin'
admin.site.site_title='BazaarPK Admin'
admin.site.index_title='Store operations'
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): list_display=('name','slug'); prepopulated_fields={'slug':('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): list_display=('name','category','price','stock','featured','active'); list_filter=('category','featured','active'); search_fields=('name','short_description'); prepopulated_fields={'slug':('name',)}
class OrderItemInline(admin.TabularInline): model=OrderItem; extra=0; readonly_fields=('product_name','price','quantity','product')
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): list_display=('id','full_name','city','total','payment_method','status','created_at'); list_filter=('status','payment_method','city'); search_fields=('full_name','phone','email'); inlines=[OrderItemInline]
