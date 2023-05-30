from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Loans(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    loan_name = models.CharField(max_length=100)
    loan_amount = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.loan_name