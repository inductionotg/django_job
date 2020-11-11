from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date=models.DateField()
    company = models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phoneNumber=models.IntegerField()

class ban(models.Model):
    date=models.DateField()
    company = models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phoneNumber=models.IntegerField()

class chennai(models.Model):
    date=models.DateField()
    company = models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phoneNumber=models.IntegerField()

class delhi(models.Model):
    date=models.DateField()
    company = models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phoneNumber=models.IntegerField()

