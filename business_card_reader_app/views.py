from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from .models import BusinessCard


def home(request):
    return render(request, 'business_card_reader_app/card_upload.html')


def business_cards_list(request):
    business_cards = BusinessCard.objects.order_by('surname')
    return render(request, 'business_card_reader_app/business_cards_list.html', {'business_cards' : business_cards})


def card_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'business_card_reader_app/card_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'business_card_reader_app/card_upload.html')