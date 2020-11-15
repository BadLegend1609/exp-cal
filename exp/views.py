from django.shortcuts import render
from django.http import HttpResponse
from .models import Acc, Details

# Create your views here.

#crud

#sites
def index(request):
    acc_objects = Acc.objects.all()
    acc_details = Details.objects.all()
    context = {
        'acc_objects' : acc_objects,
        'acc_details' : acc_details
    }
    return render(request, "index.html", context)

def journal(request):
    return render(request, "journal.html")