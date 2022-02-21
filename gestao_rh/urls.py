from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
urlpatterns = [
    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
    # path('funcionarios/', include('apps.funcionarios.urls'), namespace='funcionarios'),
    # path('funcionarios/', include('apps.funcionarios.urls'), namespace='funcionarios'),
    # path('funcionarios/', include('apps.funcionarios.urls'), namespace='funcionarios'),
]
