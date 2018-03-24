from django.shortcuts import render, redirect

from .models import BusinessCard
from .templates.business_card_reader_app.forms import ImageFileForm


def home(request):
    return render(request, 'business_card_reader_app/card_upload.html')


def business_cards_list(request):
    business_cards = BusinessCard.objects.order_by('surname')
    return render(request, 'business_card_reader_app/business_cards_list.html', {'business_cards' : business_cards})


def card_upload(request):
    if request.method == 'POST':
        form = ImageFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card_upload')
    else:
        form = ImageFileForm()
    return render(request, 'business_card_reader_app/card_upload.html', {
        'form': form
    })