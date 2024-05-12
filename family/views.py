from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    peoples = [
        {"name":"abijeet gupta","age":34},
        {"name":"mayank gupta","age":15},
        {"name":"manish gupta","age":18},
        {"name":"rohan gupta","age":10}
    ]
    vegetables=[
        'pumpkin','tomato','potato'
    ]
    return render(request,"C:\\Users\\asus\\relation\\family\\templates\\index.html",context={"peoples":peoples ,"vegetables":vegetables})

def about(request):
    context={"page":"about"} #iska mtlb h ki upar notification mae  about page likha hua aajaega
    return render(request,"C:\\Users\\asus\\relation\\family\\templates\\about.html",context)

def contact(request):
      context={"page":"contact"}#iska mtlb h ki upar notification mae  contact page likha hua aajaega
      return render(request,"C:\\Users\\asus\\relation\\family\\templates\\contact.html",context)


    
        