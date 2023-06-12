from django.shortcuts import render, redirect
from .models import Services
from .forms import ServicesForm

# Create your views here.


def services(request):
    services = Services.objects.all()
    return render(request, 'projet_2/back/services/services.html', {'services': services})


def updateServices(request,id):
    edit = Services.objects.get(id=id)
    if request.method == 'POST':
        form = ServicesForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ServicesForm(instance=edit)
    return render(request, 'projet_2/back/services/services_edit.html', {'form': form})


def createServices(request):
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ServicesForm()
    return render(request, 'projet_2/back/services/services_create.html', {"form": form})


def destroy_Services(request, id):
    destroy = Services(id)
    destroy.delete()
    return redirect('backoffice')
