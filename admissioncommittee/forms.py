from django import forms


class CourseForm(forms.Form):
    code = forms.CharField(max_length=5, label="Код курса (например, G1900)")
    cathedra = forms.ChoiceField(choices=(
        ("1", "Gryffindor"), ("2", "Hufflepuff"), ("3", "Ravenclaw"), ("4", "Slytherin")), label="Кафедра")
    required_css_class = "field"
    error_css_class = "error"
