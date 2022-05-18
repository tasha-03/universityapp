from django import forms
from admissioncommittee.models import Course
from userprofile.models import User


class UserForm(forms.Form):
    full_name = forms.CharField(label="Полное имя")
    course = forms.ChoiceField(choices=[(
        course.id, course.code) for course in Course.objects.all()], label="Выбранный курс")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    required_css_class = "field"
    error_css_class = "error"


class AnketaForm(forms.Form):
    user = forms.ChoiceField(label="Пользователь", choices=[(
        user.id, user.full_name) for user in User.objects.all()])
    address = forms.CharField(max_length=50)
    birthday = forms.DateField(label="День рождения", widget=forms.DateInput())
