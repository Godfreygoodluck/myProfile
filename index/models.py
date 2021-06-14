from django.db import models

# Create your models here.


class Ecommerce(models.Model):
    photo= models.ImageField(blank=True, upload_to = "gallery/Ecommerce")
    links = models.URLField(max_length=500, blank=True)
    github = models.URLField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Portfolio(models.Model):
    photo = models.ImageField(blank=True, upload_to = "gallery/Portfolio")
    links = models.URLField(max_length=500, blank=True)
    github = models.URLField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    photo = models.ImageField(blank=True, upload_to = "gallery/Blog")
    links = models.URLField(max_length=500, blank=True)
    github = models.URLField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    name = models.CharField(max_length=100)
    phone = models.TextField()
    message = models.TextField()
    mail = models.EmailField(max_length=254)
    created_on = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    phone = models.TextField()
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)

class Profile(models.Model):
    image = models.ImageField(upload_to = "gallery/myPic", blank=True)
    aboutMe = models.TextField( blank=True )

class MySkill(models.Model):
    skill = models.CharField(max_length=50)
    percentage = models.CharField(max_length=3)
    progresBar = models.CharField(max_length=20, blank=True)

class What_i_do(models.Model):
    H_tag = models.CharField(max_length=100, blank=True)
    text = models.CharField(max_length=500)