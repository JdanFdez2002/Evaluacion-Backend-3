from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label="Nombre",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Tu nombre",
        }),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "tu@email.com",
        }),
    )
    asunto = forms.CharField(
        max_length=150,
        label="Asunto",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Asunto del mensaje",
        }),
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 5,
            "placeholder": "Cuéntanos en qué te ayudamos",
        }),
    )

