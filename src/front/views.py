from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request,'front/list.html',{})

# def list(request,name):
#     return render(request,'front/list.html',{})