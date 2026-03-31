from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    TYPE = (
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    )

    CATEGORY = (
        ('Grocery', 'Grocery'),
        ('Snacks', 'Snacks'),
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Recharge', 'Recharge'),
        ('Monthly', 'Monthly'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    type = models.CharField(max_length=10, choices=TYPE)
    category = models.CharField(max_length=20, choices=CATEGORY)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return str(self.user)
