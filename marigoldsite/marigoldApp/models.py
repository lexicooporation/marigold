from django.db import models
from cloudinary.models import CloudinaryField 
class Product(models.Model):  

    CATEGORY_CHOICES = [
        ('candles', 'Candles'),
        ('melts', 'Wax Melts'),
        ('gifts', 'Gift Sets'),
    ]

    name        = models.CharField(max_length=100)  
    image       = CloudinaryField('image', blank=True, null=True)
    description = models.TextField()               
    price       = models.DecimalField(decimal_places=2, max_digits=8)
    category    = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='candles')
    etsy_url    = models.URLField(blank=True)        
    is_active   = models.BooleanField(default=True)  
    is_featured = models.BooleanField(default=False) 
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return self.name
    
class Review(models.Model):
    author      = models.CharField(max_length=100)         
    location    = models.CharField(max_length=100, blank=True) 
    content     = models.TextField()                          
    rating      = models.PositiveSmallIntegerField(default=5) 
    is_approved = models.BooleanField(default=False)          
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author} — {self.rating}★"

class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ('shipping',  'Shipping & Delivery'),
        ('products',  'Products & Ingredients'),
        ('care',      'Candle Care Tips'),
        ('orders',    'Orders & Custom Work'),
    ]
    question    = models.CharField(max_length=300)
    answer      = models.TextField()
    category    = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    order       = models.PositiveSmallIntegerField(default=0)  
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['-category', 'order']

    def __str__(self):
        return self.question

class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('custom',    'Custom / Bespoke Order'),
        ('wholesale', 'Wholesale Enquiry'),
        ('order',     'Order Question'),
        ('general',   'General Hello'),
        ('other',     'Something else'),
    ]

    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.EmailField()
    subject    = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    message    = models.TextField()
    sent_at    = models.DateTimeField(auto_now_add=True)
    is_read    = models.BooleanField(default=False) 

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.get_subject_display()}"