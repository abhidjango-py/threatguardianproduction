from django.db import models
# Create your models here.
class GetInTouch(models.Model):
    name=models.CharField(max_length=100,null=False)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=12)
    question=models.TextField(default="No text just connecting")
    date=models.DateTimeField()
    def __str__(self):
        return self.name

class CourseApplied(models.Model):
    email=models.EmailField(max_length=100,null=False)
    name=models.CharField(max_length=100)
    opt=models.CharField(max_length=20,default="Just Connecting")
    date=models.DateTimeField()
    def __str__(self):
        return "%s | %s | %s" %(self.email,self.name,self.opt)

class Carousal(models.Model):
    text=models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.text

class DirTeam(models.Model):
    photo=models.ImageField(upload_to='static/')
    name=models.CharField(max_length=50,null=False)
    desg=models.CharField(max_length=50,null=False)
    twitter=models.URLField(max_length=50,null=True)
    linkedin=models.URLField(max_length=50)
    gmail=models.URLField(max_length=50)
    def __str__(self):
        return self.name

class LeadTeam(models.Model):
    photo=models.ImageField(upload_to='static/')
    name=models.CharField(max_length=50,null=False)
    desg=models.CharField(max_length=50,null=False)
    twitter=models.URLField(max_length=50,null=True)
    linkedin=models.URLField(max_length=50)
    gmail=models.URLField(max_length=50)
    def __str__(self):
        return self.name

class DevTeam(models.Model):
    photo=models.ImageField(upload_to='static/')
    name=models.CharField(max_length=50,null=False)
    desg=models.CharField(max_length=50,null=False)
    linkedin=models.URLField(max_length=50)
    def __str__(self):
        return self.name

class Service(models.Model):
    icontext=models.CharField(max_length=50)
    heading=models.CharField(max_length=50)
    text=models.TextField(max_length=1000)
    def __str__(self):
        return self.heading

class LinkService(models.Model):
    icontext=models.CharField(max_length=50)
    heading=models.CharField(max_length=50)
    text=models.TextField(max_length=1000)
    link=models.TextField(max_length=50)
    def __str__(self):
        return self.heading

class AboutUs(models.Model):
    text=models.TextField(max_length=1000,null=False)
    mission=models.TextField(max_length=250,null=False)
    plan=models.TextField(max_length=250,null=False)
    vision=models.TextField(max_length=250,null=False)

class Gallery(models.Model):
    image=models.ImageField(upload_to='static/')
    alt=models.CharField(max_length=50)
    def __str__(self):
        return self.alt
class Blog(models.Model):
    type=models.CharField(max_length=50)
    heading=models.CharField(max_length=50)
    date=models.DateField()
    desc=models.TextField()
    link=models.URLField()
    image=models.ImageField(upload_to='static/')
    def __str__(self):
        return self.heading

class Job(models.Model):
    block=models.CharField(max_length=5)
    heading=models.CharField(max_length=50)
    jobdesc=models.CharField(max_length=100)
    reqskill=models.CharField(max_length=100)
    apply=models.BooleanField(default=True)
    def __str__(self):
        return self.block

class Working(models.Model):
    image=models.ImageField(upload_to='static/')
    alt=models.CharField(max_length=50)
    def __str__(self):
        return self.alt

class Course(models.Model):
    image=models.ImageField(upload_to='static/')
    heading=models.CharField(max_length=50)
    duration=models.CharField(max_length=50)
    apply=models.BooleanField(default=True)
    def __str__(self):
        return self.heading

class ClientandCollab(models.Model):
    image=models.ImageField(upload_to='static/')
    alt=models.CharField(max_length=50)
    def __str__(self):
        return self.alt