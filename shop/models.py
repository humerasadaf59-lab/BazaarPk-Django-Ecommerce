from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from decimal import Decimal

class Category(models.Model):
    name=models.CharField(max_length=80, unique=True)
    slug=models.SlugField(unique=True)
    icon=models.CharField(max_length=30, default='✦')
    def __str__(self): return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name='products')
    name=models.CharField(max_length=180)
    slug=models.SlugField(unique=True)
    short_description=models.CharField(max_length=240)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    old_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    stock=models.PositiveIntegerField(default=10)
    image_url=models.URLField(blank=True)
    badge=models.CharField(max_length=30,blank=True)
    featured=models.BooleanField(default=False)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name
    def get_absolute_url(self): return reverse('product_detail',args=[self.slug])
    @property
    def discount_percent(self):
        if self.old_price and self.old_price>self.price:
            return round((1-self.price/self.old_price)*100)
        return 0

class Order(models.Model):
    STATUS_CHOICES=[('pending','Pending'),('confirmed','Confirmed'),('packed','Packed'),('shipped','Shipped'),('delivered','Delivered'),('cancelled','Cancelled')]
    PAYMENT_CHOICES=[('cod','Cash on Delivery'),('easypaisa','Easypaisa'),('jazzcash','JazzCash')]
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='orders')
    full_name=models.CharField(max_length=120)
    phone=models.CharField(max_length=30)
    email=models.EmailField(blank=True)
    city=models.CharField(max_length=80)
    address=models.TextField()
    payment_method=models.CharField(max_length=20,choices=PAYMENT_CHOICES,default='cod')
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    subtotal=models.DecimalField(max_digits=12,decimal_places=2)
    shipping=models.DecimalField(max_digits=10,decimal_places=2,default=199)
    total=models.DecimalField(max_digits=12,decimal_places=2)
    notes=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'#{self.id} — {self.full_name}'

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    product_name=models.CharField(max_length=180)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField()
    def line_total(self): return self.price*self.quantity
