from django.urls import path
from .views import *

                    

urlpatterns = [
    #path('/' , name='index'),
    path('marcas', MarcaList.as_view(), name='marca_list'),
    path('marcas/create', MarcaCreate.as_view(), name='marca_create'),
    path('marcas/update/<pk>', MarcaUpdate.as_view(), name='marca_update'),
    path('marcas/delete/<pk>', MarcaDelete.as_view(), name='marca_delete'),

    path('autos', AutoList.as_view(), name='auto_list'),
    path('autos/create', AutoCreate.as_view(), name='auto_create'),
    path('autos/update/<pk>', AutoUpdate.as_view(), name='auto_update'),
    path('autos/delete/<pk>', AutoDelete.as_view(), name='auto_delete'),

    path('tipos', TipoList.as_view(), name='tipo_list'),
    path('tipos/create', TipoCreate.as_view(), name='tipo_create'),
    path('tipos/update/<pk>', TipoUpdate.as_view(), name='tipo_update'),
    path('tipos/delete/<pk>', TipoDelete.as_view(), name='tipo_delete'),
    
    path('transmisiones', TransmisionList.as_view(), name='transmision_list'),
    path('transmisiones/create', TransmisionCreate.as_view(), name='transmision_create'),
    path('transmisiones/update/<pk>', TransmisionUpdate.as_view(), name='transmision_update'),
    path('transmisiones/delete/<pk>', TransmisionDelete.as_view(), name='transmision_delete'),
]