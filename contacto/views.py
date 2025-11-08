from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm


def contacto(request):
    enviado = request.GET.get('ok') is not None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect(f"{reverse('contacto:contacto')}?ok")
    else:
        form = ContactForm()

    return render(request, 'contacto/contacto.html', {"form": form, "enviado": enviado})
