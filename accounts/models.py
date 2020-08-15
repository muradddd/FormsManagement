from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    image=models.ImageField('Image',upload_to='user/',null=True,blank=True)
    bio=models.TextField('Bio',null=True,blank=True)

    @property
    def avatar(self):
        if self.image:
            return self.image.url
        else:
            return 'https://image.flaticon.com/icons/png/512/64/64572.png'