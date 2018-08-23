"""crediario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from crediario.admin import admin_site
from django.urls import path
from crediario.clientes import views as clientes_views


urlpatterns = [
    path('painel/', admin_site.urls),
    path('clientes/', clientes_views.vw_clientes),
    path('api/clientes/<int:codigo>/imagem/', 
        clientes_views.vw_api_imagem_cliente,
        name='api_cliente_imagem'),
]
