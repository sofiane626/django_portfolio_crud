from django.shortcuts import render, redirect
from .models import About
from .forms import AboutForm

# Create your views here.


def update(request):
    edit = About.objects.get(id=1)
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AboutForm(instance=edit)
    return render(request, 'projet_2/back/about/about_edit.html', {'form': form})
