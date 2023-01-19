from django.shortcuts import render
from datetime import datetime
from tgapp.models import GetInTouch,CourseApplied,Carousal,AboutUs,DirTeam,LeadTeam,DevTeam,Service,LinkService,Gallery,Blog,Job,Working,Course,ClientandCollab
from django.contrib import messages
from django import template


# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        question=request.POST.get('question')
        contact=GetInTouch(name=name,email=email,phone=phone,question=question,date=datetime.today())
        contact.save()
    car=Carousal.objects.all()
    about=AboutUs.objects.filter(id=1).values_list('text',flat=True)
    mission=AboutUs.objects.filter(id=1).values_list('mission',flat=True)
    plan=AboutUs.objects.filter(id=1).values_list('plan',flat=True)
    vision=AboutUs.objects.filter(id=1).values_list('vision',flat=True)
    dirteam=DirTeam.objects.all()
    devteam=DevTeam.objects.all()
    leadteam=LeadTeam.objects.all()
    services=Service.objects.all()
    linkservices=LinkService.objects.all()
    gallery=Gallery.objects.all()
    blogs=Blog.objects.all()
    career=Job.objects.all()
    working=Working.objects.all()
    clandco=ClientandCollab.objects.all()
    course=Course.objects.all().order_by('-id')[:3]
    return render(request,'index.html',{'car':car,'about':about,'mission':mission,'plan':plan,'vision':vision,'dirteam':dirteam,'devteam':devteam,'leadteam':leadteam,'services':services,'linkservices':linkservices,'gallery':gallery,'blogs':blogs,'career':career,'working':working,'clandco':clandco,'course':course})

def education(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        if request.POST.get("course"):
            course=CourseApplied()
            course=request.POST.get("course")
        apply=CourseApplied(name=name,email=email,opt=course,date=datetime.today())
        apply.save()
    return render(request,'education.html')

def courses(request):
    clandco=ClientandCollab.objects.all()
    course=Course.objects.all().order_by('-id') 
    return render(request,'courses.html',{'course':course})