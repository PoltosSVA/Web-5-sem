from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import RegexValidator
from datetime import date
from django.contrib.auth.models import Group
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(max_length=50, label="First Name")
    last_name = forms.CharField(max_length=50, label="Last Name")
    date_of_birth = forms.DateField(label='Birth date', widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(max_length=200,

                                   validators=[RegexValidator(
                                       regex=r'^(\+375 \(29\) [0-9]{3}-[0-9]{2}-[0-9]{2})$',
                                       message='Format +375 (29) XXX-XX-XX')
                                   ], label="Phone number")


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'phone_number', 'password1', 'password2', 'date_of_birth'
        ]

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            today = date.today()
            age = today.year - date_of_birth.year - (
                        (today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            if age < 18:
                raise forms.ValidationError("You must be at least 18 years old to register.")
        return date_of_birth


    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.date_of_birth = self.cleaned_data['date_of_birth']

        if commit:
            user.save()
            # Получаем или создаем группу "Customer"
            customer_group, created = Group.objects.get_or_create(name='Customer')
            # Присваиваем пользователя к группе "Customer"
            user.groups.add(customer_group)

        return user
