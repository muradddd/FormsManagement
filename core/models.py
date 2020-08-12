from django.db import models
from accounts.models import UserModel

User=UserModel()
# Create your models here.
class Forms(models.Model):
    title=models.CharField('Title',max_length=200)
    description=models.TextField('Description')
    
    slug = models.SlugField(max_length=255, null=True, blank=True)

    created_by = models.ForeignKey(User, related_name='Form_created_by',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Field(models.Model):
    form=models.ForeignKey(Forms,on_delete=models.CASCADE)
    question=models.CharField('Question',max_length=1001)
    answer=models.CharField('Answer',max_length=1001)
    content= models.FileField(upload_to="files/")

    slug = models.SlugField(max_length=255, null=True, blank=True)
    is_required=models.BooleanField(default=False)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)