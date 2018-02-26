from django.db import models

# Create your models here.

# Account type model
class AccountType(models.Model):
    name = models.CharField(max_length=100)


# Users model which is used for all school users
class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.TextField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    guardian_id = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.TextField()
    gender = models.CharField(max_length=20)
    dob = models.CharField(max_length=50)
    passport = models.FileField(blank=True, null=True)
    category = models.CharField(max_length=50)
    classes = models.CharField(max_length=50)
    religion = models.CharField(max_length=20)
    account_type = models.ForeignKey('AccountType', on_delete=models.CASCADE)
    school = models.ForeignKey('administrator.Schools', on_delete=models.CASCADE)
    active = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name