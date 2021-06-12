from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Message,Company

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['msg','cid']


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name']