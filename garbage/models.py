from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class GarbageCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    joining_date = models.DateField()

    def __str__(self):
        return self.name


class GarbageRequest(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Assigned', 'Assigned'),
        ('Collected', 'Collected'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        GarbageCategory,
        on_delete=models.CASCADE
    )

    worker = models.ForeignKey(
        Worker,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    address = models.TextField()

    quantity = models.FloatField()

    request_date = models.DateTimeField(
        auto_now_add=True
    )

    collection_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.category.name}"