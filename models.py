from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class job_list(models.Model):
    job_id = models.AutoField(primary_key=True)
    Company_name = models.CharField(max_length=50)
    Company_title = models.CharField( max_length=50)
    salary_month = models.CharField(max_length=50)
    job_post = models.CharField(max_length=50)
    job_desc = models.CharField( max_length=5000)
    job = models.CharField( max_length=50)
    
    def __str__(self) -> str:
        return self.Company_name
    
skill_keyword=('python','html','css','java')
class job_details(models.Model):
    org_id= models.IntegerField(max_length=True)
    bu_id= models.IntegerField(max_length=True)
    bu_loc_id= models.IntegerField(max_length=True)
    job_id = models.AutoField(primary_key=True)
    job_post = models.CharField(max_length=50)
    job_vacancy = models.IntegerField(max_length=50)
    experience = models.CharField(max_length=5000)
    employee_type = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    salary_month = models.CharField(max_length=100)
    job_desc = models.CharField(max_length=5000)
    responsibility = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    requirements = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    enable = models.BooleanField(default=True)
    skill_keywords = models.CharField(max_length=500)
    job_start_date=models.DatetimeField(auto_now_add=True)
    creation_date=models.DatetimeField(auto_now_add=True)
    created_by=models.IntegerField(max_length=12)
    last_updated_date=models.DatetimeField(auto_now_add=True)
    last_updated_by=models.IntegerField(max_length=12)
    job_duration =models.CharField(max_length=100)
    
    class Meta():
        unique_together=('job_post', 'position')
    
    def __str__(self):
        return self.job_post


class candidate_details(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    categories = models.CharField(max_length=50)
    languages = models.CharField(max_length=500)
    experince = models.CharField(max_length=5000)
    qualification = models.CharField(max_length=500)
    phone = PhoneNumberField(unique=True)
    about_me = models.CharField(max_length=500)
    education = models.CharField(max_length=5000)
    experience_desc = models.CharField(max_length=500)
    projects = models.CharField(max_length=5000)
    # filefield or filepathfield
    cv = models.FileField()
    
    def __str__(self) -> str:
        return self.name

class candidate_list(models.Model):
    job_id = models.ForeignKey(job_list,on_delete=models.CASCADE)
    cadidate_id = models.ForeignKey(candidate_details,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return job_list.Company_name
    
    
