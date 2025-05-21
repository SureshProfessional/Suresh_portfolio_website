from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['main_photo', 'name', 'description', 'main_project', 'add_resume']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Har field ko required=True kar do (by default hota hai, ye explicit hai)
        for field in self.fields.values():
            field.required = True

    def clean(self):
        cleaned_data = super().clean()

        for field in self.fields:
            value = cleaned_data.get(field)
            old_value = getattr(self.instance, field)

            # Agar value blank hai (None, '', False, ya empty)
            if not value:
                # Aur purani value bhi exist karti ho (None nahi)
                if old_value:
                    cleaned_data[field] = old_value

        return cleaned_data
