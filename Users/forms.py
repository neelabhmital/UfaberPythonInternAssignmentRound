from django import forms
from django.contrib.auth import get_user_model

#retrieving the current user model
user = get_user_model()
class UserRegistration(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = [
                    "username",
                    "email",
                    "password",
                    "confirm_password"
                 ]

    def clean_confirm_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return confirm_password

    def clean_email(self, *args, **kwargs):
        inp_email = self.cleaned_data.get("email")
        qs = user.objects.filter(email=inp_email)
        if qs.exists():
            raise forms.ValidationError("Email already taken")

        return inp_email

class UserLogin(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = [
                    "username",
                    "password"
                 ]