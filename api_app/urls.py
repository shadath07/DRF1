from django.urls import path
from . import views

urlpatterns = [
    path('student_details/<int:pk>', views.student_details, name = 'student_details'),
    path('student_list/',views.student_list, name = "student_list"),
]