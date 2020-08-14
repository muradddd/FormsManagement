from django.db import models
from accounts.models import UserModel

User=UserModel()
# Create your models here.
class Forms(models.Model):
    title=models.CharField('Title',max_length=200)
    description=models.CharField('Description',max_length=500)
    
    created_by = models.ForeignKey(User, related_name='forms',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'
        ordering = ('-created_at',)

class Field(models.Model):
    ANSWER_TYPE = (
        ('text', 'Short answer'),
        ('textarea', 'Paragraph'),
        ('radio', 'Multiple choice'),
        ('checkbox', 'Checkboxes'),
        ('select', 'Dropdown'),
        ('date', 'Date'),
    )
    form=models.ForeignKey(Forms,on_delete=models.CASCADE, related_name='field')
    question=models.CharField('Question',max_length=1001)
    answer_type = models.CharField('Answer type',max_length=100, choices=ANSWER_TYPE)
    is_required=models.BooleanField(default=False)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Option(models.Model):
    field = models.ForeignKey(Field,on_delete=models.CASCADE)
    value = models.CharField('Question',max_length=100)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Response(models.Model):
    form = models.ForeignKey(Forms,on_delete=models.CASCADE, related_name='responses')

    answered_by = models.ForeignKey(User, related_name='responses',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class ResponseQA(models.Model):
    response = models.ForeignKey(Response,on_delete=models.CASCADE, related_name='answers')
    question=models.CharField('Question',max_length=1001)
    answer = models.TextField('Answer')

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)