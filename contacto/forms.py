from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label="Nombre",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Tu nombre",
            }
        ),
    )
    correo = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "tu@correo.com",
            }
        ),
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Cuéntanos en qué te ayudamos",
            }
        ),
    )
