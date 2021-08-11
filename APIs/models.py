from django.db import models

# Create your models here.
# Product 테이블 정의
class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    image = models.ImageField(upload_to="product/", blank=True, null=True) # 옵션 확인 필요
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'