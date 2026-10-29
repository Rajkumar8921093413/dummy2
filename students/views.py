from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json
# Create your views here.
def get_student_info(request):
    students = Student.objects.all()
    student_list = []
    for student in students:
        student_list.append({
            "id" : student.student_id,
            "name": student.name,
            "age": student.age,
            "gender": student.gender,
            "course": student.course,
        })
    return JsonResponse({"status":"success","data":student_list})


@csrf_exempt
def create_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        student = Student.objects.create(
            name=data['name'],
            age=data['age'],
            gender=data['gender'],
            course=data['course']
        )
        return JsonResponse({
            "status": "success",
            "data": {
                "id": student.student_id,
                "name": student.name,
                "age": student.age,
                "gender": student.gender,
                "course": student.course,
            }
        })
    return JsonResponse({"status":"error","data":"Invalid request"})


def get_student_by_id(request, id=None):
    student_id = id or request.GET.get('id')
    if not student_id:
        return JsonResponse({"status": "error", "message": "Student ID is required"}, status=400)

    try:
        student = Student.objects.get(pk=student_id)
        return JsonResponse({
            "status": "success",
            "data": {
                "id": student.student_id,
                "name": student.name,
                "age": student.age,
                "gender": student.gender,
                "course": student.course,
            }
        })
    except Student.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Student not found"}, status=404)