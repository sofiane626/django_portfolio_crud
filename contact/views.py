from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.


def Contactupdate(request):
    edit = Contact.objects.get(id=1)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=edit)
    return render(request, 'projet_2/back/contact/contact_edit.html', {'form': form})
