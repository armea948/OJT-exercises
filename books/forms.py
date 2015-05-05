from django import forms
from books.models import Book

class ContactForm(forms.Form):
        subject = forms.CharField(max_length=100)
        message = forms.CharField(widget=forms.Textarea)
        sender = forms.EmailField()
        cc_myself = forms.BooleanField(required=False)

class SignUp(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    repeatpwd = forms.CharField(max_length=30, widget=forms.PasswordInput)

class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()

class PublisherForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state_province = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    website = forms.URLField()
    phone = forms.CharField(max_length=20)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
