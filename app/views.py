from app.forms import MessageForm
from django.shortcuts import render,redirect
from .models import Company,Message
from app.forms import MessageForm,CompanyForm

# Create your views here.
def index(request):
    return render(request,"app/index.html",{
        "companies": Company.objects.all()
    })

def extract(s):
    ans = 0
    for i in s:
        if(i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9'):
            ans = ans*10 + (ord(i)-ord('0'))
        else:
            break

    return ans

def company(request,companyid):
    temp_messages = Message.objects.all()
    messages = []
    for message in temp_messages:
        if companyid == extract(str(message.cid)):
            messages.append(message)
    
    print("messages are:")
    print(messages)
    company = Company.objects.get(pk=companyid)
    return render(request,"app/company.html",{
        "messages":messages,
        "company": company,
        "empty" : len(messages)
    })

def new(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            new_msg = form.save(commit=False)
            new_msg.save()
            return redirect('/')
    else:
        form = MessageForm()
    return render(request, 'app/new.html',{'form':form})

def edit(request):
    pass

def newc(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            new_company = form.save(commit=False)
            new_company.save()
            return redirect('/')
    else:
        form = CompanyForm()
    return render(request, 'app/newc.html',{'form':form})