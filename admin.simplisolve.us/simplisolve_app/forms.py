from .models import Contact
from django import forms
import pycountry
import phonenumbers
import locale
from django.contrib.auth.models import User, Permission
from .models import Candidate, Research_scientist, Machine_learning_engineer, Software_application_developer
class PermissionAssignmentForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    permission = forms.ModelChoiceField(queryset=Permission.objects.all())
def get_country_codes():
    country_codes = ['United States +1']
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    sorted_countries = sorted(pycountry.countries, key=lambda c: c.name)
    for country in sorted_countries:
        try:
            country_name = country.name
            country_alpha2 = country.alpha_2
            phone_code = phonenumbers.country_code_for_region(country_alpha2)
            country_codes.append(f"{country_name} +{phone_code}")
        except Exception as e:
            print("not available")
            pass
    locale.setlocale(locale.LC_ALL, '')
    return country_codes

COUNTRY_CODES = get_country_codes()
class CandidateForm(forms.ModelForm):
    country_code = forms.ChoiceField(
        choices=[(code, code) for code in COUNTRY_CODES])

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Add more valid extensions as needed
            valid_extensions = ['.com', '.net', '.org', '.us']
            valid_email = any(email.endswith(ext) for ext in valid_extensions)
            if not valid_email:
                raise forms.ValidationError('Invalid email extension')
        return email

    def clean_phone_number(self):
        country_code = self.cleaned_data.get('country_code')
        code = country_code.split('+')
        phone_number = '+'+code[1] + self.cleaned_data.get('phone_number')
        try:
            parsed_number = phonenumbers.parse(phone_number, country_code)
            if not phonenumbers.is_valid_number(parsed_number):
                raise forms.ValidationError('Invalid phone number')
            else:
                formatted_number = phonenumbers.format_number(
                    parsed_number, phonenumbers.PhoneNumberFormat.E164)
                return formatted_number
        except phonenumbers.NumberParseException:
            if not self.cleaned_data.get('code') or not self.cleaned_data.get('phone_number'):
                return None
            raise forms.ValidationError('Invalid phone number format')
    class Meta:
        model = Candidate
        fields = ['first_name', 'last_name', 'country_code', 'phone_number', 'email', 'resume', 'code', 'salary_exceptation',
                  'experience_fields', 'data_visualization_experience', 'visa_sponsorship', 'predictive_model_experience']

        exclude = []
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        experience_fields = forms.ChoiceField(
            # Use RadioSelect widget to create radio button # Set the initial value for the field
            widget=forms.RadioSelect(),
        )
class Research_scientist_form(forms.ModelForm):
    country_code = forms.ChoiceField(
        choices=[(code, code) for code in COUNTRY_CODES])
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Add more valid extensions as needed
            valid_extensions = ['.com', '.net', '.org', '.us']
            valid_email = any(email.endswith(ext) for ext in valid_extensions)
            if not valid_email:
                raise forms.ValidationError('Invalid email extension')
        return email
    def clean_phone_number(self):
        country_code = self.cleaned_data.get('country_code')
        code = country_code.split('+')
        phone_number = '+'+code[1] + self.cleaned_data.get('phone_number')
        try:
            parsed_number = phonenumbers.parse(phone_number, country_code)
            if not phonenumbers.is_valid_number(parsed_number):
                raise forms.ValidationError('Invalid phone number')
            else:
                formatted_number = phonenumbers.format_number(
                    parsed_number, phonenumbers.PhoneNumberFormat.E164)
                return formatted_number
        except phonenumbers.NumberParseException:
            if not self.cleaned_data.get('code') or not self.cleaned_data.get('phone_number'):
                return None
            raise forms.ValidationError('Invalid phone number format')
    class Meta:
        model = Research_scientist
        fields = ['first_name', 'last_name', 'country_code', 'phone_number', 'email', 'resume', 'code', 'salary_exceptation',
                  'like_working_in_team', 'experience_with_ml_framework', 'research_publications', 'experience_as_research_scientist']
        exclude = ['datetime']
        widgets = {
            'datetime': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
class Software_application_developer_form(forms.ModelForm):
    country_code = forms.ChoiceField(
        choices=[(code, code) for code in COUNTRY_CODES])
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Add more valid extensions as needed
            valid_extensions = ['.com', '.net', '.org', '.us']
            valid_email = any(email.endswith(ext) for ext in valid_extensions)
            if not valid_email:
                raise forms.ValidationError('Invalid email extension')
        return email
    def clean_phone_number(self):
        country_code = self.cleaned_data.get('country_code')
        code = country_code.split('+')
        phone_number = '+'+code[1] + self.cleaned_data.get('phone_number')
        try:
            parsed_number = phonenumbers.parse(phone_number, country_code)
            if not phonenumbers.is_valid_number(parsed_number):
                raise forms.ValidationError('Invalid phone number')
            else:
                formatted_number = phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.E164)
                return formatted_number
        except phonenumbers.NumberParseException:
            if not self.cleaned_data.get('code') or not self.cleaned_data.get('phone_number'):
                return None
            raise forms.ValidationError('Invalid phone number format')
    class Meta:
        model = Software_application_developer
        fields = ['first_name', 'last_name', 'country_code', 'phone_number', 'email', 'resume', 'code', 'salary_exceptation',
                  'project_link', 'software_dev_experience', 'experience_with_sql', 'us_citizen_or_permanent_resident']
        exclude = ['datetime']
        widgets = {
            'datetime': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
class Machine_learning_engineer_form(forms.ModelForm):
    country_code = forms.ChoiceField(
        choices=[(code, code) for code in COUNTRY_CODES])
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Add more valid extensions as needed
            valid_extensions = ['.com', '.net', '.org', '.us']
            valid_email = any(email.endswith(ext) for ext in valid_extensions)
            if not valid_email:
                raise forms.ValidationError('Invalid email extension')
        return email
    def clean_phone_number(self):
        country_code = self.cleaned_data.get('country_code')
        code = country_code.split('+')
        phone_number = '+'+code[1] + self.cleaned_data.get('phone_number')
        try:
            parsed_number = phonenumbers.parse(phone_number, country_code)
            if not phonenumbers.is_valid_number(parsed_number):
                raise forms.ValidationError('Invalid phone number')
            else:
                formatted_number = phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.E164)
                return formatted_number
        except phonenumbers.NumberParseException:
            if not self.cleaned_data.get('code') or not self.cleaned_data.get('phone_number'):
                return None
            raise forms.ValidationError('Invalid phone number format')
    class Meta:
        model = Machine_learning_engineer
        fields = ['first_name', 'last_name', 'country_code', 'phone_number', 'email', 'resume', 'code',
                  'salary_exceptation', 'experience_generative_models', 'experience_ml_pipelines', 'preferred_work_location']
        exclude = ['datetime']
        widgets = {
            'datetime': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
class ContactForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Add more valid extensions as needed
            valid_extensions = ['.com', '.net', '.org', '.us']
            valid_email = any(email.endswith(ext) for ext in valid_extensions)
            if not valid_email:
                raise forms.ValidationError('Invalid email extension')
        return email
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = Contact
        fields = []
