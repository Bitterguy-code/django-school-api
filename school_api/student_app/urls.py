from django.urls import path
from .views import all_students

urlpatterns = [
    path('students/', all_students.as_view(), name='all_students')
]