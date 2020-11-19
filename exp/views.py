from django.shortcuts import render
from django.http import HttpResponse
from .models import Acc, Detail, Debit, Credit

# Create your views here.

#crud

#sites
def index(request):
    acc_objects = Acc.objects.all()
    acc_details = Detail.objects.all()
    context = {
        'acc_objects' : acc_objects,
        'acc_details' : acc_details
    }
    return render(request, "index.html", context)

def journal(request):
    debit = Debit.objects.all()
    credit = Credit.objects.all()
    context = {
        'debit_obj' : debit,
        'credit_obj' : credit
    }
    return render(request, "journal.html", context)