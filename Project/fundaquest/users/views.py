from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
import smtplib
from django.contrib.sessions.backends.db import SessionStore
import socket
from django.utils.crypto import get_random_string
from subjects.models import Subject
from .models import Student,Teacher,TeacherManager
from .forms import StudentForm,UserRegisterForm,TeacherForm
from django.template import RequestContext

session = SessionStore()



def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		f = StudentForm(request.POST)
		print(f.is_valid())
		print(form.is_valid())

		if (form.is_valid() and f.is_valid()):
			user = form.save()
			#f.user = user
			u = f.save()
			u.user=user
			u.save()
			# user = serializers.serialize('json', self.get_queryset())
			print(type(user))


			auth.login(request, user)
			# request.session["user"] = user
			request.session["role"] = "student"
			return HttpResponseRedirect('/users/sendemails/')
		else:
			 form = StudentForm()
			 f=UserRegisterForm()
			 return render(request, 'users/register.html', {'form':form,'f':f})
	return render(request,'users/register.html',{})

def tregister(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		f = TeacherForm(request.POST)

		print(f.is_valid())
		print(form.is_valid())

		if (form.is_valid() and f.is_valid()):
			user = form.save()
			# f.user = user
			u = f.save()
			u.user=user
			u.save()
			for number in range(1,6):
				x = request.POST.get('subject' + str(number), '')
				if(x != ''):
					print("Subject"+x)
					tm = TeacherManager(teacher = u, subject = Subject.objects.filter(subject_name=x).first())
					tm.save()
				else:
					break

			auth.login(request, user)
			#request.session["user"] = user
			request.session["role"] = "teacher"
			return HttpResponseRedirect('/users/sendemails/')
		else:
			 form = TeacherForm()
			 f=UserRegisterForm()
			 subject=Subject.objects.all()
			 subject_list=list(subject)
			 return render(request, 'users/tregister.html', {'form':form,'f':f,'subject_list':subject_list})
	return render(request,'users/tregister.html',{})


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password =  request.POST['password']
		user = auth.authenticate(username=username, password=password)
		context={}
		if user:
			auth.login(request, user)
			username = request.POST['username']
			request.session['username'] = username
			s=Student.objects.filter(user=user).first()
			if isinstance(s, Student):
				request.session["role"]="student"
				return render(request,'users/login_student.html')
			else:
				request.session["role"]="teacher"
				return render(request, 'users/login_teacher.html')
	return render(request, 'users/login.html', {})


def profile(request):
	if request.session.has_key('username'):
		posts = request.session['username']
		query = User.objects.filter(username=posts)
		return render(request, 'users/profile.html', {"query":query})
	else:
		return render(request, 'users/login.html', {})

def logout(request):
	try:
		auth.logout(request)
		del request.session['username']
	except:
		pass
	return render(request, 'users/login.html', {})


def sendemails(request):
	socket.getaddrinfo('localhost', 8080)
	user = request.user
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login("prizeshbhadaniya@gmail.com","prizesh@345")
	msg='To:'+ user.email +'\n'+'From:prizeshbhadaniya@gmail.com'+'\n'+'Subject:Registration @our app\n'
	msg=msg+ "Hello " +  user.username + ", Thankuh for being part of our us.we provide content and also give platform to student to show their skills.keep Learning!!!"
	server.sendmail("prizeshbhadaniya@gmail.com", user.email, msg)
	if request.session['role']=='student':
		return render(request,'users/login_student.html')
	else:
		return render(request,'users/login_teacher.html')

def forgethtml(request):
	return render(request,'users/justmail.html')

def forget(request):
	otp = get_random_string(6, allowed_chars='0123456789')
	print(otp)
	request.session['otp']=otp
	socket.getaddrinfo('localhost', 8080)
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login("prizeshbhadaniya@gmail.com","prizesh@345")
	email=request.POST.get('mail','')
	msg='To:'+ email+'\n'+'From:prizeshbhadaniya@gmail.com'+'\n'+'Subject:set new password\n'
	msg = msg +'hello , our provided otp is  ' + otp
	server.sendmail("prizeshbhadaniya@gmail.com",email,msg)
	print("Mail Sent Successfully")
	return render(request,'users/otp.html')

def verify(request):
	otp=request.POST.get('otp','')
	print(otp)
	print(request.session['otp'])
	if (otp==request.session['otp']):
		return render(request,'users/set.html')
	else:
		messages.add_message(request, messages.ERROR, "Invalid OTP, please enter valid OTP.")
		return render(request,'users/otp.html')

def set(request):
	uname=request.POST.get('uname','')
	pass1=request.POST.get('pass','')
	repass=request.POST.get('repass','')
	if pass1==repass:
		user = User.objects.filter(username=uname).first()
		user.set_password(pass1)
		user.save()
		user1 = auth.authenticate(username=uname, password=pass1)
		auth.login(request, user1)
		s=Student.objects.filter(user=user).first()
		if isinstance(s, Student):
			request.session["role"]="student"
			return render(request,'users/login_student.html')
		else:
			request.session["role"]="teacher"
			return render(request, 'users/login_teacher.html')
		return render(request,'users/set.html')

def loginstudent(request):
	 return render(request,'users/login_student.html')

def back(request):
	if (request.session["role"] == 'student'):
		 return render(request,'users/login_student.html')
	else:
		 return render(request,'users/login_teacher.html')
