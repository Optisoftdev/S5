from django.db import models

# Create your models here.

# scchool model
class Schools(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    logo = models.FileField(blank=True, null=True)
    state = models.CharField(max_length=50)
    lga = models.CharField(max_length=50)
    school_type = models.CharField(max_length=20)
    active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)



    # SchoolAdmin model
# class SchoolAdmin(models.Model):
#     # school = models.ForeignKey(Schools, on_delete=models.CASCADE)
#     school = models.IntegerField(blank=True, null=True)
#     name = models.CharField(max_length=255)
#     address = models.TextField()
#     email = models.EmailField()
#     phone = models.IntegerField()
#     active = models.BooleanField(default=0, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)