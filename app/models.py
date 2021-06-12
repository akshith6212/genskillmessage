from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length = 30) #company name
    # photo = models.BinaryField()
    id = models.AutoField(primary_key=True) #id of the company

    def __str__(self):
        return f"{self.id}.{self.name}"

class Message(models.Model):
    # msg = models.TextField() #content of message
    msg = RichTextUploadingField(blank=True, null=True)
    cid = models.ForeignKey(Company,on_delete=models.CASCADE) #company id
    id = models.AutoField(primary_key=True) #message id for sorting
    d = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}:{self.msg[:6]}"

