from django.shortcuts import render,redirect
from .models import Portfolio,PortfolioFiltre
from .forms import PortfolioForm, FiltreForm
# Create your views here.


def getPortfolio(request):
    portfolio = Portfolio.objects.all()
    portfolioFiltre = PortfolioFiltre.objects.all()
    return render(request, 'projet_2/back/portfolio/portfolio.html', {'portfolio': portfolio, 'portfolioFiltre': portfolioFiltre})


def updateFiltre(request):
    edit = PortfolioFiltre.objects.get(id=1)
    if request.method == 'POST':
        form = FiltreForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FiltreForm(instance=edit)
    return render(request, 'projet_2/back/portfolio/portfolio_edit.html', {'form': form})


def updatePortfolio(request, id):
    edit = Portfolio.objects.get(id=id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PortfolioForm(instance=edit)
    return render(request, 'projet_2/back/portfolio/portfolio_edit.html', {'form': form})


def createFiltre(request):
    if request.method == 'POST':
        form = FiltreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FiltreForm()
    return render(request, 'projet_2/back/portfolio/portfolio_edit.html', {"form": form})


def createPortfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PortfolioForm()
    return render(request, 'projet_2/back/portfolio/portfolio_edit.html', {"form": form})


def destroyFiltre(request, id):
    destroy = PortfolioFiltre(id)
    destroy.delete()
    return redirect('backoffice')


def destroyPortfolio(request, id):
    destroy = Portfolio(id)
    destroy.delete()
    return redirect('backoffice')
