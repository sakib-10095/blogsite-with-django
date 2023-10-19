from django.shortcuts import render,redirect
from myapp.models import Post
from myapp.forms import SignUpForm, loginForm
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required




# Create your views here.
def homePage(request):
    report=Post.objects.all()
    return render(request,"home.html",{'report':report})    

    

@login_required
def contactPage(request):
    return render(request,"contact.html")


def aboutPage(request):
    return render(request,"about.html")

@login_required
def Dashboard(request):
    return render(request,"dasboard.html")


def singupPage(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations !! you have successfully sinup.')
            form.save()
            return redirect('loginPage')
    else:
        form=SignUpForm()
    return render(request,"singup.html",{'form':form})



def loginPage(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=loginForm(request=request, data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=auth.authenticate(username=uname,password=upass)
                if user != None:
                    login(request,user)
                    messages.success(request, 'Crongratulations!! you have successfully login')
                    return redirect('Dashboard')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            form=loginForm()
        return render(request,"login.html",{'form':form})
    else:
        return redirect('Dashboard')
   
def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def updatepost(request):
    return render(request,'update.html')
