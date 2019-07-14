from django.conf.urls import url
from django.contrib import admin
from . import views  # This line is new!
from .views import Pdf
from .views import wishmaker

urlpatterns = [
    url(r"^$", views.main),
    url(r"^home/$", views.home, name="home"),
    url(r"^python/$", views.python, name="python"),
    url(r"^csharp/$", views.csharp, name="csharp"),
    url(r"^about/$", views.about, name="about"),
    url(r"^about/Pdf/$", views.Pdf, name="Pdf"),
    url(r"^wishmaker/$", views.wishmaker, name="wishmaker"),
    url(r"^wishmakersite/$", views.wishmakersite, name="wishmakersite"),
    url(r"^quotedash/$", views.quotedash, name="quotedash"),
    url(r"^quotedashsite/$", views.quotedashsite, name="quotedashsite"),
    url(r"^contact/$", views.contact, name="contact"),
    url(r"^clakkle/$", views.clakkle, name="clakkle"),
    url(r"^weddingplanner/$", views.weddingplanner, name="weddingplanner"),
    url(r"^weddingplannersite/$", views.weddingplannersite, name="weddingplannersite"),
    url(r"^healthwall/$", views.healthwall, name="healthwall"),
    url(r"^healthwallsite/$", views.healthwallsite, name="healthwallsite"),
    url(r"^linkedIn/$", views.linkedIn, name="linkedIn"),
    # This line has changed! Notice that urlpatterns is a list, the comma is in
]  # anticipation of all the routes that will be coming soon

