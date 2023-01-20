from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Shtat, Soldier, Zvannya
from .tables import ShtatTable

def index(request):
    return render(request, "index.html")

def shtat(request):

    #shtat = Shtat.objects.all().select_related('soldier__soldier_zvannya')
    shtat = Shtat.objects.select_related('soldier__soldier_zvannya').all()

    table = ShtatTable(shtat)
    #table = ShtatTable(Shtat.objects.all())

    RequestConfig(request).configure(table)
    return render(request, 'main_table.html', {'table': table})