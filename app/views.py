from django.shortcuts import render
# Create your views here.
def data_render(request):
    data='this iss our assumption'
    d={'assumption':data}
    return render(request,'data_render.html',context=d)

def login(request):
    d={'username':'divya','age':23}
    return render(request,'login.html',context=d)