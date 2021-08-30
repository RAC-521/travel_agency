from django.shortcuts import render
from .models import Deal


def index(request):

    deals = Deal.objects.all()

    return render(request, 'index.html', {'deals' : deals})