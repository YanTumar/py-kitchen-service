from django import forms
from django.contrib.auth import get_user_model

class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "years_of_experience"]
