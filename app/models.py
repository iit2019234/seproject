from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class section(models.Model):
    section_id=models.CharField(max_length=122,null = True)
    facultyid = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    def __str__(self):
        return '%s %s' %(self.section_id,self.facultyid)

class resource(models.Model):
    resource_name=models.CharField(max_length=122,null = True)
    resource_id=models.CharField(max_length=122,null = True)
    quantity=models.IntegerField(null = True)

    def __str__(self):
        return '%s' %(self.resource_id)

class student(models.Model):
    section_id=models.ForeignKey(section,null = True,on_delete = models.SET_NULL)
    student_name=models.CharField(max_length=122,null = True)
    student_id=models.CharField(max_length=122,null = True)
    student_mail=models.CharField(max_length=122,null = True)
    def __str__(self):
        return '%s' %(self.student_id)

class lab(models.Model):
    lab_id=models.CharField(max_length=122,null = True)
    def __str__(self):
        return '%s '%(self.lab_id)

class booking(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    lab_id=models.ForeignKey(lab,null = True,on_delete = models.SET_NULL)
    section_id=models.ForeignKey(section,null = True,on_delete = models.SET_NULL)
    startDate=models.DateTimeField()
    lastDate=models.DateTimeField()
    def __str__(self):
        return '%s %s - %s' %(self.user,self.lab_id,self.section_id)

class resource_booking(models.Model):
    status_category=(("Pending","Pending"),
                      ("Accepted","Accepted"),
                      ("Declined","Declined"))
    select_booking=models.ForeignKey(booking,on_delete = models.CASCADE)
    select_resource=models.ForeignKey(resource,on_delete = models.CASCADE)
    quantity=models.IntegerField()
    status=models.CharField(max_length=12,choices=status_category,default='Pending')
    def __str__(self):
        return '%s %s'%(self.select_booking,self.select_resource)
