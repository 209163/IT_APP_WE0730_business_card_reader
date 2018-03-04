from django.shortcuts import render


def dashboard(request):
    return render(request, 'business_card_reader_app/index.html', {})


def business_cards_list(request):
    return render(request, 'business_card_reader_app/business_cards_list.html', {})


