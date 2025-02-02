from django.urls import path
from . import views

urlpatterns = [
    path("main", views.main_page, name="vals-main"),
    path("main/<str:id>", views.main_detail, name="vals-detail")
]