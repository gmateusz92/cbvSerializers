from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import Response, status
from rest_framework import status
from rest_framework import APIView
from django.http import Http404

class StudentList(APIView):

    def get(request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)    
