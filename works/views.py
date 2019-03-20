from django.shortcuts import render

from .models import work

# Create your views here.
def home(request):
    works = work.objects
    return render(request,'works/home.html',{'works':works})
