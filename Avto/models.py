from django.db import models

class Phone(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    description = models.TextField(default="", blank=True)
    image = models.ImageField(upload_to='images',blank=True,null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand

