from django.db import models

class Phone(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand