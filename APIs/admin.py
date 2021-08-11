from django.contrib import admin
from APIs.models import Product, Review

# Register your models here.
@admin.register(Product) # 데코레이터 - register함수 대신 사용
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image', 'created_at')
#admin.site.register(Product, ProductAdmin)

# Review 테이블 등록
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'category', 'store', 'delivery', 'price', 'created_at')