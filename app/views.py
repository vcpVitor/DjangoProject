from django.shortcuts import render, redirect
from app.forms import PeluciasForm
from app.models import Pelucia

# Create your views here.
def home(request):
    data = {}
    data['db'] = Pelucia.objects.all()
    return render(request, 'index.html', data)

def cadastro(request):
    data = {}
    data['form'] = PeluciasForm()
    return render(request,'form.html', data)

def create(request):
    form = PeluciasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Pelucia.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Pelucia.objects.get(pk=pk)
    data['form'] = PeluciasForm(instance=data['db'])
    return render(request,'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Pelucia.objects.get(pk=pk)
    form = PeluciasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request,pk):
    db = Pelucia.objects.get(pk=pk)
    db.delete()
    return redirect('home')