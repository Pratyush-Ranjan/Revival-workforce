from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django import forms
from .forms import UserRegistrationForm, CompanyRequirementForm
from .models import Company
# Create your views here.
def start(request):
    return render(request, 'accounts/home.html')
def signup_view(request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/home")
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                userObj = form.cleaned_data
                username = userObj['username']
                email =  userObj['email']
                password =  userObj['password']
                if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    User.objects.create_user(username, email, password)
                    user = authenticate(username = username, password = password)
                    login(request, user)
                    return HttpResponseRedirect("/home")
                else:
                    raise forms.ValidationError('Looks like a user with that email or username already exists')
        else:
            form = UserRegistrationForm()
        return render(request, 'accounts/signup.html', {'user_form' : form})
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

class CreateJob(CreateView):
    #python method corresponding to a get request
    def get(self, request, *args, **kwargs):
        context = {'cform': CompanyRequirementForm()}
        return render(request, 'accounts/jobadd.html', context)
    def post(self, request, *args, **kwargs):
        context = {'cform': CompanyRequirementForm()}
        form = CompanyRequirementForm(request.POST)
        if form.is_valid():
            company = Company()
            company.Name = request.POST.get('Name')
            company.Companyname = request.POST.get('Companyname')
            company.Phone_no = request.POST.get('Phone_no')
            company.Address = request.POST.get('Address')
            company.Industry_type = request.POST.get('Industry_type')
            company.Skill_required = request.POST.get('Skill_required')
            company.save()
            return render(request, 'accounts/jobadd.html', context)
        else:
            return render(request, 'accounts/jobadd.html', {'cform': form})