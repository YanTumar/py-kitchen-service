from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from kitchen.models import Dish


class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "years_of_experience"]

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data.get("years_of_experience")
        if years_of_experience is not None and years_of_experience > 50:
            raise ValidationError("Experience should be less than or equal to 50 years.")

        return years_of_experience


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username..."})
    )
