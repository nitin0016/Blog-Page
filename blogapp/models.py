from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=255)
    image=CloudinaryField('image')

    def __str__(self):
        return self.username

class Userdata(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=230)
    contact=models.PositiveIntegerField()
    address=models.TextField(max_length=255)
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return  self.name

class Blog(models.Model):
    title=models.CharField(max_length=255)
    image=CloudinaryField('image')
    description=RichTextField(blank=True,null=True)
    created_by=models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.title

class ContactUs(models.Model):
    name=models.CharField(max_length=255)
    contact=models.PositiveIntegerField()
    address=models.TextField(max_length=255)

    def __str__(self):
        return  self.name
