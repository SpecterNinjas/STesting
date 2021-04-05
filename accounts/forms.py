from django import forms
from django.core.exceptions import ValidationError
from .models import ProfileCreation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        labels = {
            'username': _('Login'),
            'password1': _('Parol'),
            'password2': _('Tasdiqlang'),
        }
        # labels = {
        #     'fullname': 'Ism va familiya',
        #     'login': 'Login',
        #     'phone': 'Telefon raqam',
        #     'area': 'Hudud',
        #     'city': 'Shahar/tuman',
        #     'school': 'Maktab',
        #     'grade': 'Sinf',
        # }

    # def clean_fullname(self):
    #     fullname = self.cleaned_data.get("fullname").strip()
    #     if ' ' not in fullname:
    #         raise forms.ValidationError("Iltimos to'liq ism va familiyangizni kiriting.")
    #     return fullname
    #
    # def clean_phone(self):
    #     phone = self.cleaned_data.get("phone")
    #     if ('+' not in phone[0]) or (len(phone) != 13):
    #         raise forms.ValidationError("Iltimos telefon raqamingizni to'liq kiriting. Masalan: +998906367357")
    #     return phone
    #
    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Tasdiqlash uchun bir xil parolni kiriting.")
    #     return password2


class ProfileDetailForm(forms.ModelForm):
    class Meta:
        model = ProfileCreation
        fields = ['fullname', 'phone', 'area', 'city', 'school', 'grade']
        labels = {
            'fullname': _('Ism va familiya'),
            'phone': _('Telefon raqam'),
            'area': _('Hudud'),
            'city': _('Shahar/tuman'),
            'school': _('Maktab'),
            'grade': _('Sinf'),
        }
