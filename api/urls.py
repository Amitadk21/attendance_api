from django.urls import path
from api import views


urlpatterns = [
    path('attendance-api/', views.student_attendance)
]
