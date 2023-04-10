from django.forms import forms, ModelForm
from .models import auction_listing 

class listingForm(ModelForm):
    class Meta:
        model = auction_listing
        fields = '__all__'

