from django.shortcuts import render
from testapp.models import student
from django.http import HttpResponse
from . import form

# Create your views here.
def student_view(request):
    students=student.objects.all()
    return render(request,'testapp/results.html',{'students':students})
def formview(request):
    forms=form.updateForm()
    if request.method=='POST':
        forms=form.updateForm(request.POST)
        if forms.is_valid():
            forms.save(commit=True)
    return render(request,'testapp/form.html',{'forms':forms})
