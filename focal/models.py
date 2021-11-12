from django.db import models

# Create your models here.

class Vision(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(max_length=500, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Mission(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(max_length=500, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CustomerSatisfaction(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(max_length=500, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title