from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import re


def index(request):
    template = loader.get_template("form/form.html")
    return HttpResponse(template.render())


@csrf_exempt
def email(request):
    regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b")
    email: str = request.POST.get("email")

    valid = True
    context = {"email": email}

    if type(email) == str:
        if not re.fullmatch(regex, email) or not email:
            valid = False
            context.update({"error": "Invalid email address."})
        if email == "example@example.com":
            valid = False
            context.update({"error": "Email address already exists."})

    template = "form/email/valid.html" if valid else "form/email/invalid.html"

    return render(request, template, context)


@csrf_exempt
def phone(request):
    regex = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
    phone: str = request.POST.get("phone")

    valid = True
    context = {"phone": phone}

    if type(phone) == str:
        if not re.fullmatch(regex, phone) or not phone:
            valid = False
            context.update({"error": "Invalid phone number."})

    template = "form/phone/valid.html" if valid else "form/phone/invalid.html"

    print(context)
    return render(request, template, context)
