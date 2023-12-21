from django.contrib.auth.models import Permission,User
from django.contrib.auth.decorators import permission_required,login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import random
from .models import Research_scientist_Data,Contact,Research_scientist,Machine_learning_engineer,Software_application_developer,Machine_learning_engineer_data,Data_scientist_data,Software_application_developer_data
from django.core.mail import send_mail, get_connection,EmailMessage
from django.conf import settings
import secrets
from .forms import ContactForm,Research_scientist_form,Machine_learning_engineer_form,Software_application_developer_form,PermissionAssignmentForm
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,get_object_or_404,redirect
from .forms import CandidateForm,Software_application_developer_form
from .models import Candidate,DestinationModel,Interview,RejectionModel,Score_technical,Score_coding,InterviewDateCoding,InterviewDateTechnical,SaveScoreDataScientistTechnical
from django.contrib import messages  
from django.http import JsonResponse,HttpResponse
from django.views.decorators.cache import never_cache,cache_control
from datetime import  timedelta
from ipware import get_client_ip
from datetime import datetime

email_connection = get_connection(
        backend=settings.SECOND_EMAIL_BACKEND,
        host=settings.SECOND_EMAIL_HOST,
        port=settings.SECOND_EMAIL_PORT,
        username=settings.SECOND_EMAIL_HOST_USER,
        password=settings.SECOND_EMAIL_HOST_PASSWORD,
        use_tls=settings.SECOND_EMAIL_USE_TLS,
        use_ssl=settings.SECOND_EMAIL_USE_SSL,
    )

def Selected_candidates(request):
    return render(request,'recuriements/selected_candidate.html')



def assign_permission(request):
    if request.method == 'POST':
        form = PermissionAssignmentForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            permission = form.cleaned_data['permission']
            user.user_permissions.add(permission)
            return render(request, 'success.html')
    else:
        form = PermissionAssignmentForm()
    return render(request, 'assign_permission.html', {'form': form})

def index(request):
    return render(request,'index.html')

def career(request):
    return render(request,'recuriements/candidate_insert_data.html')

count=3

def send_invitation_technical(request, candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    candidate = get_object_or_404(Interview,id1=candidate_id)

    send_mail(

        'Interview Invitation',

        f'Please choose your Technical interview dates by clicking on the following link: http://admin.simplisolve.us/select-interview-dates/?candidate_id={candidate_id}',

        'recruitment@simplisolve.us',

        [candidate.email],

        fail_silently=False,
        connection=email_connection

    )

    return render(request,'recuriements/invitation_sent.html')
from django.shortcuts import render, redirect
from .models import Interview, Question, Marks

from django.http import HttpResponse
from django.contrib import messages
import tkinter as tk
from tkinter import messagebox
def show_technical_score(request,candidate_id):
    scores = SaveScoreDataScientistTechnical.objects.filter(id1=candidate_id)
    candidate=get_object_or_404(Interview,id1=candidate_id)

    # Pass the fetched data to the template
    return render(request, 'recuriements/show_scores.html', {'scores': scores,'candidate':candidate})
def update_marks(request):
    if request.method == 'POST':
        score_topic= request.POST.get('score_topic')
        score_id= request.POST.get('score_id')
        marks1 = request.POST.get('marks1')
        marks2 = request.POST.get('marks2')
        marks3 = request.POST.get('marks3')
        marks4 = request.POST.get('marks4')

        try:
            score = SaveScoreDataScientistTechnical.objects.get(topic=score_topic)
            score.marks1 = marks1
            score.marks2 = marks2
            score.marks3 = marks3
            score.marks4 = marks4
            score.save()

            messages.success(request, 'Score updated successfully.')
            scores = SaveScoreDataScientistTechnical.objects.filter(id1=score_id)
            candidate=get_object_or_404(Interview,id1=score_id)
            return render(request, 'recuriements/show_scores.html', {'scores': scores,'candidate':candidate,'messages': messages.get_messages(request)})
        except SaveScoreDataScientistTechnical.DoesNotExist:
            messages.error(request, 'Score not found')



def Save_score_data_scientist_technical(request,candidate_id):
    existing_topics = SaveScoreDataScientistTechnical.objects.filter(id1=candidate_id).values_list('topic', flat=True)
    if request.method == 'POST':
        candidate=get_object_or_404(Interview,id1=candidate_id)
        selected_topic = request.POST.get('selectedTopic')
        questions={}
        for key, value in request.POST.items():
            if key.startswith('Ques'):
                questions[key]=value
        # Extract questions and marks from the dictionary
        question_keys = list(questions.keys())
        mark_values = list(questions.values())
        print(candidate.id1)
        cand_id=candidate.id1
        interview_instance = SaveScoreDataScientistTechnical(
            id1=cand_id,
            topic=selected_topic,
            question1=question_keys[0] if len(question_keys) > 0 else '',
            marks1=int(mark_values[0]) if len(mark_values) > 0 else None,
            question2=question_keys[1] if len(question_keys) > 1 else '',
            marks2=int(mark_values[1]) if len(mark_values) > 1 else None,
            question3=question_keys[2] if len(question_keys) > 2 else '',
            marks3=int(mark_values[2]) if len(mark_values) > 2 else None,
            question4=question_keys[3] if len(question_keys) > 3 else '',
            marks4=int(mark_values[3]) if len(mark_values) > 3 else None,
        )
        interview_instance.save()
        messages.success(request,f"Score Saved for Topic : {selected_topic}")
        return render(request,'recuriements/Data_scientist_technical_interview.html',{'candidate':candidate,'existing_topics': existing_topics})

                        
        
                
        
       
       


def send_invitation_coding(request, candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    candidate = get_object_or_404(Interview,id1=candidate_id)

    send_mail(

        'Interview Invitation',

        f'Please choose your Coding interview dates by clicking on the following link: http://admin.simplisolve.us/select-interview-dates1/?candidate_id={candidate_id}',

        'recruitment@simplisolve.us',

        [candidate.email],

        fail_silently=False,
        connection=email_connection

    )

    return render(request,'recuriements/invitation_sent.html')
id_date=''
id_date1=''
def select_interview_dates_technical(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    candidate_id = request.GET.get('candidate_id')

    if request.method == 'POST':

        selected_date_1 = request.POST.get('selected_date_1')

        selected_date_2 = request.POST.get('selected_date_2')

        selected_date_3 = request.POST.get('selected_date_3')

        selected_date_1= datetime.strptime(selected_date_1, '%Y-%m-%dT%H:%M')

        selected_date_2= datetime.strptime(selected_date_2, '%Y-%m-%dT%H:%M')

        selected_date_3= datetime.strptime(selected_date_3, '%Y-%m-%dT%H:%M')

        # Update the interview dates for the candidate

        interview_dates=InterviewDateTechnical(

            id1=candidate_id,

        selected_date_1 = selected_date_1,

        selected_date_2 = selected_date_2,

        selected_date_3 = selected_date_3,

        )

        interview_dates.save()

        return render(request,'recuriements/date_selection_confirmation_technical.html', {'selected_date_1': selected_date_1,

            'selected_date_2': selected_date_2,

            'selected_date_3': selected_date_3,})

    return render(request, 'recuriements/select_interview_dates_technical.html',{'candidate_id':candidate_id})
def select_interview_dates_coding(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    candidate_id = request.GET.get('candidate_id')

    if request.method == 'POST':

        selected_date_1 = request.POST.get('selected_date_1')

        selected_date_2 = request.POST.get('selected_date_2')

        selected_date_3 = request.POST.get('selected_date_3')

        selected_date_1= datetime.strptime(selected_date_1, '%Y-%m-%dT%H:%M')

        selected_date_2= datetime.strptime(selected_date_2, '%Y-%m-%dT%H:%M')

        selected_date_3= datetime.strptime(selected_date_3, '%Y-%m-%dT%H:%M')

        # Update the interview dates for the candidate

        interview_dates=InterviewDateCoding(

            id1=candidate_id,

        selected_date_1 = selected_date_1,

        selected_date_2 = selected_date_2,

        selected_date_3 = selected_date_3,

        )

        interview_dates.save()

        return render(request,'recuriements/date_selection_confirmation_coding.html', {'selected_date_1': selected_date_1,

            'selected_date_2': selected_date_2,

            'selected_date_3': selected_date_3,})

    return render(request, 'recuriements/select_interview_dates_coding.html',{'candidate_id':candidate_id})
def submit_interview(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    if request.method == 'POST':

        # Retrieve candidate and interview data

         # Adjust this to match your form

        topic = request.POST.get('topic')  # Adjust this to match your form

        selected_questions = request.POST.getlist('questions') 

         # Adjust this to match your form

        selected_marks = request.POST.getlist('marks')  # Adjust this to match your form

        candidate=get_object_or_404(Interview,id1=candidate_id)

        a=[]

        for i in selected_questions:

            a.append(i)

        b=str(a)

        interview = Technical(

            id1=candidate.first_name,

            topic=topic,

            questions=b,

            marks=selected_marks,

        )

        interview.save()

        return render(request,'recuriements/question_list.html',{'candidate_id':candidate_id}) # Replace with the actual URL

    return render(request, 'recuriements/question_list.html',{'candidate_id':candidate_id})
def add_topic(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    if request.method == 'POST':

        topic_form = TopicForm(request.POST)

        if topic_form.is_valid():


            return redirect('add_question')

    else:

        topic_form = TopicForm()

    

    topics = Topic.objects.all()

    

    return render(request, 'recuriements/add_topic.html', {'topic_form': topic_form, 'topics': topics})
def get_questions(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    topic_id = request.GET.get('topic_id')

    if topic_id:

        questions = Question.objects.filter(topic_id=topic_id)

        questions_data = [{'text': question.text, 'marks': question.marks} for question in questions]

        return JsonResponse(questions_data, safe=False)

    else:

        return JsonResponse([], safe=False)
def add_question(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    if request.method == 'POST':

        question_form = QuestionForm(request.POST)

        if question_form.is_valid():

            question_form.save()

    topics = Topic.objects.all()

    questions = Question.objects.all()

    question_form = QuestionForm()

    selected_topic_id = request.GET.get('topic_id')  # Get the selected topic ID from the query parameter

    selected_topic = None

    if selected_topic_id:

        selected_topic = Topic.objects.get(pk=selected_topic_id)

        questions = questions.filter(topic=selected_topic)

    return render(request, 'recuriements/add_question.html', {

        'question_form': question_form,

        'topics': topics,

        'questions': questions,

        'selected_topic': selected_topic,

    })
def confirm_otp_data_scientist(request, candidate_id):
    global count
    error_message = None  
    candidate = get_object_or_404(Candidate, id=candidate_id)
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if candidate.otp == int(float((entered_otp))):
            # OTP matched, proceed with application submission
            candidate.submitted = True
            candidate.save()
            candidate_id = candidate.id
            candidate_name = f"{candidate.first_name} {candidate.last_name}"
            candidate_phone_number=f"{candidate.phone_number}"
            subject = 'New Data scientist Application Submission'
            message = f'candidate_id:{candidate_id}\nName: {candidate_name}\nPhone: {candidate_phone_number}\nEmail: {candidate.email}\nDate and Time: {candidate.datetime}\nsalary_exceptation:-{candidate.salary_exceptation}\nexperience_fields:-{candidate.experience_fields}\ndata_visualization_experience:-{candidate.data_visualization_experience}\nvisa_sponsorship:{candidate.visa_sponsorship}\npredictive_model_experience:{candidate.predictive_model_experience}\nresume: {candidate.resume.name}'
            from_email = 'recruitment@simplisolve.us'  # Use a valid email address
            recipient_list = ["recruitment@simplisolve.us",candidate.email]  # Replace with actual recipient email addresses
            email1 = EmailMessage(subject, message, from_email, recipient_list,connection=email_connection)
            email1.attach(candidate.resume.name, candidate.resume.file.read())
            email1.send(fail_silently=False)
            request.session['new_data_added'] = True
            Data_scientists = Data_scientist_data(
                id1=candidate.id,
                first_name=candidate.first_name,
                last_name=candidate.last_name,
                email=candidate.email,
                phone_number=candidate.phone_number,
                resume=candidate.resume.name,
                datetime=candidate.datetime,
                code=candidate.code,
                salary_exceptation=candidate.salary_exceptation,
                experience_fields=candidate.experience_fields,
                predictive_model_experience=candidate.predictive_model_experience,
                data_visualization_experience=candidate.data_visualization_experience,
                visa_sponsorship=candidate.visa_sponsorship,
                )
            Data_scientists.save()

            # messages.success(request, 'recuriements/Application submitted successfully.')

            return render(request, 'recuriements/success.html')

        else:

            count=count-1

            error_message = 'Invalid OTP. Please try again.'

            if count==0:

                count=3

                return render(request,'recuriements/max_otp.html')

            return render(request, 'recuriements/otp_confirmation.html', {'candidate_id': candidate_id,'error_message': error_message})
def confirm_otp_machine_learning(request, candidate_id):
    global count
    error_message = None  
    candidate = get_object_or_404(Machine_learning_engineer, id=candidate_id)
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if candidate.otp == int(float((entered_otp))):
            # OTP matched, proceed with application submission
            candidate.submitted = True
            candidate.save()
            candidate_id = candidate.id
            candidate_name = f"{candidate.first_name} {candidate.last_name}"
            candidate_phone_number=f"{candidate.phone_number}"
            subject = 'New Machine learning engineer Application Submission'
            message = f'candidate_id:{candidate_id}\nName: {candidate_name}\nPhone: {candidate_phone_number}\nEmail: {candidate.email}\nDate and Time: {candidate.datetime}\nsalary_exceptation:-{candidate.salary_exceptation}\nexperience_generative_models:{candidate.experience_generative_models}\nexperience_ml_pipelines:{candidate.experience_ml_pipelines}\npreferred_work_location:{candidate.preferred_work_location}'
            from_email = 'recruitment@simplisolve.us'  # Use a valid email address
            recipient_list = ["recruitment@simplisolve.us",candidate.email]  # Replace with actual recipient email addresses
            email1 = EmailMessage(subject, message, from_email, recipient_list,connection=email_connection)
            email1.attach(candidate.resume.name, candidate.resume.file.read())
            email1.send(fail_silently=False)
            request.session['new_data_added'] = True
            Machine_learning_engineers = Machine_learning_engineer_data(
                id1=candidate.id,
                first_name=candidate.first_name,
                last_name=candidate.last_name,
                email=candidate.email,
                phone_number=candidate.phone_number,
                resume=candidate.resume.name,
                datetime=candidate.datetime,
                code=candidate.code,
                salary_exceptation=candidate.salary_exceptation,
                experience_generative_models=candidate.experience_generative_models,
                experience_ml_pipelines=candidate.experience_ml_pipelines,
                preferred_work_location=candidate.preferred_work_location)
            Machine_learning_engineers.save()

            messages.success(request, 'recuriements/Application submitted successfully.')

            return render(request, 'recuriements/success.html')

        else:

            count=count-1

            error_message = 'Invalid OTP. Please try again.'

            if count==0:

                count=3

                return render(request,'recuriements/max_otp.html')

            return render(request, 'recuriements/otp_confirmation_machine_learning.html', {'candidate_id': candidate_id,'error_message': error_message})
def confirm_otp_software_developer(request, candidate_id):
    global count
    error_message = None  
    candidate = get_object_or_404(Software_application_developer, id=candidate_id)
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if candidate.otp == int(float((entered_otp))):
            # OTP matched, proceed with application submission
            candidate.submitted = True
            candidate.save()
            candidate_id = candidate.id
            candidate_name = f"{candidate.first_name} {candidate.last_name}"
            candidate_phone_number=f"{candidate.phone_number}"
            subject = 'New software developer  Application Submission'
            message = f'candidate_id:{candidate_id}\nName: {candidate_name}\nPhone: {candidate_phone_number}\nEmail: {candidate.email}\nDate and Time: {candidate.datetime}\nsalary_exceptation:-{candidate.salary_exceptation}\nproject_link:{candidate.project_link}\nsoftware_dev_experience:{candidate.software_dev_experience}\nexperience_with_sql:{candidate.experience_with_sql}\nus_citizen_or_permanent_resident:{candidate.us_citizen_or_permanent_resident}'
            from_email = 'recruitment@simplisolve.us'  # Use a valid email address
            recipient_list = ["recruitment@simplisolve.us",candidate.email]  # Replace with actual recipient email addresses
            email1 = EmailMessage(subject, message, from_email, recipient_list,connection=email_connection)
            email1.attach(candidate.resume.name, candidate.resume.file.read())
            email1.send(fail_silently=False)
            request.session['new_data_added'] = True
            Software_application_developers = Software_application_developer_data(
                id1=candidate.id,
                first_name=candidate.first_name,
                last_name=candidate.last_name,
                email=candidate.email,
                phone_number=candidate.phone_number,
                resume=candidate.resume.name,
                datetime=candidate.datetime,
                code=candidate.code,
                salary_exceptation=candidate.salary_exceptation,
                project_link=candidate.project_link,
                software_dev_experience=candidate.software_dev_experience,
                experience_with_sql=candidate.experience_with_sql,
                us_citizen_or_permanent_resident=candidate.us_citizen_or_permanent_resident
                
                )
            Software_application_developers.save()

            messages.success(request, 'recuriements/Application submitted successfully.')

            return render(request, 'recuriements/success.html')

        else:

            count=count-1

            error_message = 'Invalid OTP. Please try again.'

            if count==0:

                count=3

                return render(request,'recuriements/max_otp.html')

            return render(request, 'recuriements/otp_confirmation_software_developer.html', {'candidate_id': candidate_id,'error_message': error_message})
def confirm_otp_research_scientist(request, candidate_id):
    global count
    error_message = None  
    candidate = get_object_or_404(Research_scientist, id=candidate_id)
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if candidate.otp == int(float((entered_otp))):
            # OTP matched, proceed with application submission
            candidate.submitted = True
            candidate.save()
            candidate_id = candidate.id
            candidate_name = f"{candidate.first_name} {candidate.last_name}"
            candidate_phone_number=f"{candidate.phone_number}"
            subject = 'New Research scientist Application Submission'
            message = f'candidate_id:{candidate_id}\nName: {candidate_name}\nPhone: {candidate_phone_number}\nEmail: {candidate.email}\nDate and Time: {candidate.datetime}\nsalary_exceptation:-{candidate.salary_exceptation}\nlike_working_in_team:{candidate.like_working_in_team}\nexperience_with_ml_framework:-{candidate.experience_with_ml_framework}\nresearch_publications:-{candidate.research_publications}\nexperience_as_research_scientist:{candidate.experience_as_research_scientist}'
            from_email = 'recruitment@simplisolve.us'  # Use a valid email address
            recipient_list = ["recruitment@simplisolve.us",candidate.email]  # Replace with actual recipient email addresses
            email1 = EmailMessage(subject, message, from_email, recipient_list,connection=email_connection)
            email1.attach(candidate.resume.name, candidate.resume.file.read())
            email1.send(fail_silently=False)
            request.session['new_data_added'] = True
            Research_scientists = Research_scientist_Data(
                id1=candidate.id,
                first_name=candidate.first_name,
                last_name=candidate.last_name,
                email=candidate.email,
                phone_number=candidate.phone_number,
                resume=candidate.resume.name,
                datetime=candidate.datetime,
                code=candidate.code,
                salary_exceptation=candidate.salary_exceptation,
                like_working_in_team=candidate.like_working_in_team,
                experience_with_ml_framework=candidate.experience_with_ml_framework,
                research_publications=candidate.research_publications,
                experience_as_research_scientist=candidate.experience_as_research_scientist
                )
            Research_scientists.save()

            messages.success(request, 'recuriements/Application submitted successfully.')

            return render(request, 'recuriements/success.html')

        else:

            count=count-1

            error_message = 'Invalid OTP. Please try again.'

            if count==0:

                count=3

                return render(request,'recuriements/max_otp.html')

            return render(request, 'recuriements/otp_confirmation_research_scientist.html', {'candidate_id': candidate_id,'error_message': error_message})
def update_candidate(request, candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    try:

        candidate = Machine_learning_engineer_data.objects.get(id1=candidate_id)

        request.session.pop('new_data_added', None)  
        post="Machine Learning Engineer"

        return render(request, 'recuriements/update_candidate.html', {'candidate': candidate,'post':post})

    except:

        try:

            candidate = Software_application_developer_data.objects.get(id1=candidate_id)

            request.session.pop('new_data_added', None)  
            post="Software Application Developer "

            return render(request, 'recuriements/update_candidate.html', {'candidate': candidate,'post':post})

        except:
            try:
                candidate =Research_scientist_Data.objects.get(id1=candidate_id)

                request.session.pop('new_data_added', None)  
                post="Research Scientist" 

                return render(request, 'recuriements/update_candidate.html', {'candidate': candidate,'post':post})
            except:
                try:
                    candidate =Data_scientist_data.objects.get(id1=candidate_id)

                    request.session.pop('new_data_added', None)  
                    post="Data Scientist" 

                    return render(request, 'recuriements/update_candidate.html', {'candidate': candidate,'post':post})
                except:
                    candidate= get_object_or_404(DestinationModel, id1=candidate_id)
                    request.session.pop('new_data_added', None)  

                    return render(request, 'recuriements/update_candidate.html', {'candidate': candidate})              
def save_scores_technical(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    candidate = get_object_or_404(Interview, id1=candidate_id)

    if request.method == 'POST':

        cand = get_object_or_404(Interview, id1=candidate_id)

        first_name = cand.first_name

        last_name = cand.last_name

         # Collect data for all questions and scores

        question_1 = request.POST.get('question_text_1')

        arafat_score_1 = request.POST.get('arafat_score_1')

        helal_score_1 = request.POST.get('helal_score_1')

        mujib_score_1 = request.POST.get('mujib_score_1')

        

        question_2 = request.POST.get('question_text_2')

        arafat_score_2 = request.POST.get('arafat_score_2')

        helal_score_2 = request.POST.get('helal_score_2')

        mujib_score_2 = request.POST.get('mujib_score_2')

        

        question_3 = request.POST.get('question_text_3')

        arafat_score_3 = request.POST.get('arafat_score_3')

        helal_score_3 = request.POST.get('helal_score_3')

        mujib_score_3 = request.POST.get('mujib_score_3')

        try:

            arafat_score_1 = int(arafat_score_1)

            helal_score_1 = int(helal_score_1)

            mujib_score_1 = int(mujib_score_1)

            arafat_score_2 = int(arafat_score_2)

            helal_score_2 = int(helal_score_2)

            mujib_score_2 = int(mujib_score_2)

            arafat_score_3 = int(arafat_score_3)

            helal_score_3 = int(helal_score_3)

            mujib_score_3 = int(mujib_score_3)

        except ValueError:

            # Handle the case where score fields are not valid numbers

            return HttpResponse("Invalid score values")

        # Save all the collected data as a single record

        score = Score_technical(

            id1=cand.id1,

            candidate=first_name + ' ' + last_name,

            question_1=question_1,

            arafat_score_1=arafat_score_1,

            helal_score_1=helal_score_1,

            mujib_score_1=mujib_score_1,

            question_2=question_2,

            arafat_score_2=arafat_score_2,

            helal_score_2=helal_score_2,

            mujib_score_2=mujib_score_2,

            question_3=question_3,

            arafat_score_3=arafat_score_3,

            helal_score_3=helal_score_3,

            mujib_score_3=mujib_score_3,

        )

        score.save()  # Save the single record

        return redirect('confirmation_page')

    return render(request, 'recuriements/machine_learning.html', {'candidate': candidate})
def save_scores_coding(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    candidate = get_object_or_404(Interview, id1=candidate_id)

    if request.method == 'POST':

        cand = get_object_or_404(Interview, id1=candidate_id)

        first_name = cand.first_name

        last_name = cand.last_name

         # Collect data for all questions and scores

        question_1 = request.POST.get('question_text_1')

        arafat_score_1 = request.POST.get('arafat_score_1')

        helal_score_1 = request.POST.get('helal_score_1')

        mujib_score_1 = request.POST.get('mujib_score_1')

        

        question_2 = request.POST.get('question_text_2')

        arafat_score_2 = request.POST.get('arafat_score_2')

        helal_score_2 = request.POST.get('helal_score_2')

        mujib_score_2 = request.POST.get('mujib_score_2')

        

        question_3 = request.POST.get('question_text_3')

        arafat_score_3 = request.POST.get('arafat_score_3')

        helal_score_3 = request.POST.get('helal_score_3')

        mujib_score_3 = request.POST.get('mujib_score_3')

        try:

            arafat_score_1 = int(arafat_score_1)

            helal_score_1 = int(helal_score_1)

            mujib_score_1 = int(mujib_score_1)

            arafat_score_2 = int(arafat_score_2)

            helal_score_2 = int(helal_score_2)

            mujib_score_2 = int(mujib_score_2)

            arafat_score_3 = int(arafat_score_3)

            helal_score_3 = int(helal_score_3)

            mujib_score_3 = int(mujib_score_3)

        except ValueError:

            # Handle the case where score fields are not valid numbers

            return HttpResponse("Invalid score values")

        # Save all the collected data as a single record

        score = Score_coding(

            id1=cand.id1,

            candidate=first_name + ' ' + last_name,

            question_1=question_1,

            arafat_score_1=arafat_score_1,

            helal_score_1=helal_score_1,

            mujib_score_1=mujib_score_1,

            question_2=question_2,

            arafat_score_2=arafat_score_2,

            helal_score_2=helal_score_2,

            mujib_score_2=mujib_score_2,

            question_3=question_3,

            arafat_score_3=arafat_score_3,

            helal_score_3=helal_score_3,

            mujib_score_3=mujib_score_3,

        )

        score.save()  # Save the single record

        return redirect('confirmation_page')

    return render(request, 'recuriements/machine_learning.html', {'candidate': candidate})
def confirmation_page(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    # Your view logic here

    return render(request, 'recuriements/confirmation_page.html')  # This renders the confirmation page template
def selected_candidate(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    return render(request,'recuriements/selected_candidate.html')
def display_scores(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    # Retrieve all score objects from the database

    candidate_scores = Score_technical.objects.all()
    candidate_score = Score_coding.objects.all()

    return render(request, 'recuriements/score_display.html', {'candidate_scores': candidate_scores})
def accept1(request, candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    if request.method == 'POST':
        candidate=get_object_or_404(Interview,id1=candidate_id)
        interview_type = request.POST.get('interview_type')

        if interview_type == 'technical':
            if candidate.post=='Data Scientist':
                existing_topics = SaveScoreDataScientistTechnical.objects.filter(id1=candidate_id).values_list('topic', flat=True)
                return render(request,'recuriements/Data_scientist_technical_interview.html',{'candidate':candidate,'existing_topics':existing_topics})
            elif candidate.post=="Research Scientist":
                existing_topics = SaveScoreDataScientistTechnical.objects.filter(id1=candidate_id).values_list('topic', flat=True)
                return render(request,'recuriements/Research_Scientist_technical_interview.html',{'candidate':candidate,'existing_topics':existing_topics})
            elif candidate.post=="Software Application Developer":
                print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
                existing_topics = SaveScoreDataScientistTechnical.objects.filter(id1=candidate_id).values_list('topic', flat=True)
                return render(request,'recuriements/Software_Application_Developer_technical_interview.html',{'candidate':candidate,'existing_topics':existing_topics})
            else:
                return render(request,'recuriements/Machine_Learning_Engineer_technical_interview.html',{'candidate':candidate,'existing_topics':existing_topics})


        elif interview_type == 'coding':
        
            

            return render(request,'recuriements/coding.html',{'candidate':candidate})

        elif interview_type=='decision':

            technical_score=get_object_or_404(Score_technical,id1=candidate_id)
            coding_score=get_object_or_404(Score_coding,id1=candidate_id)

            

            return render(request, 'recuriements/final.html', {'technical_score': technical_score,'coding_score':coding_score,'candidate':candidate})

def show_dates_technical(request, candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    candidate = get_object_or_404(Interview, id1=candidate_id)

    dates = InterviewDateTechnical.objects.filter(id1=candidate_id)  # FLilter InterviewDate objects by candidate_id

    return render(request, 'recuriements/interview_invitation.html', {'candidate': candidate, 'dates': dates})

def show_dates_coding(request, candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    candidate = get_object_or_404(Interview, id1=candidate_id)

    dates = InterviewDateCoding.objects.filter(id1=candidate_id)  # FLilter InterviewDate objects by candidate_id

    return render(request, 'recuriements/interview_invitation1.html', {'candidate': candidate, 'dates': dates})

def send_zoom_invitation_technical(request, candidate_id, selected_date):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    candidate = get_object_or_404(Candidate, id=candidate_id)

    meeting_id = 'your-zoom-meeting-id'

    meeting_password = 'your-zoom-meeting-password'

    # Compose the email subject and message

    subject = 'Zoom Meeting Invitation '

    message = f'Hello {candidate.first_name},\n\nYou are invited for Technical interview to a Zoom meeting on {selected_date}.\n\nMeeting ID: {meeting_id}\nMeeting Password: {meeting_password}\n\nJoin the meeting at: https://zoom.us/j/{meeting_id}'

    # Send the email

    from_email = 'support@simplisolve.us'  # Replace with your email address

    recipient_list = [candidate.email]

    try:

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        

        return HttpResponse('Zoom invitation email sent successfully.')

    except Exception as e:

        return HttpResponse(f'Error sending Zoom invitation email: {str(e)}')

def send_zoom_invitation_coding(request, candidate_id, selected_date):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    candidate = get_object_or_404(Candidate, id=candidate_id)

    meeting_id = 'your-zoom-meeting-id'

    meeting_password = 'your-zoom-meeting-password'

    # Compose the email subject and message

    subject = 'Zoom Meeting Invitation '

    message = f'Hello {candidate.first_name},\n\nYou are invited for Coding interview to a Zoom meeting on {selected_date}.\n\nMeeting ID: {meeting_id}\nMeeting Password: {meeting_password}\n\nJoin the meeting at: https://zoom.us/j/{meeting_id}'

    # Send the email

    from_email = 'support@simplisolve.us'  # Replace with your email address

    recipient_list = [candidate.email]

    try:

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return HttpResponse('Zoom invitation email sent successfully.')

    except Exception as e:

        return HttpResponse(f'Error sending Zoom invitation email: {str(e)}')

def machine_learning(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    candidate=get_object_or_404(Interview,id1=candidate_id)

    if request.method=='POST':

        pass

    return render(request,'recuriements/machine_learning.html',{'candidate':candidate})


def remove_candidate_data(request, candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    if request.method == 'POST':

        call_take = request.POST.get('call_take')

        if call_take == 'yes':

            if candidate_id is not None:

                try:

                    candidate= get_object_or_404(DestinationModel, id1=candidate_id)

                    return render(request,'recuriements/take_interview.html',{'candidate':candidate})

                except:

                    try:

                        candidate= get_object_or_404(Data_scientist_data, id1=candidate_id)
                        post="Data Scientist"

                        return render(request,'recuriements/take_interview.html',{'candidate':candidate,'post':post})

                    except:
                        try:

                            candidate= get_object_or_404(Machine_learning_engineer_data, id1=candidate_id)
                            post="Machine Learning Engineer"

                            return render(request,'recuriements/take_interview.html',{'candidate':candidate,'post':post})

                        except:
                            try:

                                candidate=get_object_or_404(Research_scientist_Data,id1=candidate_id)
                                post="Research Scientist"

                                return render(request,'recuriements/take_interview.html',{'candidate':candidate,'post':post})
                            except:
                                try:
                                    candidate=get_object_or_404(Software_application_developer_data,id1=candidate_id)
                                    post="Software Application Developer"

                                    return render(request,'recuriements/take_interview.html',{'candidate':candidate,'post':post})

                                except:

                                    candidate=get_object_or_404(Interview,id1=candidate_id)

                                    return render(request,'recuriements/take_interview.html',{'candidate':candidate})

            else:

                interview_candidates =Interview.objects.all()

                return render(request, 'recuriements/interview.html', {'interview_candidates': interview_candidates})

        elif call_take=='no':

            try:
                candidate= get_object_or_404(DestinationModel, id1=candidate_id)
            except:
                try:
                    candidate= get_object_or_404(Data_scientist_data, id1=candidate_id)
                except:
                    try:
                        candidate= get_object_or_404(Machine_learning_engineer_data, id1=candidate_id)
                    except:
                        try:
                            candidate=get_object_or_404(Research_scientist_Data,id1=candidate_id)
                        except:
                            candidate=get_object_or_404(Software_application_developer_data,id1=candidate_id)
                            
                

            destination_candidate = DestinationModel(

            id1=candidate.id1,

            first_name=candidate.first_name,

            last_name=candidate.last_name,

            email=candidate.email,

            phone_number=candidate.phone_number,

            resume=candidate.resume.name,

            datetime=candidate.datetime,

            code=candidate.code,
            post=request.POST.get('post_data'),

            # =
            )


            destination_candidate.save()

            candidate.delete()  

            destination_candidates = DestinationModel.objects.all()
            

            return render(request, 'recuriements/pending.html', {'destination_candidates': destination_candidates})

            

    interview_candidates =Interview.objects.all()

    return render(request, 'recuriements/interview.html', {'interview_candidates': interview_candidates})

def Data_scientist(request):
    form= CandidateForm()
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate=form.save(commit=False)
            candidate.ip_address, _ = get_client_ip(request)  # Get client's IP address
            # Check if the candidate has exceeded the application limit
            day=60
            two_months_ago = timezone.now() -timedelta(days=day)
            application_count = Candidate.objects.filter(
                # email=candidate.email,
                ip_address=candidate.ip_address, 
                last_application_date__gte=two_months_ago
            ).count()
            print(application_count)
            if application_count >=150:
                remaining_days = (two_months_ago + timedelta(days=day) -timezone.now()).days
                remaining_text=day-remaining_days
                return render(request,'recuriements/max_apply.html',{'days':remaining_text})   
            # Generate and send OTP
            candidate.application_count = application_count + 1
            candidate.last_application_date = timezone.now() 
            # Store OTP in the Candidate model
                # Send OTP via email
            otp = ''.join(str(secrets.randbelow(10)) for i in range(6))
            candidate.otp= otp
            candidate.save()
            with open('simplisolve_app/templates/recuriements/otp_email_form.html', 'r') as file:
                email_template = file.read()
                
            # Replace placeholders in the template
            email_template = email_template.replace('[User]', candidate.first_name+" "+candidate.last_name)
            email_template = email_template.replace('[OTP Code]', str(candidate.otp))
            html_message = email_template
            
            message="Email verification OTP"
            subject = 'Your OTP for Data scientist Application Submission'
        
            from_email = 'recruitment@simplisolve.us'
            recipient_list = [candidate.email]
            send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        html_message=html_message,
        fail_silently=False,
        connection=email_connection
    )
            return render(request,'recuriements/otp_confirmation.html',{'candidate_id':candidate.id}) 
        else:
            print(form.errors)
    else:
        print(form.errors)
    return render(request, 'recuriements/data_scientist.html', {'form': form})

def main_page(request):
    return render(request,'recuriements/main_page.html')
    

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'new_data_added' in request.session:
                new_data_added = request.session.pop('new_data_added')
                request.session['new_data_added'] = True
            else:
                request.session['new_data_added'] = False
            
            # Redirect to multiple pages after login
            # return redirect('dashboard')
            # return render(request, 'recuriements/dashboard.html',{'new_data_added': new_data_added})
            return redirect('dashboard')
        else:
            # Handle invalid login
            return render(request, 'recuriements/login.html', {'error_message': 'Invalid login credentials'})
        
    return render(request,'recuriements/login.html')

def user_logout(request):
    logout(request)
    request.session.pop('profile_name', None) 
    return redirect('https://www.simplisolve.us')



def dashboard(request):
    new_data_added = request.session.pop('new_data_added', False)
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    
    return render(request, 'recuriements/dashboard.html',{'new_data_added': new_data_added})
@never_cache
def apply_candidate(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    request.session.pop('new_data_added', None) 
    
    
    return render(request,'recuriements/career_all_apply.html')
def remove_new_data_indicator(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    if 'new_data_added' in request.session:

        del request.session['new_data_added']

        return JsonResponse({'message': 'Indicator removed'})

    return JsonResponse({'message': 'No indicator to remove'})
def pending(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    destination_candidates = DestinationModel.objects.all()

    return render(request, 'recuriements/pending.html', {'destination_candidates': destination_candidates})
def inter(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    interview_candidates =Interview.objects.all()

    return render(request, 'recuriements/interview.html', {'interview_candidates': interview_candidates})

def take_interview(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    candidate =Interview.objects.get(id1=candidate_id)

    return render(request,'recuriements/take_interview.html',{'candidate':candidate})

def candidate_decision(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    if request.method == 'POST':

        review = request.POST.get('review')

        salary = request.POST.get('salary')

        try:

            candidate = get_object_or_404(DestinationModel, id1=candidate_id)

            interview_candidate = Interview(

                id1=candidate.id1,

                first_name=candidate.first_name,

                last_name=candidate.last_name,

                email=candidate.email,

                phone_number=candidate.phone_number,

                resume=candidate.resume.name,

                datetime=candidate.datetime,

                review=review,

                salary=salary,     
                post=candidate.post,)

            interview_candidate.save()

            candidate.delete()

            interview_candidates =Interview.objects.all()

            return render(request, 'recuriements/interview.html', {'interview_candidates': interview_candidates})

        except:

            try:

                candidate=get_object_or_404(Data_scientist_data,id1=candidate_id)

                interview_candidate = Interview(

                    id1=candidate.id1,

                    first_name=candidate.first_name,

                    last_name=candidate.last_name,

                    email=candidate.email,

                    phone_number=candidate.phone_number,

                    resume=candidate.resume.name,

                    datetime=candidate.datetime,

                    review=review,

                    salary=salary,
                    post="Data Scientist",)

                interview_candidate.save()

                candidate.delete()

                interview_candidates =Interview.objects.all()

                return render(request, 'recuriements/interview.html', {'interview_candidates': interview_candidates})

            except:
                try:
                    candidate=get_object_or_404(Software_application_developer_data,id1=candidate_id)

                    interview_candidate = Interview(

                    id1=candidate.id1,

                    first_name=candidate.first_name,

                    last_name=candidate.last_name,

                    email=candidate.email,

                    phone_number=candidate.phone_number,

                    resume=candidate.resume.name,

                    datetime=candidate.datetime,

                    review=review,

                    salary=salary,    
                    post="Software Application Developer",)

                    interview_candidate.save()

                    candidate.delete()

                    interview_candidates =Interview.objects.all()

                    return render(request, 'recuriements/interview.html', {'interview_candidates': interview_candidates})
                except:
                    try:
                        candidate=get_object_or_404(Research_scientist_Data,id1=candidate_id)

                        interview_candidate = Interview(

                        id1=candidate.id1,

                        first_name=candidate.first_name,

                        last_name=candidate.last_name,

                        email=candidate.email,

                        phone_number=candidate.phone_number,

                        resume=candidate.resume.name,

                        datetime=candidate.datetime,

                        review=review,

                        salary=salary, 
                        post="Research Scientist",   )

                        interview_candidate.save()

                        candidate.delete()

                        interview_candidates =Interview.objects.all()

                        return render(request, 'recuriements/interview.html', {'interview_candidates': interview_candidates})
                    except:
                        try:
                            candidate=get_object_or_404(Machine_learning_engineer_data,id1=candidate_id)

                            interview_candidate = Interview(

                            id1=candidate.id1,

                            first_name=candidate.first_name,

                            last_name=candidate.last_name,

                            email=candidate.email,

                            phone_number=candidate.phone_number,

                            resume=candidate.resume.name,

                            datetime=candidate.datetime,

                            review=review,

                            salary=salary,      
                            post="Machine Learning Engineer",     )

                            interview_candidate.save()

                            candidate.delete()

                            interview_candidates =Interview.objects.all()

                            return render(request, 'recuriements/interview.html', {'interview_candidates': interview_candidates})
                        except:

                            candidate=get_object_or_404(Interview,id1=candidate_id)

                            interview_candidate = Interview(

                                id1=candidate.id1,

                                first_name=candidate.first_name,

                                last_name=candidate.last_name,

                                email=candidate.email,

                                phone_number=candidate.phone_number,

                                resume=candidate.resume.name,

                                datetime=candidate.datetime,

                                review=review,

                                salary=salary,
                                post=candidate.post )

                            interview_candidate.save()

                            candidate.delete()

                            interview_candidates =Interview.objects.all()

                            return render(request, 'recuriements/interview.html', {'interview_candidates': interview_candidates})

    return render(request,'recuriements/take_interview.html',{'candidate':candidate})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def reject_candidate(request, candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    try:

        candidate = get_object_or_404(Data_scientist_data, id1=candidate_id)

    except:

        try:

            candidate = get_object_or_404(DestinationModel, id1=candidate_id)

        except:
            try:

                candidate = get_object_or_404(Machine_learning_engineer_data, id1=candidate_id)

            except:
                try:

                    candidate = get_object_or_404(Software_application_developer_data, id1=candidate_id)

                except:
                    try:

                        candidate = get_object_or_404(Research_scientist_Data, id1=candidate_id)
                    except:
                        try:

                            candidate = get_object_or_404(Interview, id1=candidate_id)
                        except:
                            try:
                                candidate = get_object_or_404(Score_technical, id1=candidate_id)
                            except:
                                candidate = get_object_or_404(Score_coding, id1=candidate_id)
                            

    if request.method == 'POST':

        rejection_reason = request.POST.get('rejection_reason')
        reject_by = request.POST.get('reject_by')

        rejection_candidate = RejectionModel(

            id1=candidate.id1,

            first_name=candidate.first_name,

            last_name=candidate.last_name,

            email=candidate.email,

            resume=candidate.resume,

            datetime=candidate.datetime,

            

            code=candidate.code,

            phone_number=candidate.phone_number,

            rejection_reason=rejection_reason,
            reject_by=reject_by

        )

        rejection_candidate.save()

        candidate_name=f'{candidate.first_name}{candidate.last_name}'

        candidate_phone_number=f'{candidate.code}{candidate.phone_number}'

        subject = 'Rejection Message '

        message = f'Name:{candidate_name}\nPhone: {candidate_phone_number}\nEmail: {candidate.email}\nrejection_reason:{rejection_reason}'

        from_email = 'support@simplisolve.us'  # Use a valid email address

        recipient_list = ["dpkchoudhary103@gmail.com",f"{candidate.email}"]  # Replace with actual recipient email addresses

        email = EmailMessage(subject, message, from_email, recipient_list)

        email.send()

        messages.success(request, 'recuriements/Application submitted successfully and email sent.')

        candidate.delete()

        reject_candidates=RejectionModel.objects.all()

        return render(request,'recuriements/reject_candidates.html',{'reject_candidates':reject_candidates})

    return render(request, 'recuriements/reject_candidate.html', {'candidate': candidate})

def reject_candidates(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')

    reject_candidates = RejectionModel.objects.all()
    return render(request, 'recuriements/reject_candidates.html', {'reject_candidates': reject_candidates})


def Call_to_action(request):
    return render(request,'Call_action.html')
def Contact_us(request):
    form= ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.ip_address, _ =get_client_ip(request)  # Get client's IP address
            current_time = timezone.now()
            print(current_time)
            past_hour_threshold = current_time - timezone.timedelta(hours=1)
            print(past_hour_threshold)
            application_count = Contact.objects.filter(
                ip_address=user.ip_address, 
                last_application_date__gte=past_hour_threshold
            ).count()
            print(application_count)
            sub=request.POST.get("selected_subject")
            if(len(sub) == 0):
                error='Please select a subject'
                return render(request,'Contact_us.html',{'error_message':error})
            selected_subject=sub.replace(' ','_')
            messag=request.POST['message']
            print(type(messag),len(messag))
            
            if(len(messag) <=1):
                error='Message field must be filled'
                return render(request,'Contact_us.html',{'error_message':error})
            elif messag.count(" ")<20:
                error='Message has to be at least 20 words '
                return render(request,'Contact_us.html',{'error_message':error})
            user_message=messag.replace(' ','_')
            nam=request.POST['name']
            user_name=nam.replace(' ','_')
            user_email=request.POST['email']
            if application_count >=13:
                return redirect('Max_apply')   
            # Generate and send OTP
            user.application_count = application_count + 1
            user.last_application_date = timezone.now() 
            
            # Store OTP in the Candidate model
                # Send OTP via email
            
        
            otp = ''.join(str(secrets.randbelow(10)) for i in range(6))
            user.otp= otp
            user.save()
        
            with open('simplisolve_app/templates/recuriements/code_email_form.html', 'r') as file:
                email_template = file.read()
                
            # Replace placeholders in the template
            email_template = email_template.replace('[User]', user_name)
            email_template = email_template.replace('[Code]', str(user.otp))
            html_message = email_template
            
            message="Email verification Code"
        
            subject = "Email Verification Code "
            from_email = 'support@simplisolve.us'
            recipient_list = [user_email]

            email = EmailMessage(subject, message, from_email, recipient_list)
            email.content_subtype = 'html'  # Set the content type to HTML
            email.body = html_message 
            

            email.send()
            return render(request,'email_confirmation.html',{'user_id':user.id,'selected_subject':selected_subject,'user_message':user_message,'user_name':user_name,'user_email':user_email}) 

            # return render(request,'thank_you.html') 
    
        else:

            print(form.errors)
            return render(request, 'Contact_us.html', {'form': form})
    return render(request, 'Contact_us.html', {'form': form})
def confirm_code(request, user_id,selected_subject,user_message,user_name,user_email):
    global count
    error_message = None  
    user = get_object_or_404(Contact, id=user_id)
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if user.otp == int(float((entered_otp))):
            # OTP matched, proceed with application submission
            user.submitted = True
            user.save()
            user_id = user.id
            nam= user_name
            user_name=nam.replace('_',' ')
            user_email=user_email
            messag=user_message
            mess=messag.replace('_',' ')
            sub1=selected_subject
            selected_subject=sub1.replace('_',' ')
            subject = 'New Contact application Submission'
            message = f'Name:-{user_name}\nSubject:-{selected_subject}\nEmail: {user_email}\nMessage: {mess}'
            from_email = 'support@simplisolve.us'  # Use a valid email address
            recipient_list = [user_email,'support@simplisolve.us']  # Replace with actual recipient email addresses
            email1 = EmailMessage(subject, message, from_email, recipient_list)
            email1.send()
            return redirect('thank_you')
 
        else:
            count=count-1
            error_message = 'Invalid OTP. Please try again.'
            if count==0:
                count=3
                return redirect('Max_code')
            return render(request, 'email_confirmation.html', {'user_id': user_id,'selected_subject':selected_subject,'user_message':user_message,'user_name':user_name,'user_email':user_email,'error_message': error_message})
    return render(request, 'email_confirmation.html', {'user_id': user_id,'selected_subject':selected_subject,'user_message':user_message,'user_name':user_name,'user_email':user_email})
def thank_you(request):
    return render(request,'thank_you.html')
def Max_code(request):
    return render(request,'Max_code.html')
def Max_apply(request):
    return render(request,'Max_apply.html')


def Research_scientist_engineer(request):
    form= Research_scientist_form()
    if request.method == 'POST':
        form = Research_scientist_form(request.POST, request.FILES)
        if form.is_valid():
            candidate=form.save(commit=False)
            candidate.ip_address, _ = get_client_ip(request)  # Get client's IP address
            # Check if the candidate has exceeded the application limit
            day=60
            two_months_ago = timezone.now() -timedelta(days=day)
            application_count = Research_scientist.objects.filter(
                # email=candidate.email,
                ip_address=candidate.ip_address, 
                last_application_date__gte=two_months_ago
            ).count()
            print(application_count)
            if application_count >=20:
                remaining_days = (two_months_ago + timedelta(days=day) -timezone.now()).days
                remaining_text=day-remaining_days
                return render(request,'recuriements/max_apply.html',{'days':remaining_text})   
            # Generate and send OTP
            candidate.application_count = application_count + 1
            candidate.last_application_date = timezone.now() 
            # Store OTP in the Candidate model
                # Send OTP via email
            otp = ''.join(str(secrets.randbelow(10)) for i in range(6))
            candidate.otp= otp
            candidate.save()
            with open('simplisolve_app/templates/recuriements/otp_email_form.html', 'r') as file:
                email_template = file.read()
                
            # Replace placeholders in the template
            email_template = email_template.replace('[User]', candidate.first_name+" "+candidate.last_name)
            email_template = email_template.replace('[OTP Code]', str(candidate.otp))
            html_message = email_template
            
            message="Email verification OTP"
            subject = 'Your OTP for Research scientist Application Submission'
            
        
            from_email = 'recruitment@simplisolve.us'
            recipient_list = [candidate.email]
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                html_message=html_message,
                fail_silently=False,
                connection=email_connection)
            
           
            return render(request,'recuriements/otp_confirmation_research_scientist.html',{'candidate_id':candidate.id}) 
        else:
            print(form.errors)
    else:
        print(form.errors)
    return render(request, 'recuriements/research_scientist.html', {'form': form})


def Machine_learning(request):
    form= Machine_learning_engineer_form()
    if request.method == 'POST':
        form = Machine_learning_engineer_form(request.POST, request.FILES)
        if form.is_valid():
            candidate=form.save(commit=False)
            candidate.ip_address, _ = get_client_ip(request)  # Get client's IP address
            # Check if the candidate has exceeded the application limit
            day=60
            two_months_ago = timezone.now() -timedelta(days=day)
            application_count =Machine_learning_engineer.objects.filter(
                # email=candidate.email,
                ip_address=candidate.ip_address, 
                last_application_date__gte=two_months_ago
            ).count()
            print(application_count)
            if application_count >=20:
                remaining_days = (two_months_ago + timedelta(days=day) -timezone.now()).days
                remaining_text=day-remaining_days
                return render(request,'recuriements/max_apply.html',{'days':remaining_text})   
            # Generate and send OTP
            candidate.application_count = application_count + 1
            candidate.last_application_date = timezone.now() 
            # Store OTP in the Candidate model
                # Send OTP via email
            otp = ''.join(str(secrets.randbelow(10)) for i in range(6))
            candidate.otp= otp
            candidate.save()
            with open('simplisolve_app/templates/recuriements/otp_email_form.html', 'r') as file:
                email_template = file.read()
                
            # Replace placeholders in the template
            email_template = email_template.replace('[User]', candidate.first_name+" "+candidate.last_name)
            email_template = email_template.replace('[OTP Code]', str(candidate.otp))
            html_message = email_template
            
            message="Email verification OTP"
            subject = 'Your OTP for  Machine learning Application Submission'
        
            from_email = 'recruitment@simplisolve.us'
            recipient_list = [candidate.email]
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                html_message=html_message,
                fail_silently=False,
                connection=email_connection)
            
            
            
            return render(request,'recuriements/otp_confirmation_machine_learning.html',{'candidate_id':candidate.id}) 
        else:
            print(form.errors)
    else:
        print(form.errors)
    return render(request, 'recuriements/machine_learning_engineer.html', {'form': form})


def Software_application(request):
    form= Software_application_developer_form()
    if request.method == 'POST':
        form = Software_application_developer_form(request.POST, request.FILES)
        if form.is_valid():
            candidate=form.save(commit=False)
            candidate.ip_address, _ = get_client_ip(request)  # Get client's IP address
            # Check if the candidate has exceeded the application limit
            day=60
            two_months_ago = timezone.now() -timedelta(days=day)
            application_count =Software_application_developer.objects.filter(
                # email=candidate.email,
                ip_address=candidate.ip_address, 
                last_application_date__gte=two_months_ago
            ).count()
            print(application_count)
            if application_count >=20:
                remaining_days = (two_months_ago + timedelta(days=day) -timezone.now()).days
                remaining_text=day-remaining_days
                return render(request,'recuriements/max_apply.html',{'days':remaining_text})   
            # Generate and send OTP
            candidate.application_count = application_count + 1
            candidate.last_application_date = timezone.now() 
            # Store OTP in the Candidate model
                # Send OTP via email
            otp = ''.join(str(secrets.randbelow(10)) for i in range(6))
            candidate.otp= otp
            candidate.save()
            with open('simplisolve_app/templates/recuriements/otp_email_form.html', 'r') as file:
                email_template = file.read()
                
            # Replace placeholders in the template
            email_template = email_template.replace('[User]', candidate.first_name+" "+candidate.last_name)
            email_template = email_template.replace('[OTP Code]', str(candidate.otp))
            html_message = email_template
            
            message="Email verification OTP"
        
            subject = 'Your OTP for  software developer Application Submission'
        
            from_email = 'recruitment@simplisolve.us'
            recipient_list = [candidate.email]
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                html_message=html_message,
                fail_silently=False,
                connection=email_connection)
            
           
            
            return render(request,'recuriements/otp_confirmation_software_developer.html',{'candidate_id':candidate.id}) 
        else:
            print(form.errors)
    else:
        print(form.errors)
    return render(request, 'recuriements/software_developer_application.html', {'form': form})
def permission_page(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    return render(request,'recuriements/permission_page.html')
    
def Software_application_developer_apply(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    if not request.user.has_perm('simplisolve_app.view_software_application_developer_data'):
        return redirect('permission_page')
    request.session.pop('new_data_added', None) 
    candidates = Software_application_developer_data.objects.all()
    return render(request,'recuriements/Software_application_developer_apply.html',{'candidates':candidates})
def Machine_learning_engineer_apply(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    request.session.pop('new_data_added', None) 
    candidates = Machine_learning_engineer_data.objects.all()
    return render(request,'recuriements/Machine_learning_engineer_apply.html',{'candidates':candidates})
def Data_scientist_apply(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    request.session.pop('new_data_added', None) 
    candidates = Data_scientist_data.objects.all()
    return render(request,'recuriements/Data_scientist_apply.html',{'candidates':candidates})

def Research_scientist_apply(request):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    request.session.pop('new_data_added', None) 
    candidates =Research_scientist_Data.objects.all()
    return render(request,'recuriements/Research_scientist_apply.html',{'candidates':candidates})
def software_details(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    if not request.user.has_perm('simplisolve_app.view_software_application_developer_data'):
        return redirect('login')
    candidates=get_object_or_404(Software_application_developer_data,id1=candidate_id)
    return render(request,'recuriements/software_details.html',{'candidates':candidates})
def Machine_details(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    candidates=get_object_or_404(Machine_learning_engineer_data,id1=candidate_id)
    return render(request,'recuriements/Machine_details.html',{'candidates':candidates})
def Data_details(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    candidates=get_object_or_404(Data_scientist_data,id1=candidate_id)
    return render(request,'recuriements/Data_details.html',{'candidates':candidates})
def Research_details(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('')
    candidates=get_object_or_404(Research_scientist_Data,id1=candidate_id)
    return render(request,'recuriements/Research_details.html',{'candidates':candidates})
def page_not_found(request):
    return render(request,'recuriements/404.html')
def interview_process_view(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    coding_score_exists = Score_coding.objects.filter(id1=candidate_id).exists()

    # Check if data exists in Score_technical table for the given candidate_id
    technical_score_exists = Score_technical.objects.filter(id1=candidate_id).exists()

    interview_candidate = get_object_or_404(Interview, id1=candidate_id)
    
    return render(request, 'recuriements/interview_whole_process.html', {
        'interview_candidate': interview_candidate,
        'coding_score_exists': coding_score_exists,
        'technical_score_exists': technical_score_exists
    })
    
def rejectdata(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    try:

        candidate = get_object_or_404(Data_scientist_data, id1=candidate_id)

    except:

        try:

            candidate = get_object_or_404(DestinationModel, id1=candidate_id)

        except:
            try:

                candidate = get_object_or_404(Machine_learning_engineer_data, id1=candidate_id)

            except:
                try:

                    candidate = get_object_or_404(Software_application_developer_data, id1=candidate_id)

                except:
                    try:

                        candidate = get_object_or_404(Research_scientist_Data, id1=candidate_id)
                    except:
                        try:

                            candidate = get_object_or_404(Interview, id1=candidate_id)
                        except:
                            try:
                                candidate = get_object_or_404(Score_technical, id1=candidate_id)
                                
                            except:
                                candidate = get_object_or_404(Score_coding, id1=candidate_id)

    
    return render(request,'recuriements/rejectdata.html',{'candidate':candidate})
def rejection_reason(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    a=get_object_or_404(RejectionModel,id1=candidate_id)
    return render(request,'recuriements/rejection_reason.html',{'candidate_id':a})
def review_salary(request,candidate_id):
    if not request.user.is_authenticated:
        # Redirect to login if not authenticated
        return redirect('login')
    a=get_object_or_404(Interview,id1=candidate_id)
    return render(request,'recuriements/review_salary.html',{'candidate':a})