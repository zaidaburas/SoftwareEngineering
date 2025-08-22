from django.shortcuts import render, redirect, get_object_or_404
from .models import Teachers
from .forms import TeacherForm

def getAll(request):
    teachers = Teachers.objects.all()
    return render(request, "getAll.html", {"teachers": teachers})

def create(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("getAll")
    else:
        form = TeacherForm()
    return render(request, "form.html", {"form": form, "title": "إضافة مدرس"})


def update(request, id):
    teacher = get_object_or_404(Teachers, id=id)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect("getAll")
    else:
        form = TeacherForm(instance=teacher)
    return render(request, "form.html", {"form": form, "title": "تعديل مدرس"})


def delete(request, id):
    teacher = get_object_or_404(Teachers, id=id)
    if request.method == "POST":
        teacher.delete()
        return redirect("getAll")
    return render(request, "delete.html", {"teacher": teacher})
