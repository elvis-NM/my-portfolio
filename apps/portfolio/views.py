from django.shortcuts import render, redirect, HttpResponse

# the index function is called when root is visited


def main(req):
    return render(req, "portfolio/consulting.html")


def index(req):
    return render(req, "portfolio/consulting.html")


def pyth(req):
    return render(req, "portfolio/python.html")


def sharp(req):
    return render(req, "portfolio/aspnet.html")


def about(req):
    return render(req, "portfolio/about.html")
