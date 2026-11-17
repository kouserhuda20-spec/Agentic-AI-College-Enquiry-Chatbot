
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("chatbot/", views.index, name="chatbot"),
    path("chatbot/", views.index, name="index"),
    path("chat-api/", views.chat_api, name="chat_api"),
    path("reports/", views.reports, name="reports"),
    path("reports/export/", views.export_college_csv, name="export_college_csv"),
]
