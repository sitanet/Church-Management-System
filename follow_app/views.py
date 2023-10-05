from email.message import EmailMessage
import os
import socket
from sre_constants import BRANCH
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.utils import send_verification_email

from accounts.views import check_role_admin, check_role_coordinator
from .models import Team_Lead, TeamMember
# from accounts.context_processors import get_staff
from .forms import Team_LeadForm, MemberForm, CommentForm
from .models import Member, Comment
from django.shortcuts import render, get_object_or_404
# from .utils import custom_id
from accounts.models import User, UserProfile
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.shortcuts import render
from django.utils import timezone
from follow_app.models import Member
# from .tasks import send_birthday_wish_email

# Create your views here.

# def dashboard(request):
#     member = Member.objects.count()
#     return render(request, 'admin_staff/dashboard.html', {'member': member})

# @user_passes_test(check_role_admin)
# @login_required(login_url='login')
# def register_member(request):
#     return render(request, 'admin_staff/register_member.html')

def network_not_available(request):
    
    return render(request, 'admin_staff/network_not_available.html')


@login_required(login_url='login')
@user_passes_test(check_role_admin)
def profile(request):
    profile = UserProfile.objects.all()
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required(login_url='login')
@user_passes_test(check_role_admin)
def register_member(request):
    
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        
        try:

            socket.create_connection(("8.8.8.8", 53), timeout=3)
            is_network_connected = True
        except OSError:
            is_network_connected = False

        if is_network_connected:
       
            if form.is_valid():
                
            
                form = form.save(commit=False)
                
                form.user = request.user
                
                form.save()

            # Send email with template
                recipient_email = request.POST.get('email')
                recipient_name = request.POST.get('first_name')
                subject = 'Thank you for Coming'
                
                # Render the HTML email template
                html_message = render_to_string(
                    'accounts/email/welcome_email.html',
                    {
                        'recipient_name': recipient_name,
                    
                    }
                )

            # Send the email
                send_mail(
                    subject,
                    '',
                    'The CityGate Church Followup Unit',
                    [recipient_email],
                    fail_silently=False,
                    html_message=html_message,
                )

            
                messages.success(request, 'Account has been registered successfully!.')
                return redirect('display_all_member')
            else:
                    messages.warning(request, form.errors)
                    messages.warning(request, 'Please Check the form filed and fill them before submission!.')
                    return redirect('register_member')
                    # print('invalid form')
                
        else:
            # Network is not connected, handle accordingly (e.g., raise an exception or log)
            return redirect('network_not_available')
                
            
            
        
            
        
                
    else:
        
            form = MemberForm()
            team_lead = Team_Lead.objects.all()
            team_members = TeamMember.objects.all()
            member = User.objects.all()
        

            
            # cust_coa = Coa.objects.raw("select * from chart_of_accounts_coa where right(gl_no,3) = '200'")
            
            
            context = {
                'form': form,
                'team_lead': team_lead,
                'team_members': team_members,
                'member': member,
            
                
            }
       
    

    return render(request, 'admin_staff/register_member.html', context)

@login_required(login_url='login')
@user_passes_test(check_role_admin)
def display_all_member(request):
    member = Member.objects.all()
    return render(request, 'admin_staff/display_all_member.html', {'member': member})

    




@login_required(login_url='login')
@user_passes_test(check_role_admin)

def display_comment(request):
    current_user = request.user
    comment = Comment.objects.filter(team_sup=current_user)
    mem_com = Member.objects.all()
    context = {
         'comment':comment,
         'mem_com':mem_com,
         
     } 
    return render(request, 'admin_staff/display_comment.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_admin)
def all_comment(request):
    # current_user = request.user
    comment = Comment.objects.all()
    mem_com = Member.objects.all()
    context = {
         'comment':comment,
         'mem_com':mem_com,
         
     } 
    return render(request, 'admin_staff/all_comment.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_admin)

def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect('display_all_member')

@login_required(login_url='login')
@user_passes_test(check_role_admin)

# def member_detail(request, id):
#     member = get_object_or_404(Member, id=id)
    
#     if request.method == 'POST':
#         form = MemberForm(request.POST, request.FILES, instance=member)
#         if form.is_valid():
#             form.save()
#             return redirect('display_all_member')
#     else:
#         form = MemberForm(instance=member)
#         coordinators = Team_Lead.objects.all()
#         team_members = TeamMember.objects.all()
#     return render(request, 'admin_staff/member_detail.html', {'form': form, 'member': member, 'coordinators': coordinators, 'team_members': team_members,})

@login_required(login_url='login')
@user_passes_test(check_role_admin)
def member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been Updated successfully!.')
            return redirect('display_all_member')
    else:
        form = MemberForm(instance=member)
        current_user = request.user
        team_lead = Team_Lead.objects.all()
        team_members = TeamMember.objects.all()
    return render(request, 'admin_staff/member_detail.html', {'form': form, 'member': member, 'team_lead': team_lead, 'team_members': team_members,})


# def member_detail(request, id):
#     member = get_object_or_404(Member, id=id)
#     if request.method == 'POST':
#         form = MemberForm(request.POST, request.FILES)
#         if form.is_valid():
#             if len(request.FILES) != 0:
#                 if len(member.image) > 0:
#                     os.remove(member.image.path)
#                 member.image = request.FILES['image']
#             member.first_name = request.POST.get('first_name')
#             member.middle_name = request.POST.get('middle_name')
#             member.last_name = request.POST.get('last_name')
#             member.date_of_birth = request.POST.get('date_of_birth')
#             member.email = request.POST.get('email')
#             member.phone_no = request.POST.get('phone_no')
#             member.gender = request.POST.get('gender')
#             member.marital_status = request.POST.get('marital_status')
#             member.occupation = request.POST.get('occupation')
#             member.address = request.POST.get('address')
#             member.nationality = request.POST.get('nationality')
#             member.kcc_center = request.POST.get('kcc_center')
#             member.wedding_ann = request.POST.get('wedding_ann')
#             member.join = request.POST.get('join')
#             member.reg_date = request.POST.get('reg_date')
#             member.about = request.POST.get('about')
#             member.dept = request.POST.get('dept')
#             member.purpose = request.POST.get('purpose')
#             member.coordinator = request.POST.get('coordinator')
#             member.team_member = request.POST.get('team_member')
#             member.save()
#             messages.success(request, 'Account has been updated successfully!.')
#             return redirect('display_all_member')
#     else:
#         form = MemberForm()
#         coordinators = Coordinator.objects.all()
#         team_members = TeamMember.objects.all()
        

#     context = {
#                     'form':form,
#                     'member':member,
#                     # 'coordinators':coordinators,
#                     # 'team_members':team_members,
                    
#                    }   

#     return render(request, 'admin_staff/member_detail.html', context)







def add_coordinator(request):
 
    return render(request, 'admin_staff/add_coordinator.html')




    
    
@login_required(login_url='login')
@user_passes_test(check_role_admin)
def new_comment(request, id):
    member = get_object_or_404(Member, id=id)
    coordinator = Member.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.member = member
            comment.coor_comm = coordinator
            comment.team_sup = request.user
            # comment.phone_number = UserProfile.phone_number
            comment.save()
            return redirect('display_comment')
   
    else:
        form = CommentForm()
    context = {
         'member':member,
         'form':form,   
     }
    return render(request, 'admin_staff/new_comment.html', context)


# @login_required(login_url='login')
# @user_passes_test(check_role_admin)
# def add_coordinator(request, id):
#     member = get_object_or_404(Member, id=id)
#     coordinator = Member.objects.get(id=id)
#     if request.method == 'POST':
#         form = Team_LeadForm(request.POST)
#         if form.is_valid():
#             coordinator = form.save(commit=False)
            
#             coordinator.save()
#             return redirect('add_coordinator')
   
#     else:
#         form = Team_LeadForm()
#     context = {
#          'member':member,
#          'form':form,   
#      }
#     return render(request, 'admin_staff/add_coordinator.html', context)




def add_coordinator(request):
    if request.method == 'POST':
        form = Team_LeadForm(request.POST, request.FILES)
        
        if form.is_valid():

        # Save the Coordinator to the database
          
             form.save()
             messages.success(request, 'Account has been registered successfully!.')
             return redirect('add_coordinator')
        else:
            messages.warning(request, form.errors)
            messages.warning(request, 'Please Check the form filed and fill them before submission!.')
            return redirect('add_coordinator')
            # print('invalid form')
            
    else:
       
        form = MemberForm()
        team_lead = User.objects.filter(role='2')
        
        context = {
             'form': form,
             'team_lead': team_lead,
            
        }

    return render(request, "admin_staff/add_coordinator.html", context)




# def count_data(request):
#     member_count = Member.objects.count()
#     return render(request, 'admin_staff/dashboard.html', {'member_count': member_count})


# def send_birthday_wishes(request):
#     today = timezone.now().date()
#     customers_with_birthday = Member.objects.filter(date_of_birth=today)

#     for customer in customers_with_birthday:
#         send_birthday_wish_email.delay(customer.email, customer.first_name)

#     return render(request, 'admin_staff/birthday_sent.html')