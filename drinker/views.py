from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from drinker.forms import RegistrationForm, LoginForm
from drinker.models import Drinker
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def DrinkerRegistration(request):
	#If user is already signed in redirect him to profile page
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')	
	#If user is not signed in and the submit button was hit then post the form
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
		# if form is valid create the form
        if form.is_valid():		    
            user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            user.save()
            drinker = user.get_profile()  
            drinker.name = form.cleaned_data['name']
            drinker.birthday = form.cleaned_data['birthday']
            drinker.save()  
#            drinker = Drinker(user=user, name=form.cleaned_data['name'], birthday=form.cleaned_data['birthday'])	
#            drinker.save()			
            return HttpResponseRedirect('/profile/')
		# If user was not signed and form was posted but form was not valid return the form with validation issues
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))		
    else:
		# If user is not signed in return the form
        '''	user is not submitting the form, show them a blank registration form'''
        form = RegistrationForm()
        context = {'form': form,}
        return render_to_response('register.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']	
            drinker = authenticate(username=username, password=password)
            if drinker is not None:
                login(request, drinker)
                return HttpResponseRedirect('/profile/')
            else:
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))		
    else:
        ''' user is not submitting the form, show the login form '''	
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request)) 	 	

def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')		