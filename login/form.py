from django import forms

class loginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input100'}), label="email", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input100'}))
    widgets = {
        'password': forms.PasswordInput(),
    }