from django.db import models
from datetime import date
from accounts.models import User




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
       
    )

    STATUS = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
       
    )

  
    # coordinator = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='coordinator')
    # team_member = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='team_member')
    # custom_id = models.CharField(primary_key = True, max_length=10, unique=True, default=custom_id)
    image = models.ImageField(upload_to='images/')
    first_name = models.CharField(max_length=50, blank=False, null=False , unique=True,)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    date_of_birth = models.CharField(max_length=15, blank=True, null=True)

    email = models.EmailField(max_length=45, blank=True, null=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    gender = models.PositiveIntegerField(choices=GENDER, blank=True, null=True)
    marital_status = models.PositiveIntegerField(choices=MARITAL, blank=True, null=True)
    occupation = models.CharField(max_length=20, blank=True,null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)
    kcc_center = models.CharField(max_length=20, blank=True, null=True)
    
    wedding_ann = models.CharField(max_length=30, blank=True, null=True)
    join = models.CharField(max_length=20, blank=True, null=True)
    # reg_date = models.CharField(max_length=20, blank=True, null=True)
    about = models.CharField(max_length=20, blank=True, null=True)
    dept = models.CharField(max_length=20, blank=True, null=True)
    purpose = models.CharField(max_length=20, blank=True, null=True)
    team_lead = models.CharField(max_length=20, blank=True, null=True)
    team_member = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.PositiveIntegerField(choices=STATUS, default='1', blank=True)


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
    coor_comm = models.CharField(max_length=25, blank=True, null=True)
    date_created = models.DateField(default=date.today, blank=True, null=True)
    comment = models.TextField()
  
   


    def __str__(self):
        return self.first_name






# models.py




