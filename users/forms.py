import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Pseudonym, IpiNumber


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class PseudonymCreationForm(forms.ModelForm):
    class Meta:
        model = Pseudonym
        fields = ('name',)


class PseudonymChangeForm(forms.ModelForm):
    class Meta:
        model = Pseudonym
        fields = ('name',)


class IpiNumberCreationForm(forms.ModelForm):
    def clean_number(self):
        """
        Format inputed number if the Base number is missing hyphens
        e.g a1234567890 should be A-123456789-0
        """
        data = self.cleaned_data.get('number')
        if re.search('^[a-zA-Z]\d{10}$', data):
            header = data[:1]
            id_number = data[1:10]
            check_digit = data[-1:]
            data = "{}-{}-{}".format(header, id_number, check_digit)

        return data.upper()

    class Meta:
        model = IpiNumber
        fields = ('number',)
        widgets = {
            'ipi_type': forms.HiddenInput(),
        }
