from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard),
    path('business_cards_list/', views.business_cards_list),

]