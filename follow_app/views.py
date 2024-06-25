from email.message import EmailMessage
import os
import socket
from sre_constants import BRANCH
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.forms import UserForm
from accounts.utils import send_verification_email

from accounts.views import check_role_admin, check_role_coordinator
from .models import NYSC, Children, Team_Lead, TeamMember
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

from django.conf import settings
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



from django.conf import settings
import socket
@login_required(login_url='login')
@user_passes_test(check_role_admin)





def register_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        
        # Check for network connection
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            is_network_connected = True
        except OSError:
            is_network_connected = False

        if is_network_connected:
            if form.is_valid():
                member = form.save(commit=False)
                
                member.user = request.user
                member.save()

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

                messages.success(request, 'Account has been registered successfully!')
                return redirect('success')
            else:
                messages.warning(request, form.errors)
                messages.warning(request, 'Please check the form fields and fill them before submission.')
                return redirect('register_member')
        else:
            # Network is not connected, show a red toast notification
            messages.error(request, 'Network not available. Please check your connection.')
            return redirect('register_member')
    else:
        form = MemberForm()
        team_lead = Team_Lead.objects.all()
        team_members = TeamMember.objects.all()
        member = User.objects.all()
        
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



def member_detail_universal(request, id):
    member = get_object_or_404(Member, id=id)
    return render(request, 'admin_staff/member_detail_universal.html', {'member': member})


@login_required(login_url='login')
@user_passes_test(check_role_admin) 

def display_kbn_business(request):
    member = Business.objects.all()
    return render(request, 'admin_staff/display_kbn_business.html', {'member': member})


@login_required(login_url='login')
@user_passes_test(check_role_admin) 

def display_kbn_car(request):
    member = Career.objects.all()
    return render(request, 'admin_staff/display_kbn_car.html', {'member': member})


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


@login_required(login_url='login')
@user_passes_test(check_role_admin)
def member_detail(request, id):
    member = get_object_or_404(Member, id=id)
    team_lead = Team_Lead.objects.all()  # Initialize outside of the 'else' block
    team_members = TeamMember.objects.all()  # Initialize outside of the 'else' block
    
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been Updated successfully!.')
            return redirect('display_all_member')
    else:
        form = MemberForm(instance=member)
        current_user = request.user
    return render(request, 'admin_staff/member_detail.html', {'form': form, 'member': member, 'team_lead': team_lead, 'team_members': team_members})











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






@login_required(login_url='login')
@user_passes_test(check_role_admin)
def admin_registration(request):
 
    return render(request, 'admin_staff/admin_registration.html')



from django.shortcuts import render, get_object_or_404, redirect
from .models import Member, Family
@login_required(login_url='login')
@user_passes_test(check_role_admin)
def list_family(request):
    family = Family.objects.all()
    return render(request, 'admin_staff/list_family.html', {'family': family})





def family_detail(request, id):
    family = get_object_or_404(Family, id=id)
    children = family.children.all()
    return render(request, 'admin_staff/family_detail.html', {'family': family, 'children': children})





def delete_family(request, id):
    family = get_object_or_404(Family, id=id)
    if request.method == 'POST':
        family.delete()
        return redirect('list_family')
    return render(request, 'admin_staff/delete_family.html', {'family': family})




@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def list_members(request):
    members = Member.objects.filter(marital_status=2)
    return render(request, 'coordinators/list_members.html', {'members': members})


@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def list_members_student(request):
    members = Member.objects.all()
    return render(request, 'coordinators/list_member_student.html', {'members': members})



def nysc_detail(request, id):
    nysc = get_object_or_404(NYSC, id=id)
    return render(request, 'admin_staff/nysc_detail.html', {'nysc': nysc})



@login_required(login_url='login')
@user_passes_test(check_role_admin)
def nysc(request):
    members = NYSC.objects.all()
    return render(request, 'admin_staff/nysc.html', {'members': members})


@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def list_members_nysc(request):
    members = Member.objects.all()
    return render(request, 'coordinators/list_member_nysc.html', {'members': members})








# def nysc_detail(request, pk):
#     nysc = get_object_or_404(NYSC, pk=pk)
#     return render(request, 'nysc_detail.html', {'nysc': nysc})





@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def list_members_car_kbn(request):
    members = Member.objects.all()
    return render(request, 'coordinators/list_members_car_kbn.html', {'members': members})






@login_required(login_url='login')
@user_passes_test(check_role_admin)
def list_members_bus_kbn(request):
    members = Member.objects.all()
    return render(request, 'coordinators/list_members_bus_kbn.html', {'members': members})



@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def list_members_child(request):
    members = Member.objects.filter(marital_status=4)
    return render(request, 'coordinators/list_members_child.html', {'members': members})



@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def kbn_bus_car(request):
    members = Member.objects.all()
    return render(request, 'coordinators/kbn_bus_car.html', {'members': members})






import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import FamilyForm, ChildForm
from .models import Member, Team_Lead, TeamMember, Family, Child



@login_required(login_url='login')
@user_passes_test(check_role_coordinator)
def create_family(request, member_id):
    member = get_object_or_404(Member, id=member_id)

    if request.method == 'POST':
        family_form = FamilyForm(request.POST)
        if family_form.is_valid():
            family = family_form.save(commit=False)
            family.husband = member
            family.team_lead = request.user.role
            family.team_member = request.POST.get('team_member')
            family.wife_id = request.POST['wife_id']
            family.save()

            children_data = json.loads(request.POST.get('children', '[]'))
            for child_data in children_data:
                child_form = ChildForm({
                    'name': child_data['name'],
                    'age': child_data['age'],
                })
                if child_form.is_valid():
                    child = child_form.save(commit=False)
                    child.family = family  # Set the family field
                    child.save()

            messages.success(request, 'Family created successfully')
            return redirect('success')  # Redirect to a relevant view
        else:
            messages.error(request, 'Error in form data')
    else:
        family_form = FamilyForm()

    team_leads = Team_Lead.objects.all()
    team_members = TeamMember.objects.all()

    return render(request, 'coordinators/create_family.html', {
        'family_form': family_form,
        'member': member,
        'team_leads': team_leads,
        'team_members': team_members,
    })






from django.http import HttpResponse
from .models import Member

def search_wife(request):
    query = request.GET.get('q', '')
    results = Member.objects.filter(first_name__icontains=query)
    response_html = ''
    for member in results:
        response_html += f'<div onclick="selectWife({member.id}, \'{member.first_name} {member.last_name}\')">{member.first_name} {member.last_name}</div>'
    return HttpResponse(response_html)



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Member, Student
from .forms import StudentForm

def create_student(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.member = member
            student.save()
            messages.success(request, 'Student profile created successfully!')
            return redirect('success')
        else:
            messages.error(request, 'There was an error creating the student profile.')
    else:
        form = StudentForm()
    
    context = {
        'member': member,
        'student_form': form,
    }
    return render(request, 'coordinators/create_student.html', context)


from django.shortcuts import render

def success_page(request):
    return render(request, 'coordinators/student_success.html')




# views.py

from django.shortcuts import render, redirect
from .forms import NYSCForm

# views.py



def create_nysc(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        form = NYSCForm(request.POST)
        if form.is_valid():
            nysc_instance = form.save(commit=False)
            nysc_instance.member = member
            nysc_instance.save()
            return redirect('success')
    else:
        form = NYSCForm()
    return render(request, 'coordinators/create_nysc.html', {'form': form, 'member': member})


def success(request):
    return render(request, 'coordinators/success.html')






# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChildrenForm
from .models import Member

def create_child(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        form = ChildrenForm(request.POST)
        if form.is_valid():
            child_instance = form.save(commit=False)
            child_instance.member = member
            child_instance.save()
            return redirect('success')
    else:
        form = ChildrenForm()
    return render(request, 'coordinators/child_form.html', {'form': form, 'member': member})

def child_success(request):
    return render(request, 'coordinators/child_success.html')













from django.shortcuts import render, redirect, get_object_or_404
from .models import Member, Business
from .forms import BusinessProfileForm

def create_business_profile(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    business, created = Business.objects.get_or_create(member=member)
    
    if request.method == 'POST':
        form = BusinessProfileForm(request.POST, instance=business)
        
        if form.is_valid():
            form.save()
            return redirect('success')  # Change this to your success URL
    
    else:
        form = BusinessProfileForm(instance=business)
    
    return render(request, 'coordinators/create_business_profile.html', {
        'member': member,
        'form': form,
    })




# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import CareerProfileForm, CurrentEmploymentFormSet, PreviousEmploymentFormSet, EducationalBackgroundFormSet, OtherQualificationFormSet
from .models import Member

def create_career_profile(request, member_id):
    member = get_object_or_404(Member, id=member_id)

    if request.method == 'POST':
        career_form = CareerProfileForm(request.POST, request.FILES)
        current_employment_formset = CurrentEmploymentFormSet(request.POST, request.FILES, prefix='current_employment')
        previous_employment_formset = PreviousEmploymentFormSet(request.POST, request.FILES, prefix='previous_employment')
        educational_background_formset = EducationalBackgroundFormSet(request.POST, request.FILES, prefix='educational_background')
        other_qualification_formset = OtherQualificationFormSet(request.POST, request.FILES, prefix='other_qualification')

        if career_form.is_valid() and current_employment_formset.is_valid() and previous_employment_formset.is_valid() and educational_background_formset.is_valid() and other_qualification_formset.is_valid():
            career = career_form.save(commit=False)
            career.member = member
            career.save()

            current_employment_formset.instance = career
            current_employment_formset.save()

            previous_employment_formset.instance = career
            previous_employment_formset.save()

            educational_background_formset.instance = career
            educational_background_formset.save()

            other_qualification_formset.instance = career
            other_qualification_formset.save()

            return redirect('kbn_success')  # Replace 'kbn_success' with the actual name of your success page

    else:
        career_form = CareerProfileForm()
        current_employment_formset = CurrentEmploymentFormSet(prefix='current_employment')
        previous_employment_formset = PreviousEmploymentFormSet(prefix='previous_employment')
        educational_background_formset = EducationalBackgroundFormSet(prefix='educational_background')
        other_qualification_formset = OtherQualificationFormSet(prefix='other_qualification')

    return render(request, 'coordinators/kbn_career_form.html', {
        'form': career_form,
        'current_employment_formset': current_employment_formset,
        'previous_employment_formset': previous_employment_formset,
        'educational_background_formset': educational_background_formset,
        'other_qualification_formset': other_qualification_formset,
        'member': member
    })


# views.py

def kbn_success(request):
    return render(request, 'coordinators/kbn_success.html')




from django.shortcuts import render, get_object_or_404
from .models import Career





def member_male(request):
    member_male = Member.objects.filter(gender=1)
    return render(request, 'admin_staff/member_male.html', {'member_male': member_male})


nysc_detail
def member_male_detail(request, id):
    member = get_object_or_404(Member, id=id, gender=1)
    return render(request, 'admin_staff/member_male_detail.html', {'member': member})


def member_female(request):
    member_female = Member.objects.filter(gender=2)
    return render(request, 'admin_staff/member_female.html', {'member_female': member_female})





def member_female_detail(request, id):
    member = get_object_or_404(Member, id=id, gender=2)
    return render(request, 'admin_staff/member_female_detail.html', {'member': member})

def family(request):
    member = Family.objects.all()
    return render(request, 'admin_staff/list_family.html', {'member': member})





def member_married(request):
    member_married = Member.objects.filter(marital_status=2)
    return render(request, 'admin_staff/member_married.html', {'member_married': member_married})




def member_single(request):
    member_single = Member.objects.filter(marital_status=1)
    return render(request, 'admin_staff/member_single.html', {'member_single': member_single})




def children(request):
    children = Children.objects.select_related('member').all()
    return render(request, 'admin_staff/children.html', {'children': children})




def children_detail(request, id):
    child = get_object_or_404(Children, id=id)
    return render(request, 'admin_staff/children_detail.html', {'child': child})






@login_required(login_url='login')
@user_passes_test(check_role_admin) 

def display_kbn_business_admin(request):
    member = Business.objects.all()
    return render(request, 'admin_staff/display_kbn_business.html', {'member': member})



@login_required(login_url='login')
@user_passes_test(check_role_admin) 

def display_kbn_car_admin(request):
    member = Career.objects.all()
    return render(request, 'admin_staff/display_kbn_car.html', {'member': member})





def career_list(request):
    careers = Career.objects.all()
    return render(request, 'coordinators/career_list.html', {'careers': careers})

def career_detail(request, pk):
    career = get_object_or_404(Career, pk=pk)
    return render(request, 'coordinators/career_detail.html', {'career': career})


def business_list(request):
    business = Business.objects.all()
    return render(request, 'coordinators/business_list.html', {'business': business})

def business_detail(request, pk):
    business = get_object_or_404(Business, pk=pk)
    return render(request, 'coordinators/business_detail.html', {'business': business})


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Career

def career_delete(request, pk):
    career = get_object_or_404(Career, pk=pk)
    career.delete()
    messages.success(request, 'Career deleted successfully.')
    return redirect('career_list')  # Replace 'career_list' with the name of your list view


def business_delete(request, pk):
    business = get_object_or_404(Business, pk=pk)
    business.delete()
    messages.success(request, 'Career deleted successfully.')
    return redirect('business_list')  # Replace 'career_list' with the name of your list view





from django.http import JsonResponse

from .forms import HouseholdForm

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Household, HouseholdMember, Member
from .forms import HouseholdMemberForm

def create_household(request):
    if request.method == 'POST':
        household_form = HouseholdForm(request.POST)
        if household_form.is_valid():
            household = household_form.save()
            members_data = request.POST.getlist('members')
            positions_data = request.POST.getlist('positions')
            for member_id, position in zip(members_data, positions_data):
                if member_id and position:
                    member = Member.objects.get(id=member_id)
                    HouseholdMember.objects.create(household=household, member=member, position=position)
            messages.success(request, 'Household created successfully.')
            return redirect('success')  # Replace with your actual redirect
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        household_form = HouseholdForm()

    return render(request, 'coordinators/create_household.html', {
        'household_form': household_form,
    })

def search_members(request):
    query = request.GET.get('q')
    members = Member.objects.filter(first_name__icontains=query) | Member.objects.filter(last_name__icontains=query) | Member.objects.filter(middle_name__icontains=query)
    results = [{'id': member.id, 'name': f"{member.first_name} {member.middle_name} {member.last_name}"} for member in members]
    return JsonResponse(results, safe=False)




def household_list(request):
    households = Household.objects.all()
    return render(request, 'admin_staff/household_list.html', {'households': households})



def household_detail(request, household_id):
    household = get_object_or_404(Household, pk=household_id)
    members = household.householdmember_set.all()
    return render(request, 'admin_staff/household_detail.html', {'household': household, 'members': members})

def edit_household_member(request, household_id, member_id):
    household_member = get_object_or_404(HouseholdMember, pk=member_id)
    
    if request.method == 'POST':
        form = HouseholdMemberForm(request.POST, instance=household_member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Household member updated successfully.')
            return redirect('household_detail', household_id=household_member.household.id)
    else:
        form = HouseholdMemberForm(instance=household_member)
    
    return render(request, 'admin_staff/edit_household_member.html', {'form': form, 'household_member': household_member})




def add_household_member(request, household_id):
    household = get_object_or_404(Household, pk=household_id)
    
    if request.method == 'POST':
        form = HouseholdMemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New member added successfully.')
            return redirect('household_detail', household_id=household.id)
    else:
        form = HouseholdMemberForm(initial={'household': household})
    
    return render(request, 'admin_staff/add_household_member.html', {'form': form, 'household': household})


def delete_household_member(request, household_id, member_id):
    household_member = get_object_or_404(HouseholdMember, pk=member_id)
    household_member.delete()
    messages.success(request, 'Household member deleted successfully.')
    return redirect('household_detail', household_id=household_id)



from django.http import JsonResponse
from django.db.models import Q
from .models import Member

def search_member_add(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        members = Member.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))[:10]
        results = []
        for member in members:
            member_json = {}
            member_json['id'] = member.id
            member_json['label'] = f"{member.first_name} {member.last_name}"
            member_json['value'] = f"{member.first_name} {member.last_name}"
            results.append(member_json)
        return JsonResponse(results, safe=False)









from django.shortcuts import render, redirect, get_object_or_404
from .models import Teenager, Member
from .forms import TeenagerForm

def teenager_member_list(request):
    members = Member.objects.filter(marital_status=3)
    return render(request, 'coordinators/teenager_member_list.html', {'members': members})

def add_teenager(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = TeenagerForm(request.POST)
        if form.is_valid():
            teenager = form.save(commit=False)
            teenager.member = member
            teenager.save()
            return redirect('teenager_list')
    else:
        form = TeenagerForm()
    return render(request, 'coordinators/add_teenager.html', {'form': form, 'member': member})

def edit_teenager(request, teenager_id):
    teenager = get_object_or_404(Teenager, pk=teenager_id)
    if request.method == 'POST':
        form = TeenagerForm(request.POST, instance=teenager)
        if form.is_valid():
            form.save()
            return redirect('teenager_list')
    else:
        form = TeenagerForm(instance=teenager)
    return render(request, 'coordinators/edit_teenager.html', {'form': form, 'teenager': teenager})

def delete_teenager(request, teenager_id):
    teenager = get_object_or_404(Teenager, pk=teenager_id)
    if request.method == 'POST':
        teenager.delete()
        return redirect('teenager_list')
    return render(request, 'coordinators/delete_teenager.html', {'teenager': teenager})

def teenager_list(request):
    teenagers = Teenager.objects.all()
    return render(request, 'coordinators/teenager_list.html', {'teenagers': teenagers})

def admin_teenager_list(request):
    teenagers = Teenager.objects.all()
    return render(request, 'admin_staff/admin_teenager_list.html', {'teenagers': teenagers})



def teenager_detail(request, teenager_id):
    teenager = get_object_or_404(Teenager, id=teenager_id)
    return render(request, 'admin_staff/teenager_detail.html', {'teenager': teenager})
