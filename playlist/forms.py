from django import forms
from datetimewidget.widgets import DateWidget
from django.forms import ModelForm
from django.forms.widgets import TextInput, CheckboxInput

from .models import PlaylistEntry


class NewPlaylistForm(forms.Form):
    showName = forms.CharField(label="Show Name", max_length="200")
    host = forms.CharField(label="Hosts", max_length="200")
    date = forms.DateField(label="Date", widget = DateWidget(usel10n=True, bootstrap_version=3))

class EditPlaylistForm(forms.Form):
    pass


class PlaylistEntryForm(forms.ModelForm):
    class Meta:
        model = PlaylistEntry
        exclude = {'playlist', 'catalogueEntry'}
        widgets = {
            'artist': TextInput(attrs={'placeholder': 'Artist', 'class':"form-control input-sm typeahead-artist"}),
            'title': TextInput(attrs={'placeholder': 'Track', 'class':"form-control input-sm typeahead-track"}),
            'album': TextInput(attrs={'placeholder': 'Album', 'class':"form-control input-sm"}),
            'duration': TextInput(attrs={'placeholder': 'mm:ss', 'class':"form-control input-sm", 'style':'width: 60px;'}),
            'local': CheckboxInput(attrs={'class':"local_check",}),
            'australian': CheckboxInput(attrs={'class':"australian_check",}),
            'female': CheckboxInput(attrs={'class':"female_check",}),
        }
