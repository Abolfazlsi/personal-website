from django.shortcuts import render
from resume_app.models import Project
from contactus_app.models import Footer, Info, Message


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        content = request.POST.get("content")
        email = request.POST.get("email")
        body = request.POST.get("body")

        Message.objects.create(name=name, content=content, email=email, body=body)

    projects = Project.objects.all()
    footer = Footer.objects.all().last()
    info = Info.objects.all().last()

    context = {
        "projects": projects,
        "footer": footer,
        "info": info,

    }
    return render(request, "index.html", context)
