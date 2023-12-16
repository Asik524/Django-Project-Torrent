from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Comment, Profile
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердить пароль'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Фамилия пользователя'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Почта'
    }))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите комментарий'
            })
        }


class EditAccountForm(UserChangeForm):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class EditProfileForm(forms.ModelForm):
    photo = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Profile
        fields = ['photo', 'phone_number', 'address']
