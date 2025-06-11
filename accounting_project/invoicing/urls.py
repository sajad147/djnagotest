from django.urls import path
from . import views

app_name = 'invoicing'
urlpatterns = [
    path('', views.invoice_list, name='invoice_list'), # Assuming root of /invoices/ shows list
    path('create/', views.invoice_create, name='invoice_create'),
    path('<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('<int:pk>/print/', views.invoice_print, name='invoice_print'),
]
