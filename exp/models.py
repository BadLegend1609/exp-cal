from django.db import models

# Create your models here.

class Acc(models.Model):
    name = models.CharField(max_length=100)
    amt = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Details(models.Model):
    name = models.ForeignKey(Acc, on_delete=models.CASCADE)
    CHOICES = [
        ('P', 'Payable'),
        ('R', 'Recievable'),
        ('C', 'Clear')
    ]
    status = models.CharField(max_length=1, choices=CHOICES, default='C')
    date = models.DateTimeField()
    location = models.CharField(max_length=300)