from django.db import models
from django.db import models
# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=100)
    guests = models.PositiveIntegerField()
    phone_number = models.PositiveIntegerField(default=00000000000000)
    email = models.CharField(max_length=100,blank=True,null=True)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    massage = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"

class Message(models.Model):
    name_user = models.CharField(max_length=100)
    email_user = models.EmailField(max_length=100)
    subject_user = models.CharField(max_length=200)
    content_user = models.TextField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name_user} - {self.email_user}"