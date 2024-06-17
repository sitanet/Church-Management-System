from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields.related import ForeignKey, OneToOneField




# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, role, phone_number,  password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            role=role,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=User.ADMIN,  # Provide a role value here
            phone_number='N/A',  # Provide a phone_number value here
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user





class User(AbstractBaseUser):
    ADMIN = 1
    TEAM_LEAD = 2
    TEAM_MEMBER = 3
    PASTORATE = 4
    FACILITATOR = 5
    STUDENT = 6
    CARRER = 7
    BUSINESS = 8
    SERVICE_TEAM = 9
  

    MALE = 1
    FEMALE = 2

    ROLE_CHOICE = (
        (ADMIN, 'Admin'),
        (TEAM_LEAD, 'Team Lead'),
        (TEAM_MEMBER, 'Team Member'),
        (PASTORATE, 'Pastorate'),
        (FACILITATOR, 'Facilitator'),
        (STUDENT, 'Student'),
        (CARRER, 'Career'),
        (BUSINESS, 'Business'),
        (SERVICE_TEAM, 'Service Team'),
     
    )

    profile_picture = models.ImageField(upload_to='users/profile_pictures', default='images/avatar.jpg')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=30, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_role(self):
        if self.role == 1:
            user_role = 'Admin'
        elif self.role == 2:
            user_role = 'Team Lead'
        elif self.role == 3:
            user_role = 'Team Member'
        elif self.role == 4:
            user_role = 'Pastorate'
        if self.role == 5:
            user_role = 'KBN Facilitator'
        elif self.role == 6:
            user_role = 'KBN Student'
        elif self.role == 7:
            user_role = 'KBN Career'
        elif self.role == 8:
            user_role = 'KBN Business'
        elif self.role == 9:
            user_role = 'Service Team'

        return user_role




class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    # profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    
    
    address = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
   
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # def full_address(self):
    #     return f'{self.address_line_1}, {self.address_line_2}'

    def __str__(self):
        return self.user.email

