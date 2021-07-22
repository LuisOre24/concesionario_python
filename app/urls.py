from django.urls import path
from .views import MarcaList, MarcaCreate, MarcaUpdate, MarcaDelete

urlpatterns = [
    #path('/' , name='index'),
    path('marcas', MarcaList.as_view(), name='marca_list'),
    path('marcas/create', MarcaCreate.as_view(), name='marca_create'),
    path('marcas/update/<pk>', MarcaUpdate.as_view(), name='marca_update'),
    path('marcas/delete/<pk>', MarcaDelete.as_view(), name='marca_delete'),
]