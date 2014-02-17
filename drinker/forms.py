from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from drinker.models import Drinker

class RegistrationForm(ModelForm):
    username = forms.CharField(label=u'User Name')
    email = forms.EmailField(label=u'Email Address')
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
	
    class Meta:
        model = Drinker
        exclude = ('user',)	

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That username is already take, please select another")			
		
    def clean_password(self): 	
        #cleaned_data = super(RegistrationForm, self).clean()
        if self.data['password'] != self.data['password1']:
            raise forms.ValidationError("The passwords did not match. Please try again.")
        else:	
            return self.data['password']
			
class LoginForm(forms.Form):
    username = forms.CharField(label=(u'User Name'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
	
	
			
		