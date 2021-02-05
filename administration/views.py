from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.views import generic
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "administration/index.html"

class ClientsView(TemplateView):
    template_name = "administration/clients.html"    

class clients_list(TemplateView):
    template_name = "administration/clients_list.html" 

class LeadsView(TemplateView):
    template_name = "administration/leads.html"    
   
class TicketsView(TemplateView):
    template_name = "administration/tickets.html"    
      