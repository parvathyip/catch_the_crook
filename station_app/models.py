from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Login_Table(AbstractUser):
    user_type=models.CharField(max_length=30)
    view_password=models.CharField(max_length=30)
class Register_dgp(models.Model):
    user_login=models.ForeignKey(Login_Table,on_delete=models.CASCADE)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    image=models.ImageField(max_length=100)
    job_status=models.CharField(max_length=20)
    office_address=models.TextField()
    office_district=models.CharField(max_length=15)
    email=models.EmailField(null=True)

class Register_station(models.Model):
    user_login=models.ForeignKey(Login_Table,on_delete=models.CASCADE)
    dgp=models.ForeignKey(Register_dgp,on_delete=models.CASCADE)
    station_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    office_address=models.TextField()
    email=models.EmailField(null=True)

class Register_wanted(models.Model):
    station=models.ForeignKey(Register_station,on_delete=models.CASCADE,null=True)
    fname=models.CharField(max_length=30,null=True)
    lname=models.CharField(max_length=30,null=True)
    father_name=models.CharField(max_length=30,null=True)
    age=models.CharField(max_length=30,null=True)
    sex=models.CharField(max_length=30,null=True)
    address=models.TextField(null=True)
    # date_of_arrest=models.DateField(auto_now_add=True,null=True)
    mode_of_crime=models.CharField(max_length=30,null=True)
    crime_desc=models.TextField(null=True)
    wanted_status=models.CharField(max_length=15,default="wanted")

class Wanted_images(models.Model):
    wanted=models.ForeignKey(Register_wanted,on_delete=models.CASCADE)
    wanted_images=models.ImageField()

class Register_public(models.Model):
    user_login=models.ForeignKey(Login_Table,on_delete=models.CASCADE)
    f_name=models.CharField(max_length=30)
    l_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    email=models.EmailField()
    district=models.CharField(max_length=15,null=True)

class Add_complaint(models.Model):
    complaint_date=models.DateField(auto_now_add=True,null=True)
    public=models.ForeignKey(Register_public,on_delete=models.CASCADE ,null=True)
    missing_image=models.ImageField(blank=True)
    missing_desc=models.TextField(blank=True)
    crime_mode=models.CharField(max_length=30,blank=True)
    crime_desc=models.TextField(blank=True)
    complaint_type_status=models.CharField(max_length=10,default="missing")
    complaintid=models.CharField(max_length=100, null=True)
    complaint_status=models.CharField(max_length=10,default="Pending")
    station=models.ForeignKey(Register_station,on_delete=models.CASCADE,blank=True,null=True)
    criminal=models.ForeignKey(Register_wanted,on_delete=models.CASCADE,blank=True,null=True)
    witness_fname=models.CharField(max_length=30,null=True)
    witness_lname=models.CharField(max_length=30,null=True)
    witness_phone=models.CharField(max_length=30,null=True)
    witness_email=models.EmailField(null=True)
    witness_district=models.CharField(max_length=30,null=True)
    fir_upload=models.FileField(null=True)

class Public_feedback(models.Model):
    public=models.ForeignKey(Register_public,on_delete=models.CASCADE)
    wanted=models.ForeignKey(Register_wanted,on_delete=models.CASCADE)
    feedback=models.TextField()