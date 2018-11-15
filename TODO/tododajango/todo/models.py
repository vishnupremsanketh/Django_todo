from django.db import models

class todoitem(models.Model):
    content=models.TextField()
    fn=models.TextField(null=True)


class todosample(models.Model):
    sample=models.TextField()

class products(models.Model):
    name = models.TextField(default="None")
    phoneNumber = models.IntegerField(null=True)
    address = models.TextField(null=True)
    pinCode = models.IntegerField(null=True)

# Create your models here.
