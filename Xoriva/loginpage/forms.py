from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Password"}))

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder": "Password"}))