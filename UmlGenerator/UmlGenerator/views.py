from django.shortcuts import render
from django.http import HttpResponse
from .forms import ClassDiagram

def index(request):
    # def home_view(request):
    if request.method == 'POST':
        form = ClassDiagram(request.POST)
        print(form['className'].value())
        if form.is_valid():
            data = form.cleaned_data
            context ={}
            context['form']= ClassDiagram()
    return render(request, "class.html", context)
