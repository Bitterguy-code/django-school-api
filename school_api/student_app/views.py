from django.shortcuts import render
from .models import Student, Subject
from .serializers import StudentAllSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class all_students(APIView):
    
    def get(self, request):
        student = StudentAllSerializer(Student.objects.order_by('name'), many=True)
        
        return Response(student.data)
        
class A_student(APIView):
    
    def get(self,request,id):
        student = None
        if type(id):
            student = Student.objects.get(id = id)
        else:
            student = Student.objects.get(name = id.title())
            
        return Response(StudentAllSerializer(student).data)