from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Pet model definition
class Pet(models.Model):
    PET_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Rabbit', 'Rabbit'),
    ]
    name = models.CharField(max_length=100)
    species = models.CharField(choices=PET_CHOICES, max_length=10)
    description = models.TextField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='pet_images/', blank=True, null=True)
    available_for_adoption = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Wishlist model definition
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dog = models.ForeignKey(Pet, on_delete=models.CASCADE)  # ForeignKey to Pet

    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.dog.name}"  # Corrected to use 'dog' instead of 'pet'

class Donation(models.Model):
    PAYMENT_METHODS = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    DONATION_TYPES = [
        ('one_time', 'One-time Donation'),
        ('monthly', 'Monthly Donation'),
        ('yearly', 'Yearly Donation'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPES)
    message = models.TextField(blank=True, null=True)
    is_anonymous = models.BooleanField(default=False)
    date_donated = models.DateTimeField(default=timezone.now)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.CharField(max_length=20, default='pending')
    
    # Additional fields for payment processing
    card_number = models.CharField(max_length=16, blank=True, null=True)  # Last 4 digits only
    card_expiry = models.CharField(max_length=5, blank=True, null=True)  # MM/YY format
    card_cvv = models.CharField(max_length=4, blank=True, null=True)  # Encrypted
    
    def __str__(self):
        return f"{self.name} - ${self.amount} - {self.donation_type}"
    
    class Meta:
        ordering = ['-date_donated']
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'
