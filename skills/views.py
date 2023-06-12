from django.shortcuts import render, redirect
from .models import Skills, Skills_bar
from .forms import SkillsForm,Skills_barForm

# Create your views here.


def skills(request):
    skills_bar = Skills_bar.objects.all()
    return render(request, 'projet_2/back/skills/skills.html', {'skills_bar': skills_bar})



def updateSkills(request):
    edit = Skills.objects.get(id=1)
    if request.method == 'POST':
        form = SkillsForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SkillsForm(instance=edit)
    return render(request, 'projet_2/back/skills/skills_edit.html', {'form': form})


def updateSkills_bar(request, id):
    edit = Skills_bar.objects.get(id=id)
    if request.method == 'POST':
        form = Skills_barForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Skills_barForm(instance=edit)
    return render(request, 'projet_2/back/skills/skills_edit.html', {'form': form})


def createSkills_bar(request):
    if request.method == 'POST':
        form = Skills_barForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Skills_barForm()
    return render(request, 'projet_2/back/skills/skills_edit.html', {"form": form})


def destroy_Skills(request, id):
    destroy = Skills_bar(id)
    destroy.delete()
    return redirect('backoffice')
