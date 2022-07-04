from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField(default='example@gmail.com')
    phone = models.CharField(max_length=20)
    feedback = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullName

    class Meta:
        verbose_name_plural = 'Aloqa'


class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_img = models.FileField(upload_to='categories/%Y/%m/%d')
    description = models.TextField(blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name_plural = 'Katalog'


class RegisterTable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default='998991112233')
    age = models.CharField(max_length=100, blank=True)
    profile_img = models.ImageField(upload_to='profiles/%Y/%m/%d', blank=True)
    city = models.CharField(max_length=100, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=50, default='Male')
    about = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Foydalanuchilar'


class Add_Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    sale_price = models.FloatField()
    product_img = models.ImageField(upload_to='products/%Y/%m/%d')
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Mahsulot_qo\'shish'