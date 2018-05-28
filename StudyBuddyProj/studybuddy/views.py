from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, StudyGroup, ChatMessage, StudyGroupForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect


# Create your views here.

# This page will display ALL the groups and serve as a notice board of some sorts
@login_required(login_url='/login/')
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    studygroups_list = StudyGroup.objects.all()
    paginator = Paginator(studygroups_list, 20)

    page = request.GET.get('page');
    studygroups = paginator.get_page(page)
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'studybuddy/index.html',
        context={'studygroups':studygroups},   
)


class StudentSignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True, help_text='Your First Name.')
	last_name = forms.CharField(max_length=30, required=True, help_text='Your Last Name.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


def signup(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		form = StudentSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/')
	else:
		form = StudentSignUpForm()
	return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='/login/')
def creategroup(request):
	if request.method == 'POST':
		form = StudyGroupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = StudyGroupForm()
	return render(request, 'studybuddy/creategroup.html', {'form': form})
 

@login_required(login_url='/login/')
def updategroup_am(request, id):
	instance = StudyGroup.objects.get(id=id)
	sg_vars = StudyGroup.objects.values().get(id=id)
	form = StudyGroupForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request, 'studybuddy/updategroup_am.html', {'form': form})

@login_required(login_url='/login/')
def updategroup_delete(request, pk, template_name='studybuddy/updategroup_delete_confirm.html'):
	instance = get_object_or_404(StudyGroup, pk=pk)
	if request.method == "POST":
		instance.delete()
		return HttpResponseRedirect('/')
	return render(request, template_name, {'object': instance})



# This page will display the groups that the user is a part of
# def mygroups(request)

# def login(request):
