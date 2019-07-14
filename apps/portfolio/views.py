from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import View

from portfolioproject.utils import render_to_pdf


def main(req):
    return redirect("portfolio:home")


def home(req):
    return render(req, "portfolio/home.html")


def python(req):
    return render(req, "portfolio/python.html")


def csharp(req):
    return render(req, "portfolio/csharp.html")


def about(req):
    return render(req, "portfolio/about.html")


def contact(req):
    return redirect("portfolio/about/Pdf")


def Pdf(request, *args, **kwargs):
    pdf = render_to_pdf("portfolio/resume.html")
    if pdf:
        response = HttpResponse(pdf, content_type="application/pdf")
        filename = "resume_%s.pdf" % ("Elvis_Makia")
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        response["Content-Disposition"] = content
        return response
    return HttpResponse("Not found")


def wishmaker(req):
    return redirect("https://github.com/poferri/wishmaker.git")


def wishmakersite(req):
    return redirect("http://18.217.90.11/")


def quotedash(req):
    return redirect("https://github.com/poferri/quote_dash.git")


def quotedashsite(req):
    return redirect("http://52.14.128.79/")


def clakkle(req):
    return redirect("https://github.com/poferri/clakkle.git")


def clakklesite(req):
    return redirect("http://3.14.136.63/")


def weddingplanner(req):
    return redirect("https://github.com/poferri/WeddingPlanner.git")


def weddingplannersite(req):
    return redirect("http://18.222.165.8/")


def healthwall(req):
    return redirect("https://github.com/poferri/secrets.git")


def healthwallsite(req):
    return redirect("http://18.220.54.169/")


def linkedIn(req):
    return redirect("https://www.linkedin.com/in/elvismakia/")

