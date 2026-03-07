from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booknow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    place = models.CharField(max_length=100)
    member_count = models.IntegerField()
    event_date = models.DateField()
    payment_status = models.CharField(max_length=20, default="Pending")
    paypal_order_id = models.CharField(max_length=200, null=True, blank=True)
    paypal_capture_id = models.CharField(max_length=200, null= True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.place
     
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    my_email = models.EmailField(max_length=100)
    message = models.TextField(max_length=100)



    def __str__(self):
        return self.username
    

class roomBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    your_name = models.CharField(max_length=100)
    your_email = models.EmailField(max_length=100)
    checkin = models.DateField()
    checkout = models.DateField()
    guests = models.IntegerField()
    payment_status = models.CharField(max_length=20, default="Pending")
    paypal_order_id = models.CharField(max_length=200, null=True, blank=True)
    paypal_capture_id = models.CharField(max_length=200, null= True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.your_name



    

     




