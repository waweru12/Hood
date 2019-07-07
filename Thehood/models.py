from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True,upload_to = 'images/',default = 'images/beauty1.jpg')
   
    bio = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.user.username}'




class Neighbourhood(models.Model):
    HOODS = (
        ('South B','South B'),
        ('Makongeni','Makongeni'),
        ('Kileleshwa','Kileleshwa'),
    )
    neighbourhood = models.CharField(max_length=255,choices=HOODS)
    pic = models.ImageField(blank=True,upload_to = 'hoods/')

    def __str__(self):
        return f'{self.neighbourhood}'

    

class HoodDetails(models.Model):
    TYPE = (
        ('Contact','Contact'),
        ('Business','Business'),
    )
    detail = models.CharField(max_length = 255)
    detailtype = models.CharField(max_length = 255,choices=TYPE)
    contact = models.CharField(max_length = 13)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'{self.detail}'


class Post(models.Model):
    post = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=False,null=False)

    def __str__(self):
        return f'{self.user}'
