from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tickets,AcceptedTickets
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .forms import CreateTicketForm
# For Agents...



class LandingPageView(TemplateView):
    template_name = 'index.html'
    

class HomePageView(LoginRequiredMixin,ListView):
    print("HomePageView")
    
    def get(self, request):
        if request.user.is_staff :
            # uid = request.user.id
            # print("\n","#"*50,'\n',uid,"\n")
            context_data = {'unaccepted_tickets':Tickets.objects.all(),'accepted_tickets':AcceptedTickets.objects.filter(acceptedBy_id = request.user.id)}
            return render(request,'agent_dashboard.html',context_data)
        else:
            context_data = {'tickets':Tickets.objects.filter(userName_id = request.user.id)}
            return render(request,'home.html',context_data)

   

    
    # queryset = 
    def get_queryset(self):
       return Tickets.objects.filter(userName = self.request.user)

class AboutPageView(TemplateView):
    template_name = 'about.html'

class CreateTicketView(LoginRequiredMixin,CreateView):
    # form_class = CreateTicketForm
    model = Tickets
    template_name = 'create_ticket.html'
    fields = ['subject','description','department','priority','seat']

    def form_valid(self, form):
        form.instance.userName = self.request.user
        return super().form_valid(form)

class UpdateTicketView(LoginRequiredMixin,UpdateView):
    model = Tickets
    template_name = 'update_ticket.html'
    fields = ['subject','description','department','priority','seat']

class DeleteTicketView(LoginRequiredMixin,DeleteView):
    model = Tickets
    template_name = 'delete_ticket.html'
    success_url = reverse_lazy('Home')


# For Agents

class AgentHomePageView(LoginRequiredMixin,ListView):
    def get(self,request):
        context_data = {'unaccepted_tickets':Tickets.objects.all(),'accepted_tickets':AcceptedTickets.objects.filter(acceptedBy_id = request.user.id)}
        return render(request,'agent_dashboard.html',context_data)


class TicketsAcceptedView(LoginRequiredMixin,CreateView):
    def get(self,request):
        #1 For updating the ticket status

        if 'ticketId' in request.GET:
            # print("In Ticket Id --- ",request.GET['ticketId'],'--- ',type(request.GET['ticketId']))
            for each in Tickets.objects.filter(id = int(request.GET['ticketId'])):
                # print(each.subject,each.id,each.status)
                # updating the status
                each.status = 2
                each.save()
        else:
            print("Didn't get ticket id")


        #2 For Updating ticket updates to the accepted_ticket table
        # accepted_ticket_obj = AcceptedTickets.objects.create(acceptedBy_id = request.user.id,ticket_id = int(request.GET['ticketId']) ) 
        # accepted_ticket_obj.save() 
        context_data = {'unaccepted_tickets':Tickets.objects.filter(userName_id = request.user.id),'accepted_tickets':AcceptedTickets.objects.filter(acceptedBy_id = request.user.id)}

        return render(request,'agent_dashboard.html',context_data)
    
class TicketResolvedView(LoginRequiredMixin,CreateView):
    def get(self,request):
        #1 For updating the ticket status

        if 'ticketId' in request.GET:
            # print("In Ticket Id --- ",request.GET['ticketId'],'--- ',type(request.GET['ticketId']))
            for each in Tickets.objects.filter(id = int(request.GET['ticketId'])):
                # print(each.subject,each.id,each.status)
                # updating the status
                each.status = 1
                each.save()
        else:
            print("Didn't get ticket id")


        #2 For Updating ticket updates to the accepted_ticket table
        accepted_ticket_obj = AcceptedTickets.objects.create(acceptedBy_id = request.user.id,ticket_id = int(request.GET['ticketId']) ) 
        accepted_ticket_obj.save() 
        context_data = {'unaccepted_tickets':Tickets.objects.all(),'accepted_tickets':AcceptedTickets.objects.filter(acceptedBy_id = request.user.id)}

        return render(request,'agent_dashboard.html',context_data)

    
    
