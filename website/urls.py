from django.urls import path
from website.views import *

urlpatterns = [
    path('' ,home_page ),
    path("introduction/" , introduction),
    path("programers/", programers)
]
