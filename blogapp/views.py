from django.shortcuts import render,redirect
from .models import*
from blog.forms import Blogforms , Contactform
import requests
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@never_cache
def home(request):
    if request.method == 'POST':
        search_post = request.POST['search']
        if Blog.objects.filter(title__contains=search_post).exists():
            posts = Blog.objects.filter(title__contains=search_post)
            return render(request,'show.html',{'data':posts})
        else:
            messages.error(request,'No result found ')
            return redirect('home')
    data=Blog.objects.all()       
    return render(request,'index.html',{'data':data})
def expertise(request):
    return render(request,'expertise.html',{})    
def project(request):
    return render(request,'project.html',{})    
def career(request):
    return render(request,'career.html',{})     


def Contact(request):
    if request.method=="POST":
        form=Contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup')
    else:
        form=Contactform(request.GET)
        return render(request,'contact.html',{'form':form})    

@login_required(login_url='login')
def addblog(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=Blogforms(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form=Blogforms(request.GET)
            return render(request,'blog.html',{'form':form}) 
    else:
        return redirect('login')   

@never_cache
def blog(request):
    data=Blog.objects.all()       
    return render(request,'index.html',{'data':data})
        

def rmore(request,id):

    data=Blog.objects.get(id=id)       
    return render(request,'readmore.html',{'i':data})
                
def editblog(request,id):
    data = Blog.objects.get(id=id)
    if User.is_authenticated:
        if request.method=="POST":
                form=Blogforms(request.POST,request.FILES,instance=data)
                if form.is_valid():
                    form.save()
                    return redirect('home')
        else:
            form=Blogforms(instance=data)
            return render(request,'blog.html',{'form':form})    
    else:
        return redirect('login')   

def deleteblog(request,id):
    data = Blog.objects.get(id=id)
    data.delete()
    return redirect('home')

@never_cache
def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        image=request.FILES['image']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Already Exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email Already Exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                Profile.objects.create(username = username,image=image)
                return redirect('signup')
        else:
            messages.error(request,'Try Matching Password')
            return redirect('signup')    
    return render(request,'signup.html')

@never_cache
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            messages.error(request,'Username Or Password Is Incorrect')
            return redirect('login')
    else:
        return render(request,'login.html')           
@never_cache
def logout(request):
    auth.logout(request)
    return redirect('login')

def showQuestion(request):
    url="https://imdb8.p.rapidapi.com/auto-complete"

    querystring = {"q":"game of thr"}

    headers = {
        "X-RapidAPI-Key": "58b76fa1c5msh1c4d8fa8836771ep1cd497jsn2dc515cee937",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    
    return render(request,'show.html',{'data':response})

def ownblog(request):
    data=Blog.objects.filter(created_by=request.user)
    return render(request,'ownblog.html',{'data':data})    


def profile(request):
    if Profile.objects.filter(username__exact = request.user).exists():
        data=Profile.objects.get(username__exact =request.user)
        return render(request,'profile.html',{'data':data})
    return render(request,'profile.html')

# def addimg(request):
#      if request.method == "POST":
#         return render(request,'addimg.html')

def imgupdate(request,id):
    if User.is_authenticated:
        data = Profile.objects.get(id=id)
        if request.method == 'POST':
            profile=request.FILES['profile']
            Profile(id=id,username=data.username,image=profile).save()
            return redirect('profile')
        return render(request,'imgupdate.html',{})


# def showresult(request):
#     search_data = request.GET.get('search1')
#     print(search_data)
#     if search_data:
#         data = Blog.objects.filter(Q(title__icontains=search_data) & Q(content__icontains=search_data))    
#     else:
#         data = Blog.objects.all()
#         messages.error(request,'No result found ')
#         return redirect('home')
#     return render(request,'index.html',{'data':data})
        
    # if request.POST=='search':
    #     if Blog.objects.filter(request.POST).exists():
    #         data=Blog.objects.get(title__exact=request.Blog)
    #   
    # else:
    #     #     return redirect('home')
    
