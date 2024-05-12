from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/vege/login/")
def receipes(request):
    if request.method == "POST":
        receipe_name=request.POST.get("receipe_name")
        receipe_desc=request.POST.get("receipe_desc")
        receipe_image=request.FILES.get("receipe_image")

        Receipe.objects.create(receipe_name = receipe_name , receipe_desc = receipe_desc , receipe_image = receipe_image)
    
        return redirect('/vege/receipes/')

    queryset = Receipe.objects.all() # yeh read krne ke liye hota h  
    
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
    
    context={"receipes":queryset}
    return render(request,"D:\\relation\\vege\\templates\\receipe.html", context)

def update_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        receipe_name=request.POST.get("receipe_name")
        receipe_desc=request.POST.get("receipe_desc")
        receipe_image=request.FILES.get("receipe_image")

        queryset.receipe_name = receipe_name,
        queryset.receipe_desc = receipe_desc,
        # queryset.receipe_image=receipe_image,                                                                                                                                                                                                                                                                                     
       
        if receipe_image:
           queryset.receipe_image=receipe_image,  
       
        queryset.save()
        return redirect('/vege/receipes/')
    context={"receipes":queryset}
    return render(request,"D:\\relation\\vege\\templates\\update.html", context)
       

def del_receipe(request,id):
    Receipe.objects.get(id=id).delete()
    return redirect('/vege/receipes/')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
      
       
# agr yeh username exists nhi krta toh error aa jaega aur apn login page pae hi rhenege
        if not User.objects.filter(username=username).exists():
            messages.error(request, "invalid username")
            return redirect("/vege/login/")

# aur agr kr gya toh apn ko authenticate kran hoga
        # mtlb isi username ka yhi username h aur isi password ka yhi password h toh apnko vo authenticate krke de dega ki haa aap shi ho
        user = authenticate(username=username, password=password)

        if user is not None:  # mtlb yeh jo user h vo None(wrong) nhi    vhi user h
            login(request,user=user)
            messages.success(request, "Successfully login")
            return redirect('/vege/receipes/')
        else:
            messages.error(request,"You are not a user")
            return redirect('/vege/login/')
           

    return render(request,"D:\\relation\\vege\\templates\\login.html")  
def logout_page(request):
    logout(request)
    return render(request,"D:\\relation\\vege\\templates\\login.html")
 
def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
           messages.info(request, "Username already taken")
           return redirect("/vege/register/")

        
        user = User.objects.create(first_name = first_name , username = username)
        user.set_password(password) 
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('/vege/login/')

    return render(request, 'D:\\relation\\vege\\templates\\register.html')


