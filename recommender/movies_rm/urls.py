from . import views
from django.urls import path

urlpatterns = [
    path("<int:id>", views.index, name="index")
]
