from django.urls import path
from .views import (
    country_list, country_detail, country_create, country_update, country_delete,
    state_list, state_detail, state_create, state_update, state_delete
)

urlpatterns = [
    path('', country_list, name='country_list'),
    path('country/<int:pk>/', country_detail, name='country_detail'),
    path('country/create/', country_create, name='country_create'),
    path('country/update/<int:pk>/', country_update, name='country_update'),
    path('country/delete/<int:pk>/', country_delete, name='country_delete'),
    path('country/<int:country_id>/states/', state_list, name='state_list'),
    path('state/<int:pk>/', state_detail, name='state_detail'),
    path('<int:country_id>/state/create/', state_create, name='state_create'),
    path('<int:country_pk>/state/<int:state_pk>/update/', state_update, name='state_update'),
    path('<int:country_pk>/state/<int:state_pk>/delete/', state_delete, name='state_delete'),
]
