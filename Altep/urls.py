from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('Dashboard.urls')),
    path('usuario/',include('Accounts.urls')),
    path('api/',include('Electricity.urls')),
    path('admin/', admin.site.urls),
]

# Configurando as views dos erros
handler400 = 'Dashboard.views.handler400'
handler403 = 'Dashboard.views.handler403'
handler404 = 'Dashboard.views.handler404'
handler500 = 'Dashboard.views.handler500'
