from typing import Any
from django import forms
from django.core import validators
from django.forms.widgets import NumberInput
from .models import Student

class PracticeForm(forms.Form):
    name = forms.CharField(label="Enter Your Name",validators=[validators.MinLengthValidator(10, message='Enter a name with at least 10 characters')])
    
   
    email = forms.EmailField(label='Enter Your Email')
   
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows' : 3, 'id' : 'testId'}))
    
    number = forms.IntegerField(label='What is your number')
    
    FAVORITE_COLOR = [
        ('blue',  'Blue'),
        ('blue',  'Green'),
        ('blue',  'Blue'),
    ]
    
    color = forms.ChoiceField(choices=FAVORITE_COLOR)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLOR)
    # favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLOR)
    multiChole = forms.MultipleChoiceField(choices=FAVORITE_COLOR)
    multiChole2 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLOR)
    agree = forms.BooleanField(initial=True)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    captcha_answer = forms.IntegerField(label="2 + 2", label_suffix=" =")
    

class Studentform(forms.ModelForm):
    class Meta :
        model = Student
        fields ='__all__'
        