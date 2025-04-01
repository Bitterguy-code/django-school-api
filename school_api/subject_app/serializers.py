from rest_framework import serializers
from .models import Subject

class subjectSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    grade_average = serializers.SerializerMethodField()
    
    class Meta:
        model = Subject
        fields = ['subject_name','professor','students','grade_average']
        
    def get_students(self, obj):
        return obj.students.count()
    
    def get_grade_average(self, obj):
        grades = obj.grades.all()
        grade_sum = sum([x.grade for x in grades])
        if grade_sum == 0:
            return 0
        else:
            return round(grade_sum/len(grades),2)