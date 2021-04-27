from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image', 'country', 'gender', 'date_of_birth')
    
    def form_valid(self, form):
        form.instance.user = ProfileForm.objects.get(user=self.request.user)
        form.instance.created_by = self.request.user
        return super(ProfileForm, self).form_valid(form)