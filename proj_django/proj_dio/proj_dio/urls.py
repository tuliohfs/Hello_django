from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('soma/<n1>/<n2>', views.soma),
    path('subtracao/<n1>/<n2>', views.subtracao),
    path('multiplicacao/<n1>/<n2>', views.multiplicacao),
    path('divisao/<n1>/<n2>', views.divisao)
]
