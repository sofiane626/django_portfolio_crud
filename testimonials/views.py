from django.shortcuts import render, redirect
from .models import Testimonials
from .forms import TestimonialsForm

# Create your views here.


def testimonials(request):
    testimonials = Testimonials.objects.all()
    return render(request, 'projet_2/back/testimonials/testimonials.html', {'testimonials': testimonials})


def updateTestimonials(request, id):
    edit = Testimonials.objects.get(id=id)
    if request.method == 'POST':
        form = TestimonialsForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TestimonialsForm(instance=edit)
    return render(request, 'projet_2/back/testimonials/testimonials_edit.html', {'form': form})


def createTestimonials(request):
    if request.method == 'POST':
        form = TestimonialsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TestimonialsForm()
    return render(request, 'projet_2/back/testimonials/testimonials_create.html', {"form": form})


def destroy_Testimonials(request, id):
    destroy = Testimonials(id)
    destroy.delete()
    return redirect('backoffice')
