from django.db import models

# Create your models here.
class UserForm(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_no = models.IntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    hobbies = models.CharField(max_length=100)
    country = models.CharField(max_length=20, choices=[('india', 'India'),('usa', 'United States'),('canada', 'Canada'),('uk', 'United Kingdom')])
    bio = models.TextField()

    def __str__(self):
        return self.name
