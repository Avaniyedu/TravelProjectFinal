from django.shortcuts import render
from .models import Destination
# Create your views here.



def index(request):

    # fetch datas
    
    dests = Destination.objects.all()

    return render(request,'index.html',{'dests' : dests})

