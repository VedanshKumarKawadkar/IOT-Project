from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("login_email")
        password = self.cleaned_data.get("login_password")

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise forms.ValidationError("User Not Found")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("User Not Active")
        
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserSignupForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField(label="Email Address")
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model =  User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get("signup_email")
        username = self.cleaned_data.get("signup_username")
        pass1 = self.cleaned_data.get("signup_password")
        pass2 = self.cleaned_data.get("signup_password_confirm")

        if pass1 != pass2:
            raise forms.ValidationError("Passwords do not match.")
        
        email_qs = User.objects.filter(email=email)
        user_qs = User.objects.filter(username=username)

        if email_qs.exists():
            raise forms.ValidationError("Email Already Exists")
        if user_qs.exists():
            raise forms.ValidationError("UserName already exists")
        return email