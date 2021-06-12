from app.models import Company
from django.urls import path
from . import views as v

urlpatterns = [
    path("",v.index,name="mainapp"),
    path("<int:companyid>", v.company, name="company"),
    # path('new/',v.new, name="new_message")
]
