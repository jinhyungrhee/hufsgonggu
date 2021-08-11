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

# Review 테이블 정의
class Review(models.Model):
    title = models.CharField(max_length=256, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(upload_to="review/", blank=True, null=True)
    category = models.CharField(max_length=20, verbose_name='카테고리')
    store = models.CharField(max_length=20, verbose_name='업체')
    delivery = models.IntegerField(verbose_name='배송기간')
    price = models.IntegerField(verbose_name='가격')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'review'
        verbose_name = '리뷰'
        verbose_name_plural = '리뷰'