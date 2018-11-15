from django.db import models

class todoitem(models.Model):
    content=models.TextField()
    fn=models.TextField(null=True)


class todosample(models.Model):
    sample=models.TextField()

# Create your models here.
