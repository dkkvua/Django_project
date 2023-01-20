import django_tables2 as tables
from .models import Shtat

class ShtatTable(tables.Table):
    class Meta:
        model = Shtat
        # add class="paleblue" to <table> tag
        exclude = ("id", )
        attrs = {'class': 'hover'}
        #sequence = ('posad_nomer', 'first_name', 'last_name')