from django.conf.urls import url
from . import views  # This line is new!

urlpatterns = [
    url(r"^$", views.main),
    url(r"^index/$", views.index, name="index"),
    url(r"^pyth/$", views.pyth, name="pyth"),
    url(r"^sharp/$", views.sharp, name="sharp"),
    url(r"^about/$", views.about, name="about"),
    # This line has changed! Notice that urlpatterns is a list, the comma is in
]  # anticipation of all the routes that will be coming soon

