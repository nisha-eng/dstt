from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.IndexView.as_view(),name='index' ),
    path('clients/',views.ClientsView.as_view(),name='clients'),
    path('clients_list/',views.clients_list.as_view(),name='clients_list'),
    path('leads/',views.LeadsView.as_view(),name='leads' ),
    path('tickets/',views.TicketsView.as_view(),name='tickets' ),
]