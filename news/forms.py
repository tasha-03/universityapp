from django import forms
from django.core.exceptions import ValidationError


class NewsForm(forms.Form):
    title = forms.CharField(label="Заголовок", required=False)
    date = forms.DateField(label="Дата публикации",
                           required=False, widget=forms.DateInput())
    text = forms.CharField(widget=forms.Textarea(),
                           min_length=8, max_length=1024, label="Текст")
    rating = forms.FloatField()

    def clean_rating(self):
        rating = self.cleaned_data["rating"]

        if rating < 0 or rating > 10:
            raise ValidationError(
                "Некорректное значение - рейтинг может ринимать значения от 0 до 10")

        return rating

    def clean(self):
        super().clean()
        title = self.cleaned_data.get("title")
        date = self.cleaned_data.get("date")
        if not title:
            if not date:
                raise ValidationError(
                    "Требуется заголовок или дата публикации")

    required_css_class = "field"
    error_css_class = "error"
