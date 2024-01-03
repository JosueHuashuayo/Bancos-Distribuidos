from django.urls import path
from django.views.generic import RedirectView
from .views import ListaCuentasView,login_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path("",RedirectView.as_view(url='login/',permanent=True)),
    path('cliente/<int:cliente_id>/cuentas/', ListaCuentasView.as_view(), name='lista_cuentas'),

    
]
