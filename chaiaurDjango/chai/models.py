# models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ChaiVarieties(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(blank=True)
     
   # New field added

    def __str__(self):
        return self.name 


# One to Many Model
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarieties, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(blank=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.user.username} for {self.chai.name}"

# Many to Many model
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_varieties = models.ManyToManyField(ChaiVarieties, related_name='stores')

    def __str__(self):
        return self.name
    

# One to One Model
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarieties, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Certificate for {self.chai.name}"
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chai = models.ForeignKey(ChaiVarieties, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Order by {self.user.username} for {self.chai.name}"