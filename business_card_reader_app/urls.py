from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.card_upload, name='card_upload'),
    url(r'^business_cards_list/$', views.business_cards_list, name='business_cards_list'),

]