from django.db import models
from datetime import date
from accounts.models import User


class Pastorate(models.Model):
    # name = models.CharField(max_length=100)
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name

    def __str__(self):
        return str(self.name)

# Create your models here.
class Team_Lead(models.Model):
    # name = models.CharField(max_length=100)
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name

    def __str__(self):
        return str(self.name)
    
   

class TeamMember(models.Model):
    # name1 = models.CharField(max_length=15, blank=True, null=True)
    team_lead = models.ForeignKey(Team_Lead, on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name\
    def __str__(self):
        return str(self.name)

class Member(models.Model):
    
    MALE = 1
    FEMALE = 2
    SINGLE = 1
    MARRIED = 2
    TEENAGER = 3
    CHILDREN = 4
    PRIVATE = 1
    STATE = 2
    FEDERAL = 3
    ACTIVE = 1
    INACTIVE = 2

    
    
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
       
    )
    
    MARITAL = (
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
        (TEENAGER, 'Teenager'),
        (CHILDREN, 'Children'),
       
    )

    STATUS = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
       
    )

  

    image = models.ImageField(upload_to='images/')
    first_name = models.CharField(max_length=52)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    email = models.EmailField(max_length=52)
    phone_no = models.CharField(max_length=15)
    gender = models.PositiveIntegerField(choices=GENDER)
    marital_status = models.PositiveIntegerField(choices=MARITAL)
    occupation = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=20)
    kcc_center = models.CharField(max_length=20,blank=True, null=True)
    place_of_work = models.CharField(max_length=50,blank=True, null=True)
    position = models.CharField(max_length=40,blank=True, null=True)
    
    wedding_ann = models.DateField(blank=True, null=True)
    join = models.DateField(blank=True, null=True)
    # reg_date = models.CharField(max_length=20, blank=True, null=True)
    about = models.CharField(max_length=20,blank=True, null=True)
    dept = models.CharField(max_length=20,blank=True, null=True)
    purpose = models.CharField(max_length=20,blank=True, null=True)
    team_lead = models.CharField(max_length=20, blank=True, null=True)
    team_member = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.PositiveIntegerField(choices=STATUS, default='1', blank=True)
    kin_fullname = models.CharField(max_length=50, blank=True, null=True)
    kin_birth = models.DateField(null=True, blank=True)
    kin_gender = models.CharField(max_length=20, blank=True, null=True)
    kin_relationship = models.CharField(max_length=20, blank=True, null=True)
    kin_address = models.CharField(max_length=100, blank=True, null=True)
    kin_phone_no = models.CharField(max_length=20, blank=True, null=True)
    kin_email = models.CharField(max_length=50, blank=True, null=True)
    emergency_phone_no = models.CharField(max_length=20, blank=True, null=True)


    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
  
 

    def __str__(self):
        return self.first_name



    

class Comment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='comments')
    first_name = models.CharField(max_length=40, blank=False, null=False )
    last_name = models.CharField(max_length=25, blank=True, null=True)
    phone_no = models.CharField(max_length=25, blank=True, null=True)
    team_sup = models.ForeignKey(User, on_delete=models.CASCADE)
    team_mem = models.CharField(max_length=50, blank=True, null=True)
    coor_comm = models.CharField(max_length=30, blank=True, null=True)
    date_created = models.DateField(default=date.today, blank=True, null=True)
    comment = models.TextField()
  
   


    def __str__(self):
        return self.first_name






from django.db import models
from .models import Member

class Family(models.Model):
    husband = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='husband')
    wife = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='wife')

    family_name = models.CharField(max_length=100)
    
    team_lead = models.CharField(max_length=20, blank=True, null=True)
    team_member = models.CharField(max_length=20, blank=True, null=True)
  
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.full_name



class Child(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    




class Student(models.Model):
    UNDERGRADUATE = 'UG'
    POSTGRADUATE = 'PG'
    PROGRAM_CHOICES = [
        (UNDERGRADUATE, 'Undergraduate'),
        (POSTGRADUATE, 'Postgraduate'),
    ]

    INTERNSHIP = 'Internship'
    PART_TIME_JOB = 'Part-time job'
    WORK_TYPE_CHOICES = [
        (INTERNSHIP, 'Internship'),
        (PART_TIME_JOB, 'Part-time job'),
    ]

    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    parent_address = models.CharField(max_length=255)
    parent_phone_number = models.CharField(max_length=15)
    university_name = models.CharField(max_length=255)
    program_of_study = models.CharField(max_length=255)
    program = models.CharField(max_length=2, choices=PROGRAM_CHOICES)
    work_type = models.CharField(max_length=50, choices=WORK_TYPE_CHOICES)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)  # E.g., "June 2020 - August 2020"
    responsibilities = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} - {self.university_name}"






class NYSC(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    parent_address = models.CharField(max_length=255)
    parent_phone_number = models.CharField(max_length=20)
    university_name = models.CharField(max_length=100)
    program_of_study = models.CharField(max_length=100)
    year_of_graduation = models.IntegerField()
    place_of_assignment = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.university_name} - {self.program_of_study}"




class Children(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)  # 'class' is a reserved keyword in Python, so use 'class_name' instead
    allergies = models.TextField(blank=True, null=True)
    medical_conditions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    


# models.py

# from django.db import models
# from django.utils.translation import gettext_lazy as _



# class Kbn(models.Model):
#     member = models.ForeignKey(Member, on_delete=models.CASCADE)
#     business_name = models.CharField(max_length=255)
#     designation = models.CharField(max_length=255)
#     is_registered = models.BooleanField(default=False, verbose_name=_("Is business registered"))
#     brief_description = models.TextField(blank=True)
#     years_of_experience = models.PositiveIntegerField(default=0, verbose_name=_("Years of business experience"))
#     number_of_employees = models.PositiveIntegerField(default=1)
#     BUSINESS_SECTORS = [
#         ("Technology", "Technology"),
#         ("Finance", "Finance"),
#         ("Healthcare", "Healthcare"),
#         ("Education", "Education"),
#         ("Manufacturing", "Manufacturing"),
#         ("Real Estate", "Real Estate"),
#         ("Hospitality", "Hospitality"),
#         ("Retail", "Retail"),
#         ("Entertainment", "Entertainment"),
#         # Add more sectors as needed
#     ]
#     business_sector = models.CharField(max_length=100, choices=BUSINESS_SECTORS)
#     current_employment_job_title = models.CharField(max_length=100, blank=True, null=True)
#     current_employment_company_name = models.CharField(max_length=100, blank=True, null=True)
#     current_employment_duration = models.CharField(max_length=100, blank=True, null=True)
#     current_employment_responsibilities = models.TextField(blank=True, null=True)
#     previous_employment_job_title = models.CharField(max_length=100, blank=True, null=True)
#     previous_employment_company_name = models.CharField(max_length=100, blank=True, null=True)
#     previous_employment_duration = models.CharField(max_length=100, blank=True, null=True)
#     previous_employment_responsibilities = models.TextField(blank=True, null=True)
#     highest_qualification_degree = models.CharField(max_length=100, blank=True, null=True)
#     highest_qualification_institution = models.CharField(max_length=100, blank=True, null=True)
#     highest_qualification_year_of_graduation = models.PositiveIntegerField(blank=True, null=True)
#     highest_qualification_gpa = models.FloatField(blank=True, null=True)
#     other_qualification_certification = models.CharField(max_length=100, blank=True, null=True)
#     other_qualification_institution = models.CharField(max_length=100, blank=True, null=True)
#     other_qualification_year_of_graduation = models.PositiveIntegerField(blank=True, null=True)
#     other_qualification_gpa = models.FloatField(blank=True, null=True)
#     skills = models.TextField(blank=True, null=True)
#     achievements_and_awards = models.TextField(blank=True, null=True)
#     additional_information = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.business_name


from django.db import models
from django.utils.translation import gettext as _

class Business(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    is_registered = models.BooleanField(default=False, verbose_name=_("Is business registered"))
    brief_description = models.TextField(blank=True)
    years_of_experience = models.PositiveIntegerField(default=0, verbose_name=_("Years of business experience"))
    number_of_employees = models.PositiveIntegerField(default=1)
    BUSINESS_SECTORS = [
        ("Technology", "Technology"),
        ("Finance", "Finance"),
        ("Healthcare", "Healthcare"),
        ("Education", "Education"),
        ("Manufacturing", "Manufacturing"),
        ("Real Estate", "Real Estate"),
        ("Hospitality", "Hospitality"),
        ("Retail", "Retail"),
        ("Entertainment", "Entertainment"),
        # Add more sectors as needed
    ]
    business_sector = models.CharField(max_length=100, choices=BUSINESS_SECTORS)

    def __str__(self):
        return self.business_name


class Career(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    skills = models.TextField(blank=True, null=True)
    achievements_and_awards = models.TextField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


class CurrentEmployment(models.Model):
    career = models.ForeignKey(Career, related_name='current_employments', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)
    

class PreviousEmployment(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class EducationalBackground(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    year_of_graduation = models.PositiveIntegerField(blank=True, null=True)
    gpa = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class OtherQualification(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    certification = models.CharField(max_length=100, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    year_of_graduation = models.PositiveIntegerField(blank=True, null=True)
    gpa = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.certification



