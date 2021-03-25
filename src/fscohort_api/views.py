import re
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework import mixins
from rest_framework.fields import SerializerMethodField
from rest_framework.views import APIView
from fscohort.models import Student
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import generics

def home_api(request):
    data = {
        "name":"henry",
        "adress":"clarusway.com",
        "skills": ["python", "django"]
    }
    return JsonResponse(data)

# def student_list_api(request):
#     if request.method == "GET":
#         students = Student.objects.all()
#         student_count = Student.objects.count()
        
#         student_list = []
#         for student in students:
#             student_list.append({
#                 "firstname": student.first_name,
#                 "lastname": student.last_name,
#                 "number": student.number,
#             })
        
#         data = {
#             "students": student_list,
#             "count": student_count,
#         }
#         return JsonResponse(data)

# def student_list_api(request):
#     if request.method == "GET":
#         students = Student.objects.all()
#         student_count = Student.objects.count()
#         student_data = serialize("python", students)
#         data = {
#             "students": student_data,
#             "count": student_count,
#         }
#         return JsonResponse(data)

# @csrf_exempt
# def student_create_api(request):
#     if request.method == "POST":
#         post_body = json.loads(request.body)
        
#         name = post_body.get("first_name")
#         lastname = post_body.get("last_name")
#         number = post_body.get("number")
        
#         student_data = {
#             "first_name": name,
#             "last_name": lastname,
#             "number": number
#         }
        
#         student_obj = Student.objects.create(**student_data)
        
#         data = {
#             "message": f"Student {student_obj.first_name} created successfully!"
#         }
#         return JsonResponse(data, status=201)

# @api_view(["GET", "POST"])
# def student_list_create_api(request):
#     if request.method == "GET":
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": "Student created successfully!"
#             }
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status)
    
    
# @api_view(["GET", "PUT", "DELETE"])
# def student_get_update_delete_api(request, id):
#     student = get_object_or_404(Student, id=id)
    
#     if request.method == "GET":
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
        
#     elif request.method == "PUT":
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": "Student updated successfully"
#             }
#             return Response(data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# This can be written in class based views:
# class StudentList(APIView):
    
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class StudentGetUpdateDelete(APIView):
    
#     def get_object(self, id):
#         try:
#             return Student.objects.get(id=id)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#     def get(self, request, id):
#         student = self.get_object(id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         student = self.get_object(id)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": "Student updated"
#             }
#             return Response(data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         student = self.get_object(id)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class StudentList(generics.ListAPIView):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()
    
# class StudentListCreate(generics.ListCreateAPIView):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()
    
# class StudentGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()
#     lookup_field = 'id'

class Student(generics.GenericAPIView, 
              mixins.ListModelMixin, 
              mixins.CreateModelMixin, 
              mixins.UpdateModelMixin, 
              mixins.RetrieveModelMixin, 
              mixins.DestroyModelMixin):
    
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'
    
    def get(self, request, id):
        if id:
            return self.retrieve(request)
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id):
        return  self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)