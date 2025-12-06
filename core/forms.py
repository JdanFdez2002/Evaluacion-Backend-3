from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BaseRegistroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css_class = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{css_class} form-control".strip()


class EditorRegistroForm(BaseRegistroForm):
    group_name = "Editor"


class LectorRegistroForm(BaseRegistroForm):
    group_name = "Lector Premium"
