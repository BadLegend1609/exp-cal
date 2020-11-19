from django.db import models

# Create your models here.

class Acc(models.Model):
    name = models.CharField(max_length=100)
    amt = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Detail(models.Model):
    name = models.ForeignKey(Acc, on_delete=models.CASCADE)
    CHOICES = [
        ('P', 'Payable'),
        ('R', 'Recievable'),
        ('C', 'Clear')
    ]
    status = models.CharField(max_length=1, choices=CHOICES, default='C')
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    
    def __str__(self):
        return str(self.name) + " " + self.status
    
    
class Debit(models.Model):
    acc = models.ForeignKey(Acc, on_delete=models.CASCADE)
    debit_amt = models.IntegerField(default=0)

    def __str__(self):
        return str(self.acc)
    
class Credit(models.Model):
    acc = models.ForeignKey(Acc, on_delete=models.CASCADE)
    credit_amt = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.acc)