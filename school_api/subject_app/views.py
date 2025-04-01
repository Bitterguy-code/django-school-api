from django.shortcuts import render
from .models import Subject
from .serializers import subjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class all_subjects(APIView):
    def get(self, request):
        subject = subjectSerializer(Subject.objects.order_by('subject_name'), many=True)
        
        return Response(subject.data)
