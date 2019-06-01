from django import forms

class bookingForm(forms.Form):
    CHOICES = (
        ('Interior and Exterior', 'Interior and Exterior'),
        ('Interior Only', 'Interior Only'),
        ('Exterior Only', 'Exterior Only'),
    )
    #name = forms.CharField(label="name", max_length=100)
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter your email address'}), label="email", max_length=100 )
    address = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter your address'}), label="address", max_length=100)
    date = forms.DateField(label="Date", widget=forms.DateInput(attrs={'class': 'form-control', 'type' : 'date'}))
    service = forms.CharField(widget=forms.Select(attrs={'class' : 'form-control'},choices=CHOICES))