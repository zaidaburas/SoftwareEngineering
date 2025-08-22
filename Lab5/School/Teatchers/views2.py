from django.shortcuts import render, redirect, get_object_or_404
from .models import Teachers
from .pythonForm import TeacherForm


def create(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Teachers.objects.create(
                name=data["name"],
                experience_years=data["experience_years"],
                salary=data["salary"],
                notes=data["notes"],
                is_active=data["is_active"],
                hire_date=data["hire_date"],
                start_time=data["start_time"],
            )
            return redirect("getAll")
    else:
        form = TeacherForm()
    return render(request, "form.html", {"form": form, "title": "إضافة مدرس"})

def update(request, id):
    teacher = get_object_or_404(Teachers, id=id)
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            teacher.name = data["name"]
            teacher.experience_years = data["experience_years"]
            teacher.salary = data["salary"]
            teacher.notes = data["notes"]
            teacher.is_active = data["is_active"]
            teacher.hire_date = data["hire_date"]
            teacher.start_time = data["start_time"]
            teacher.save()
            return redirect("getAll")
    else:
        form = TeacherForm(initial={
            "name": teacher.name,
            "experience_years": teacher.experience_years,
            "salary": teacher.salary,
            "notes": teacher.notes,
            "is_active": teacher.is_active,
            "hire_date": teacher.hire_date,
            "start_time": teacher.start_time,
        })
    return render(request, "form.html", {"form": form, "title": "تعديل مدرس"})
