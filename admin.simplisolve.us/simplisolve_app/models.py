from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Research_scientist(models.Model):

    id = models.AutoField(primary_key=True)
    def save(self, *args, **kwargs):
        if not self.id:  # Check if custom ID is not set
            starting_value = 1

            # Find the highest existing custom_id
            max_custom_id =Research_scientist_Data.objects.aggregate(models.Max('id1'))['id1__max']
        
            try:

                if max_custom_id is not None:
                    self.id = max(starting_value, int(max_custom_id)+ 1)
        
                else:
                    self.id = starting_value
            except:
                self.id = starting_value
                
        return super().save(*args, **kwargs)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,default="")
    country_code = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes_data_scientist/')
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    # country_name=models.CharField(max_length=50,default="")
    code=models.CharField(max_length=20,default="+1")
    rejection_reason = models.TextField(max_length=1000,null=True)
    otp = models.PositiveIntegerField(null=True, blank=True)
    submitted = models.BooleanField(default=False)
    application_count = models.PositiveIntegerField(default=0)
    last_application_date = models.DateTimeField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    salary_exceptation = models.DecimalField(max_digits=10, decimal_places=2)
    VISA_SPONSORSHIP_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    like_working_in_team = models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    experience_with_ml_framework = models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    research_publications=models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    experience_as_research_scientist = models.CharField(
        choices=[
            ('<1', 'Less than a year'),
            ('1-2', '1 - 2 years'),
            ('2-4', '2 - 4 years'),
            ('4-7', '4 - 7 years'),
        ],
        max_length=3
    )
class Research_scientist_Data(models.Model):
    # class Meta:
    #     permissions = [
    #         ("view_research_scientist_data", "Can do something description"),
    #         # Add more custom permissions here
    #     ]
    id1= models.CharField(max_length=20,default="")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,default="")
    country_code = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes_data_scientist/')
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    # country_name=models.CharField(max_length=50,default="")
    code=models.CharField(max_length=20,default="+1")
    rejection_reason = models.TextField(max_length=1000,null=True)
    # otp = models.PositiveIntegerField(null=True, blank=True)
    # submitted = models.BooleanField(default=False)
    # application_count = models.PositiveIntegerField(default=0)
    # last_application_date = models.DateTimeField(null=True, blank=True)
    # ip_address = models.GenericIPAddressField(blank=True, null=True)
    salary_exceptation = models.DecimalField(max_digits=10, decimal_places=2)
    VISA_SPONSORSHIP_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    like_working_in_team = models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    experience_with_ml_framework = models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    research_publications=models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    experience_as_research_scientist = models.CharField(
        choices=[
            ('<1', 'Less than a year'),
            ('1-2', '1 - 2 years'),
            ('2-4', '2 - 4 years'),
            ('4-7', '4 - 7 years'),
        ],
        max_length=3
    )
class Machine_learning_engineer(models.Model):
    id = models.AutoField(primary_key=True)
    def save(self, *args, **kwargs):
        if not self.id:  # Check if custom ID is not set
            starting_value = 100000

            # Find the highest existing custom_id
            max_custom_id =Machine_learning_engineer_data.objects.aggregate(models.Max('id1'))['id1__max']
            print("ff",max_custom_id)
            try:

                if max_custom_id is not None:
                    self.id = max(starting_value, int(max_custom_id)+ 1)
                    print('ggg',self.id)
                else:
                    self.id = starting_value
            except:
                self.id = starting_value
                
        return super().save(*args, **kwargs)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,default="")
    country_code = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    # country_name=models.CharField(max_length=50,default="")
    code=models.CharField(max_length=20,default="+1")
    rejection_reason = models.TextField(max_length=1000,null=True)
    otp = models.PositiveIntegerField(null=True, blank=True)
    submitted = models.BooleanField(default=False)
    salary_exceptation =models.DecimalField(max_digits=10, decimal_places=2)
    application_count = models.PositiveIntegerField(default=0)
    last_application_date = models.DateTimeField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    VISA_SPONSORSHIP_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    experience_generative_models= models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    experience_ml_pipelines= models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    preferred_work_location = models.CharField(
        choices=[
            ('remote', 'I d like to work remotely'),
            ('onsite', 'I d prefer to work onsite'),
            ('hybrid', 'I d prefer to work in a hybrid fashion'),
        ],
        max_length=10
            )


    def __str__(self):

        return "%s %s"  %(self.first_name,self.email)
class Machine_learning_engineer_data(models.Model):
    id1 = models.CharField(max_length=500,default="")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,default="")
    country_code = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    # country_name=models.CharField(max_length=50,default="")
    code=models.CharField(max_length=20,default="+1")
    rejection_reason = models.TextField(max_length=1000,null=True)
    # otp = models.PositiveIntegerField(null=True, blank=True)
    # submitted = models.BooleanField(default=False)
    salary_exceptation =models.DecimalField(max_digits=10, decimal_places=2)
    # application_count = models.PositiveIntegerField(default=0)
    # last_application_date = models.DateTimeField(null=True, blank=True)
    # ip_address = models.GenericIPAddressField(blank=True, null=True)
    VISA_SPONSORSHIP_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    experience_generative_models= models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    experience_ml_pipelines= models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    preferred_work_location = models.CharField(
        choices=[
            ('remote', 'I d like to work remotely'),
            ('onsite', 'I d prefer to work onsite'),
            ('hybrid', 'I d prefer to work in a hybrid fashion'),
        ],
        max_length=10
            )


    def __str__(self):

        return "%s %s"  %(self.first_name,self.email)
class Software_application_developer(models.Model):
    id = models.AutoField(primary_key=True)
    def save(self, *args, **kwargs):
        if not self.id:  # Check if custom ID is not set
            starting_value = 200000

            # Find the highest existing custom_id
            max_custom_id = Software_application_developer_data.objects.aggregate(models.Max('id1'))['id1__max']
        
            try:

                if max_custom_id is not None:
                    self.id = max(starting_value, int(max_custom_id)+ 1)
            
                else:
                    self.id = starting_value
            except:
                self.id = starting_value
                
        return super().save(*args, **kwargs)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,default="")
    country_code = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    # country_name=models.CharField(max_length=50,default="")
    code=models.CharField(max_length=20,default="+1")
    rejection_reason = models.TextField(max_length=1000,null=True)
    otp = models.PositiveIntegerField(null=True, blank=True)
    submitted = models.BooleanField(default=False)
    salary_exceptation =models.DecimalField(max_digits=10, decimal_places=2)
    application_count = models.PositiveIntegerField(default=0)
    last_application_date = models.DateTimeField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    project_link = models.URLField(max_length=200, blank=True, null=True)
    software_dev_experience = models.CharField(
        choices=[
            ('<1', 'Less than a year'),
            ('1-2', '1 - 2 years'),
            ('2-4', '2 - 4 years'),
            ('4-7', '4 - 7 years'),
        ],
        max_length=3
    )
    VISA_SPONSORSHIP_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    experience_with_sql= models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    us_citizen_or_permanent_resident= models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    

    def __str__(self):

        return "%s %s"  %(self.first_name,self.email)
class Software_application_developer_data(models.Model):
    id1 =  models.CharField(max_length=500,default="")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,default="")
    country_code = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    # country_name=models.CharField(max_length=50,default="")
    code=models.CharField(max_length=20,default="+1")
    rejection_reason = models.TextField(max_length=1000,null=True)
    # otp = models.PositiveIntegerField(null=True, blank=True)
    # submitted = models.BooleanField(default=False)
    salary_exceptation =models.DecimalField(max_digits=10, decimal_places=2)
    # application_count = models.PositiveIntegerField(default=0)
    # last_application_date = models.DateTimeField(null=True, blank=True)
    # ip_address = models.GenericIPAddressField(blank=True, null=True)
    project_link = models.URLField(max_length=200, blank=True, null=True)
    software_dev_experience = models.CharField(
        choices=[
            ('<1', 'Less than a year'),
            ('1-2', '1 - 2 years'),
            ('2-4', '2 - 4 years'),
            ('4-7', '4 - 7 years'),
        ],
        max_length=3
    )
    VISA_SPONSORSHIP_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    experience_with_sql= models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    us_citizen_or_permanent_resident= models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)
    

    def __str__(self):

        return "%s %s"  %(self.first_name,self.email)

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    new_notifications = models.PositiveIntegerField(default=0)

    def __str__(self):

        return "%s" %(self.user)

class RejectionModel(models.Model):

    id1=models.CharField(max_length=20,default="")

    first_name = models.CharField(max_length=100,default="")

    last_name=models.CharField(max_length=100,default="",blank=True)

    email=models.CharField(max_length=100,default="")

    resume=models.FileField(upload_to='rejection_resume/',default="")

    datetime=models.DateTimeField(default=timezone.now)

    country_name=models.CharField(max_length=100,default="")

    code=models.CharField(max_length=20,default="")

    rejection_reason = models.TextField(max_length=1000,default=" ",null=True)
    reject_by = models.TextField(max_length=1000,default=" ",null=True)

    phone_number = models.CharField(max_length=15,default="")

    def __str__(self):

        return self.first_name

class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    def save(self, *args, **kwargs):
        if not self.id:  # Check if custom ID is not set
            starting_value = 300000

            # Find the highest existing custom_id
            max_custom_id =Data_scientist_data.objects.aggregate(models.Max('id1'))['id1__max']
            try:

                if max_custom_id is not None:
                    self.id = max(starting_value, int(max_custom_id)+ 1)
                else:
                    self.id = starting_value
            except:
                self.id = starting_value
                
        return super().save(*args, **kwargs)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,default="")
    country_code = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    # country_name=models.CharField(max_length=50,default="")
    code=models.CharField(max_length=20,default="+1")
    rejection_reason = models.TextField(max_length=1000,null=True)
    otp = models.PositiveIntegerField(null=True, blank=True)
    submitted = models.BooleanField(default=False)
    salary_exceptation =models.DecimalField(max_digits=10, decimal_places=2)
    application_count = models.PositiveIntegerField(default=0)
    last_application_date = models.DateTimeField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    EXPERIENCE_CHOICES = [
        ('Python', 'Python'),
        ('R', 'R'),
        ('Statistics', 'Statistics'),
        ('All of the above', 'All of the above'),
    ]
    experience_fields = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    YEARS_EXPERIENCE_CHOICES = [
        ('0', '0'),
        ('1-3', '1-3'),
        ('4-6', '4-6'),
        ('7-9', '7-9'),
        ('10+', '10+'),
    ]
    predictive_model_experience = models.CharField(max_length=5, choices=YEARS_EXPERIENCE_CHOICES)
    data_visualization_experience = models.CharField(max_length=5, choices=YEARS_EXPERIENCE_CHOICES)
    VISA_SPONSORSHIP_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    visa_sponsorship = models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)

    def __str__(self):

        return "%s %s"  %(self.first_name,self.email)
class Data_scientist_data(models.Model):
    id1 =  models.CharField(max_length=500,default="")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,default="")
    country_code = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    # country_name=models.CharField(max_length=50,default="")
    code=models.CharField(max_length=20,default="+1")
    rejection_reason = models.TextField(max_length=1000,null=True)
    otp = models.PositiveIntegerField(null=True, blank=True)
    salary_exceptation =models.DecimalField(max_digits=10, decimal_places=2)
    
    EXPERIENCE_CHOICES = [
        ('Python', 'Python'),
        ('R', 'R'),
        ('Statistics', 'Statistics'),
        ('All of the above', 'All of the above'),
    ]
    experience_fields = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    YEARS_EXPERIENCE_CHOICES = [
        ('0', '0'),
        ('1-3', '1-3'),
        ('4-6', '4-6'),
        ('7-9', '7-9'),
        ('10+', '10+'),
    ]
    predictive_model_experience = models.CharField(max_length=5, choices=YEARS_EXPERIENCE_CHOICES)
    data_visualization_experience = models.CharField(max_length=5, choices=YEARS_EXPERIENCE_CHOICES)
    VISA_SPONSORSHIP_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    visa_sponsorship = models.CharField(max_length=3, choices=VISA_SPONSORSHIP_CHOICES)

    def __str__(self):

        return "%s %s"  %(self.first_name,self.email)



class DestinationModel(models.Model):

    id1=models.CharField(max_length=20,default="")

    first_name = models.CharField(max_length=100,default="")
    post=models.CharField(max_length=40,null=True)

    last_name = models.CharField(max_length=100,default="",blank=True)

    email = models.EmailField(default="")

    code=models.CharField(max_length=20,default="")

    phone_number = models.CharField(max_length=20,default="") 

    resume = models.FileField(upload_to='destination_resumes/', default="")  # New field

    datetime = models.DateTimeField(default=timezone.now)  # New field 

    country_name=models.CharField(max_length=50,default="")

    def __str__(self):

        return self.first_name
from django.db import models
from django.utils import timezone

class Topic(models.Model):
    name = models.CharField(max_length=100)

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)


class Interview(models.Model):

    id1=models.CharField(max_length=20,default="")
    post=models.CharField(max_length=40,null=True)

    first_name = models.CharField(max_length=100,default="")

    last_name = models.CharField(max_length=100,default="",blank=True)

    email = models.EmailField(default="")

    phone_number = models.CharField(max_length=20,default="") 

    resume = models.FileField(upload_to='interview_resumes/', default="")  # New field

    datetime = models.DateTimeField(default=timezone.now)  # New field 

    review=models.CharField(max_length=500,default="")

    salary=models.CharField(max_length=10,default="")

    is_rejected = models.BooleanField(default=False)

    country_name=models.CharField(max_length=50,default="")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True,default=None)

    code=models.CharField(max_length=50,default="")

    rejection_reason = models.TextField(default=" ",max_length=1000,null=True)

    meeting_link = models.URLField(max_length=500,default="")

    interview_dates = models.DateField(null=True, blank=True)

    calendly_embed_code = models.CharField(max_length=500, default='https://calendly.com/dpkchoudhary103/interview')  

    def __str__(self):

        return f"{self.first_name} {self.last_name}"
class SaveScoreDataScientistTechnical(models.Model):
    id1=models.CharField(max_length=100,default="")
    topic=models.CharField(max_length=100,default="")
    question1=models.CharField(max_length=100,default="")
    marks1=models.PositiveIntegerField(null=True, blank=True)
    question2=models.CharField(max_length=100,default="")
    marks2=models.PositiveIntegerField(null=True, blank=True)
    question3=models.CharField(max_length=100,default="")
    marks3=models.PositiveIntegerField(null=True, blank=True)
    question4=models.CharField(max_length=100,default="")
    marks4=models.PositiveIntegerField(null=True, blank=True)
    

class Marks(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    marks = models.IntegerField()
class Score_technical(models.Model):

    id1=models.CharField(max_length=10,default="")

    candidate = models.CharField(max_length=50,default="")

    question_1 = models.TextField(default="")

    arafat_score_1 = models.PositiveIntegerField(null=True, blank=True)

    helal_score_1 = models.PositiveIntegerField(null=True, blank=True)

    mujib_score_1 = models.PositiveIntegerField(null=True, blank=True)

     # Add a field for the first question

    question_2 = models.TextField(default="")  # Add a field for the second question

    arafat_score_2 = models.PositiveIntegerField(null=True, blank=True)

    helal_score_2 = models.PositiveIntegerField(null=True, blank=True)

    mujib_score_2 = models.PositiveIntegerField(null=True, blank=True)

    question_3 = models.TextField(default="")  

    arafat_score_3 = models.PositiveIntegerField(null=True, blank=True)

    helal_score_3 = models.PositiveIntegerField(null=True, blank=True)

    mujib_score_3 = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):

        return self.candidate
class Score_coding(models.Model):

    id1=models.CharField(max_length=10,default="")

    candidate = models.CharField(max_length=50,default="")

    question_1 = models.TextField(default="")

    arafat_score_1 = models.PositiveIntegerField(null=True, blank=True)

    helal_score_1 = models.PositiveIntegerField(null=True, blank=True)

    mujib_score_1 = models.PositiveIntegerField(null=True, blank=True)

     # Add a field for the first question

    question_2 = models.TextField(default="")  # Add a field for the second question

    arafat_score_2 = models.PositiveIntegerField(null=True, blank=True)

    helal_score_2 = models.PositiveIntegerField(null=True, blank=True)

    mujib_score_2 = models.PositiveIntegerField(null=True, blank=True)

    question_3 = models.TextField(default="")  

    arafat_score_3 = models.PositiveIntegerField(null=True, blank=True)

    helal_score_3 = models.PositiveIntegerField(null=True, blank=True)

    mujib_score_3 = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):

        return self.candidate

class InterviewDateTechnical(models.Model):

    id1=models.CharField(max_length=20,default="")

    selected_date_1 = models.DateTimeField(null=True, blank=True)

    selected_date_2 = models.DateTimeField(null=True, blank=True)

    selected_date_3 = models.DateTimeField(null=True, blank=True)

    def __str__(self):

        return self.id1

class InterviewDateCoding(models.Model):

    id1=models.CharField(max_length=20,default="")

    selected_date_1 = models.DateTimeField(null=True, blank=True)

    selected_date_2 = models.DateTimeField(null=True, blank=True)

    selected_date_3 = models.DateTimeField(null=True, blank=True)

    def __str__(self):

        return self.id1
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    def save(self, *args, **kwargs):
        if not self.id:  # Check if custom ID is not set
            starting_value = 400000

            # Find the highest existing custom_id
            max_custom_id = Contact.objects.aggregate(models.Max('id1'))['id1__max']
            print("ff",max_custom_id)
            try:

                if max_custom_id is not None:
                    self.id = max(starting_value, int(max_custom_id)+ 1)
                    print('ggg',self.id)
                else:
                    self.id = starting_value
            except:
                self.id = starting_value
                
        return super().save(*args, **kwargs)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message=models.TextField(max_length=1000 ,default="")
    application_count = models.PositiveIntegerField(default=0)
    otp = models.PositiveIntegerField(null=True, blank=True)
    submitted = models.BooleanField(default=False)
    last_application_date = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
