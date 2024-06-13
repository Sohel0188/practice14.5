from django.shortcuts import render
from . import forms

# Create your views here.
def first(request):
    form = forms.PracticeForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)   
    return render (request,'index.html',{'form':form})


def formmodel(request):
    #print('hello')
    if request.method == "POST":
        form = forms.Studentform(request.POST)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
           
    else:
        form = forms.Studentform()
    return render (request,'model_form.html', {'form':form})
