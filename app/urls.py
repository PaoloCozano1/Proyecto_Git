from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name ="index"),
    path('registro/', registro, name="registro"),
    path('orden/', orden, name="orden"),
    path('factura/', factura, name="factura"),
    path('factura/<int:orden_id>/', factura, name="factura"),
]
