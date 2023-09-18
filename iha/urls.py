from django.urls import path
from . import views


app_name = 'iha'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:iha_id>/", views.iha_view, name="iha_view"),
    path("<int:iha_id>/add_rental/", views.add_rental, name="add_rental"),
    path('add_iha/', views.add_iha, name='add_iha'),
    path("rental_history/", views.rental_history, name="rental_history"),
    path("<int:rental_id>/cancel_rental/", views.cancel_rental, name="cancel_rental"),
    path("delete_rental_history/", views.delete_rental_history, name="delete_rental_history"),
    path('edit_iha/<int:iha_id>/', views.edit_iha, name='edit_iha'),
    path('delete_iha/<int:iha_id>/', views.delete_iha, name='delete_iha'),
]
