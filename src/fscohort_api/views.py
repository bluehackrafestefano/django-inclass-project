import re
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from fscohort.models import Student
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status

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

@api_view(["GET", "POST"])
def student_list_create_api(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Student created successfully!"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status)
    
    
@api_view(["GET", "PUT", "DELETE"])
def student_get_update_delete_api(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)
        
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Student updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)