from django import forms

from business_card_reader_app.models import BusinessCard


class CardForm(forms.ModelForm):
    class Meta:
        model = BusinessCard
        fields = ('description', 'img_path', )