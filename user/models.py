from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Teste(models.Model):
    test = models.CharField(max_length=15)
    number = models.IntegerField()

class User(AbstractUser):
    email = models.EmailField(unique=True,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class Profile(models.Model):
    GENDER_CHOICES = (
        ('Masculino','Masculino'),
        ('Feminino','Feminino'),
        ('Outros','Outros')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    gender = models.CharField(max_length=255,choices=GENDER_CHOICES, blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    profile_picture = models.ImageField(upload_to='profile_images',default='blank-profile-picture.svg')
    banner = models.ImageField(upload_to='profile_banners',blank=True,null=True)
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=255,blank=True,null=True)
    state = models.CharField(max_length=255, blank=True,null=True)
    city = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f"{self.user} Profile"

    @property
    def first_name(self):
        try:
            name_list = self.name.split()
            first_name = name_list[0]
        except:
            first_name = ''

        return first_name
    
    @property
    def surname(self):
        try:
            name_list = self.name.split()
            surname = name_list[1:]
        except:
            surname = ''

        return surname
