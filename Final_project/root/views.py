from django.shortcuts import render
from tutor.models import Tutor


# Create your views here.
def root(request):
    d = Tutor.objects.all()
    dict = {'d':d}
    return render(request, 'index.html', dict)
