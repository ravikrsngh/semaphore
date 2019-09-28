from django.shortcuts import render,get_object_or_404
from .forms import *
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.urls import reverse
import smtplib
from email.mime.multipart import MIMEMultipart
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.decorators import login_required
from email.mime.text import MIMEText
# from selenium import webdriver
# import pdfkit
import random
import string
from django.core.mail import send_mail, EmailMessage
# Create your views here.
def price(name):
	print(name)
	if name == "QUIZ (TEAM OF TWO)":
		p=150
	elif name == "PUBG (TEAM OF 4)":
		p=200
	elif name == "PUBG (TEAM OF 3)":
		p=150
	elif name == "PUBG DUO":
		p=100
	elif name == "PHOTOGRAPHY":
		p=50
	elif name == "RAFFLE":
		p=30
	elif name == "TREASURE HUNT":
		p=200
	elif name == "60 SECONDS OF FAME":
		p=100
	elif name == "TYPOTHON":
		p=50
	elif name == "HOW WELL DO YOU KNOW":
		p=50
	elif name == "GULLY CRICKET":
		p=300
	elif name == "CODE JAM":
		p=100
	elif name == "ARM WRESTLING":
		p=50
	elif name == "QUIZ SOLO":
		p=50
	elif name == "MOCK PLACEMENT":
		p=100
	elif name == "HOGOTHON":
		p=100
	elif name == "PUBG SOLO":
		p=50
	elif name == "BLIND CODING":
		p=100
	return p

def others(request,pk):
	user=User.objects.get(pk=pk)

	m=marketer.objects.filter(undercover=False)
	return render(request,'others.html',{'user':user,'m':m})
def other_view(request,pk,id):
	user=User.objects.get(pk=pk)
	m=User.objects.get(pk=id)
	m=userprofile.objects.filter(person=m.first_name)
	print(m)
	return render(request,'exform.html',{'user':user,'m':m})
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def ulogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('app:profile',args=(user.id,)))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Some one tried to login but failed")
            return HttpResponse("Invalid details")
    else:
        return render(request,'login.html',{})
@login_required
def ulogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:home'))


def email_otp(email,name,eve,username):
	mail_subject = 'Your OTP is :.'

	body="Hi ,"\
		+name\
		+"\n\n"\
		+"Thank you for registering in "\
		+eve\
		+" event in SEMAPHORE 2k19.\n Your unique id is :- "\
		+username\
		+"\n\nThanks,\nSEMAPHORE 2019."
	message = str(MIMEText(body,'plain'))
	from_email='semaphore794@gmail.com'
	to_list=[email]
	print(to_list)
	s= smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login('semaphore794@gmail.com','gzygpdajxwjgeqkb')
	s.sendmail(from_email,to_list,message)
	s.quit()
	print("Email Sent")

def register(request,pk):
	user=User.objects.get(pk=pk)
	m=marketer.objects.get(user=user)
	if request.method == "POST":
		print("REQUEST IS POST")
		user_form=userform(data=request.POST)
		userprofile_form=userprofileform(data=request.POST)
		if user_form.is_valid() and userprofile_form.is_valid():
			print("form is valid ")
			u=user_form.save(commit=False)
			profile=userprofile_form.save(commit=False)
			u.username=randomString()
			u.password="123456789"
			m.noreg=m.noreg+1
			m.t_reg=m.t_reg+1
			print(price(profile.eve.name))
			m.total_amount=m.total_amount+price(profile.eve.name)
			m.t_amount=m.t_amount+price(profile.eve.name)
			if m.total_amount in range(0,5001) and m.undercover:
				m.income=m.total_amount*0.05
			if m.total_amount in range(5001,6001) and m.undercover:
				m.income=m.total_amount*0.06
			if m.total_amount in range(6001,7001) and m.undercover:
				m.income=m.total_amount*0.07
			if m.total_amount in range(7001,8001) and m.undercover:
				m.income=m.total_amount*0.08
			if m.total_amount in range(8001,9001) and m.undercover:
				m.income=m.total_amount*0.09
			if m.total_amount>9001 and m.undercover:
				m.income=m.total_amount*0.1
			profile.person=user.first_name
			email_otp(user.email,user.first_name,profile.eve.name,u.username)
			m.save()
			u.save()
			profile.user=u
			profile.save()
			return HttpResponseRedirect(reverse('app:profile',args=(user.id,)))
		else:
			print(user_form.errors,userprofile_form.errors)
			return HttpResponse("INVALID")
	else:
		user_form=userform()
		userprofile_form=userprofileform()
		return render(request,'register.html',{'user_form':user_form,'userprofile_form':userprofile_form})


def exform(request,pk):
	user=User.objects.get(pk=pk)
	m=userprofile.objects.filter(person=user.first_name)
	print(m)
	return render(request,'exform.html',{'user':user,'m':m})


def profile(request,pk):
	user=User.objects.get(pk=pk)
	print(user.marketer.boss)
	return render(request,'profile.html',{'user':user})


def home(request):
    return render(request,'home.html',{})
def about(request):
    return render(request,'about.html',{})
def events(request):
    return render(request,'events.html',{})
def gallery(request):
    return render(request,'gallery.html',{})
def contact(request):
    return render(request,'contact.html',{})
