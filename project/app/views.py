
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def get_usr(req):
    data=Register.objects.get(Email=req.session['user'])
    return data





def login(req):
    if 'user' in req.session:
        return redirect(userhome)

    if req.method=='POST':
        email=req.POST['Email']
        password=req.POST['password']
        try:
            data=Register.objects.get(Email=email,password=password)
            req.session['user']=data.Email
            return redirect(userhome)
        except:
            shop=auth.authenticate(username=email,password=password)
            if shop is not None:
                auth.login(req,shop)
                req.session['shop']=email

                return redirect(adminhome)


            messages.warning(req, "INVALID INPUT !")
    return render(req,'login.html')



def logout(req):
    if 'user' in req.session:
        # req.session.flush()
        del req.session['user']
    if 'shop' in req.session:
        del req.session
    return redirect(login)


def register(req):

    if req.method=='POST':
        name1=req.POST['name']
        email2=req.POST['email']
        phonenumber3=req.POST['phonenumber']
        location4=req.POST['location']
        password5=req.POST['password']
        try:
            data=Register.objects.create(name=name1,Email=email2,phonenumber=phonenumber3,location=location4,password=password5)
            data.save()
            return redirect(login)
        except:
            messages.warning(req, "Email Already Exits , Try Another Email.")
    return render(req,'register.html')


def userhome(req):
    if 'user' in req.session:
        return render(req,'userhome.html')
    else:
        return redirect(login)


def adminhome(req):
    
    return render(req,'adminhome.html')


###profile
def profile(req):
    if 'user' in req.session:
        # data=Register.objects.get(Email=req.session['user'])
        return render(req,'profile.html',{'data':get_usr(req)})
    else:
        return redirect(login)
    

###profile update
def upload(req):
    if 'user' in req.session:
        data=Register.objects.get(Email=req.session['user'])
        if req.method=='POST':
            name=req.POST['name']
            phonenumber=req.POST['phonenumber']
            location=req.POST['location']
            Register.objects.filter(Email=req.session['user']).update(name=name,phonenumber=phonenumber,location=location)
            return redirect(profile)
        return render(req,'upload.html',{'data':data})

    else:
       return redirect(login)
      
  
def viewuser(req):
    return render(req,'viewuser.html')


def addpro(req):
    return render(req,'addpro.html')


def viewpro(req):
    return render(req,'viewpro.html')


def bookinghistry(req):
    return render(req,'bookinghistry.html')