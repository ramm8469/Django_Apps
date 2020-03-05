from django.urls import path
from .views import LandingPageView,HomePageView,AboutPageView,CreateTicketView,UpdateTicketView,DeleteTicketView,AgentHomePageView,TicketsAcceptedView,TicketResolvedView

# 

urlpatterns = [

    path('',LandingPageView.as_view(),name='Index'),
    path('home/',HomePageView.as_view(),name='Home'),
    path('about/',AboutPageView.as_view(),name='About'),
    path('createTicket/',CreateTicketView.as_view(),name='CreateTicket'),
    path('updateTicket/<int:pk>/',UpdateTicketView.as_view(),name='UpdateTicket'),
    path('deleteTicket/<int:pk>/',DeleteTicketView.as_view(),name='DeleteTicket'),
    # For Agents
    path('dashboard/',AgentHomePageView.as_view(),name='AgentHomePage'),
    path('acceptedTickets/',TicketsAcceptedView.as_view(),name='AcceptTicket'),
    path('resolveTickets/',TicketResolvedView.as_view(),name='ResolveTicket'),

   
    
]