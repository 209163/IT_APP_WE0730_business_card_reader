from django import forms

from business_card_reader_app.models import ImageFile


class ImageFileForm(forms.ModelForm):
    class Meta:
        model = ImageFile
        fields = ('file', )