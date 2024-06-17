from tokenize import Comment
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.models import User

from accounts.views import check_role_admin, check_role_coordinator
from follow_app.forms import CommentForm, MemberForm
from django.contrib import messages

from follow_app.models import Team_Lead, Member, TeamMember
from follow_app.models import Comment
from django.template.loader import render_to_string
from django.core.mail import send_mail


# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from twilio.rest import Client
from follow_app.forms import MemberForm
from follow_app.models import Team_Lead, TeamMember, User
from django.conf import settings
from .utils import send_sms

@user_passes_test(check_role_coordinator)


# views.py



  # Import the send_sms function


# views.py



def coor_register_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            recipient_email = request.POST.get('email')
            recipient_name = request.POST.get('first_name')
            phone_number = request.POST.get('phone_no')
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
                'The CityGate Church Follow Up Unit',
                [recipient_email],
                fail_silently=False,
                html_message=html_message,
            )

            # Send SMS via Termii
            try:
                sms_body = f"Hello {recipient_name}, welcome to The CityGate Church! We're thrilled to have you with us. Stay Blessed."
                response = send_sms(phone_number, sms_body)
                print(f'SMS sent: {response}')
            except Exception as e:
                error_message = f'Failed to send SMS: {e}'
                messages.error(request, error_message)
                print(error_message)

            messages.success(request, 'Account has been registered successfully!.')
            return redirect('coor_display_all_member')
        else:
            messages.warning(request, form.errors)
            messages.warning(request, 'Please check the form fields and fill them before submission!.')
            return redirect('coor_register_member')
    else:
        form = MemberForm()
        current_user = request.user
        team_lead = Team_Lead.objects.filter(name=current_user)
        team_members = TeamMember.objects.all()
        member = User.objects.all()

        context = {
            'form': form,
            'team_lead': team_lead,
            'team_members': team_members,
            'member': member,
        }

    return render(request, 'coordinators/coor_register_member.html', context)





@user_passes_test(check_role_coordinator)
def coor_member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    team_lead = None  # Initialize variables outside the 'else' block
    team_members = None
    
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been Updated successfully!.')
            return redirect('coor_display_all_member')
    else:
        form = MemberForm(instance=member)
        current_user = request.user
        team_lead = Team_Lead.objects.filter(name=current_user)
        team_members = TeamMember.objects.all()
    
    return render(request, 'coordinators/coor_member_detail.html', {'form': form, 'member': member, 'team_lead': team_lead, 'team_members': team_members})



@user_passes_test(check_role_coordinator)
def coor_display_comment(request):
    current_user = request.user
    comment = Comment.objects.filter(coor_comm=current_user)
    mem_com = Member.objects.all()
    context = {
         'comment':comment,
         'mem_com':mem_com,
         
     } 
    return render(request, 'coordinators/coor_display_comment.html', context)

@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def coor_display_all_member(request):
    current_user = request.user
    member = Member.objects.filter(user=current_user).filter(status='1')
    # member = Member.objects.filter(team_lead=current_user).filter(status='1')

    return render(request, 'coordinators/coor_display_all_member.html', {'member': member})

# @login_required(login_url='login')
# def coor_display_comment(request):
#     return render(request, 'coordinators/display_comment.html')


@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def coor_new_comment(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.member = member
            comment.team_sup = request.user
            # comment.phone_number = UserProfile.phone_number
            comment.save()
            return redirect('coor_display_comment')
   
    else:
        form = CommentForm()
    context = {
         'member':member,
         'form':form,   
     }
    return render(request, 'coordinators/coor_new_comment.html', context)




@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def my_team_member_list(request):
    current_user = request.user
    member = Member.objects.filter(team_lead=current_user)
    context = {
         'member':member,
     } 
    return render(request, 'coordinators/my_team_member_list.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def my_team_member_comment(request):
    current_user = request.user
    member = Comment.objects.filter(coor_comm=current_user)
    context = {
         'member':member,
     } 
    return render(request, 'coordinators/my_team_member_comment.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_coordinator)

def registration(request):
 
    return render(request, 'coordinators/registration.html')