from django import forms

from .models import *


class SearchBarForm(forms.Form):
    search = forms.CharField()


class predictionForm(forms.Form):
    open = forms.IntegerField(label="Today's Open Value ", required=False)
    prevclose = forms.IntegerField(label="Previous days Close Value ", required= False)
    ltp = forms.IntegerField(label="Lowest Traded Price Today ", required=False)
    sitename = forms.CharField(label="Please copy the name of the company (Exclude 'Profile' ) and paste it here to verify you're not a bot")

class compprofileForm(forms.Form):
    name = forms.CharField(max_length='200')

