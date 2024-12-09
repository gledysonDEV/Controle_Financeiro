from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.listar_transacoes, name='listar_transacoes'),
    path('adicionar/', views.adicionar_transacao, name='adicionar_transacao'),
    path('editar/<int:pk>/', views.editar_transacao, name='editar_transacao'),
    path('deletar/<int:pk>/', views.deletar_transacao, name='deletar_transacao'),
    path('login/', auth_views.LoginView.as_view(template_name='transacoes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', views.registrar, name='registrar'),
]
