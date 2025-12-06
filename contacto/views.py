import logging
from smtplib import SMTPDataError

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ContactForm

logger = logging.getLogger(__name__)


def contacto(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            correo = form.cleaned_data["correo"]
            mensaje = form.cleaned_data["mensaje"]

            asunto = f"Mensaje de contacto de {nombre}"
            cuerpo = (
                f"Nombre: {nombre}\n"
                f"Correo: {correo}\n\n"
                f"Mensaje:\n{mensaje}"
            )

            try:
                send_mail(
                    subject=asunto,
                    message=cuerpo,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
            except SMTPDataError:
                form.add_error(None, "Se alcanzó el límite de envíos. Espera unos segundos y vuelve a intentarlo.")
            except Exception:
                logger.exception("Error al enviar correo de contacto")
                form.add_error(None, "No se pudo enviar el mensaje. Intentalo nuevamente en unos minutos.")
            else:
                return redirect(reverse("contacto:exito"))
    else:
        form = ContactForm()

    return render(request, "contacto/contacto.html", {"form": form})


def contacto_exito(request):
    return render(request, "contacto/contacto_exito.html")
