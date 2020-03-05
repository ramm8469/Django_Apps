from django.contrib import admin
from .models import Tickets,AcceptedTickets

# Register your models here.
admin.site.register(Tickets)
admin.site.register(AcceptedTickets)

