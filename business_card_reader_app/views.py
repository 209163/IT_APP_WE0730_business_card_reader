from django.shortcuts import render

from .models import BusinessCard


def dashboard(request):
    business_cards = BusinessCard.objects.order_by('surname')
    return render(request, 'business_card_reader_app/index.html', {'business_cards' : business_cards})


def business_cards_list(request):
    business_cards = BusinessCard.objects.order_by('surname')
    return render(request, 'business_card_reader_app/business_cards_list.html', {'business_cards' : business_cards})


