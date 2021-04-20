from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from  templates import *
from app.models import *
from .forms import *
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail
from seproject.settings import *
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.urls import reverse, reverse_lazy
from django.db.models import F
# Create your views here.
def index(request):
    return render(request,'index.html')

def registerPage(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				return HttpResponseRedirect('/loginpage')
		context = {'form':form}
		return render(request, 'signup.html', context)

def loginpage(request):
	if request.user.is_authenticated:
		return render(request, 'dashboard.html')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return render(request, 'dashboard.html')
			else:
				messages.info(request, 'invalid credentials')
		return render(request, 'login.html')

#def adminLogin(request):
def sectionpage(request):
    sec=section.objects.filter(facultyid__username=request.user.username);
    return render(request,'sectionpage.html',{'sec':sec})

def create_section(request):
    form=createSection()
    user_email=request.user.email
    username=request.user.username
    if request.method=='POST':
        form=createSection(request.POST)
        if form.is_valid():
            post=form.save(commit = False)
            post.facultyid=request.user
            post.save()
            #data=post.cleaned_data
            #print('===========',post,'========')
            html_content = render_to_string('createsectionemail.html',{'post':post})
            text_content = strip_tags(html_content)
            msg=EmailMultiAlternatives(
            #subject
            'You have successfully created a section',
            #message
            text_content,
            #from
            EMAIL_HOST_USER,
            #to
            [user_email]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            print("Mail successfully sent")
            return HttpResponseRedirect('sectionpage')

    context = {'form':form,'username':username}
    return render(request, 'createSection.html',context)


def delete_section(request,pk):
    sec=section.objects.get(id=pk)
    st=student.objects.filter(section_id_id=pk)
    user=request.user.email
    send_mail=[]
    send_mail.append(user)
    print(st.count())
    for i in range(st.count()):
        print(st[i].student_mail)
        send_mail.append(st[i].student_mail)
    if request.method == "POST":
        #print('========================',sec)
        html_content = render_to_string('deletesectionemail.html',{'sec':sec})
        sec.delete()
        text_content = strip_tags(html_content)
        msg=EmailMultiAlternatives(
        #subject
        'Section deleted successfully',
        #message
        text_content,
        #from
        EMAIL_HOST_USER,
        #to
        send_mail
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        print("Mail successfully sent")
        return HttpResponseRedirect('/sectionpage')
    return render(request,'deleteSection.html',{'sec':sec})


def dashboard(request):
    Resource=resource.objects.all()
    return render(request,'dashboard.html',{'Resource':Resource})

def student_dashboard(request,pk):
    sec=section.objects.get(id=pk)
    #print(pk)
    student_details=student.objects.filter(section_id__facultyid__username=request.user.username,section_id_id=pk)
    #print(sec.section_id,"===============================")
    #print(student_details,"=================================")
    #student_details=student_details.filter()
    return render(request,'student_dashboard.html',{'student_details':student_details})

def studentDetail(request,pk):
    Student=student.objects.get(id=pk)
    return(request,'studentDetail.html',{'Student':Student})

def cancel_lab(request,pk):
    Lab = booking.objects.get(id=pk)
    st=student.objects.filter(section_id__facultyid__username=request.user.username,section_id=Lab.section_id)
    print(st)
    send_mail=[]
    user=request.user.email
    send_mail.append(user)
    print(st.count())
    for i in range(st.count()):
        print(st[i].student_mail)
        send_mail.append(st[i].student_mail)
    if request.method == "POST":
        html_content = render_to_string('deletelabemail.html',{'Lab':Lab})
        Lab.delete()
        text_content = strip_tags(html_content)
        msg=EmailMultiAlternatives(
        #subject
        'Lab cancelled',
        #message
        text_content,
        #from
        EMAIL_HOST_USER,
        #to
        send_mail
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        print("Mail successfully sent")
        return HttpResponseRedirect('/labpage')
    return render(request, 'cancelLab.html',{'Lab':Lab})

def delete_student(request,pk):
    st=student.objects.get(id=pk)
    st_mail=st.student_mail
    print('student mail:',st_mail)
    user=request.user.email
    if request.method == "POST":
        #print('========================',sec)
        html_content = render_to_string('deletestudentemail.html',{'st':st})
        st.delete()
        text_content = strip_tags(html_content)
        msg=EmailMultiAlternatives(
        #subject
        'You have been removed',
        #message
        text_content,
        #from
        EMAIL_HOST_USER,
        #to
        [user,st_mail]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        print("Mail successfully sent")
        return HttpResponseRedirect('/student_dashboard')
    return render(request,'deleteStudent.html',{'st':st})
def booklab(request,pk):
    return HttpResponse("resourcebook")

def availablelab(request):
    Lab=lab.objects.all()
    return render(request,"labs.html",{'Lab':Lab})

def resourcebook(request):
    user=request.user.email
    form = book()
    if request.method=="POST":
        form=book(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            html_content = render_to_string('bookresourceemail.html',{'data':data})
            text_content = strip_tags(html_content)
            msg=EmailMultiAlternatives(
            #subject
            'Resource selected successfully',
            #message
            text_content,
            #from
            EMAIL_HOST_USER,
            #to
            [user]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            print("Mail successfully sent")
            form.save()
            return HttpResponseRedirect("/resourcepage")
    return  render(request,'resource_book.html',{'form':form})

def resourcepage(request):
    res=resource_booking.objects.filter(select_booking__user__username = request.user.username)
    return render(request,'resource.html',{'res':res})

def delete_resource(request,pk):
    res = resource_booking.objects.get(id=pk)
    user=request.user.email
    if request.method == "POST":
        html_content = render_to_string('deleteresourceemail.html',{'res':res})
        res.delete()
        text_content = strip_tags(html_content)
        msg=EmailMultiAlternatives(
        #subject
        'Resource unselected',
        #message
        text_content,
        #from
        EMAIL_HOST_USER,
        #to
        [user]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        print("Mail successfully sent")
        return HttpResponseRedirect('/resourcepage')
    return render(request, 'delete_resource.html',{'res':res})

def labpage(request):
    book=booking.objects.filter(user__username=request.user.username)
    return render(request,'labpage.html',{'book':book})

def logoutuser(request):
    logout(request)
    return render(request,'index.html')
