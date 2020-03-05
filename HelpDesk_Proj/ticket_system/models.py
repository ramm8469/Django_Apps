from django.db import models
from django.urls import reverse,reverse_lazy

# Create your models here.

class Tickets(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    department = models.CharField(max_length=20)
    priority = models.CharField(max_length=10)
    seat  = models.CharField(max_length=4)
    status = models.IntegerField(default=0)
    # Many to One Mapping ( Many tickets from one User)
    userName = models.ForeignKey('auth.User',on_delete = models.CASCADE)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('Home')


class AcceptedTickets(models.Model):
    acceptedBy = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    ticket = models.ForeignKey(Tickets,on_delete = models.CASCADE)
    

    def __str__(self):
        return '{}'.format(self.ticket.subject)
    
    def get_absolute_url(self):
        return reverse_lazy('AgentHomePage')