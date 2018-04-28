from django import forms
from .models import CueSheet, Cue


class CueSheetCreationForm(forms.ModelForm):
    class Meta:
        model = CueSheet
        fields = (
            'programme_title',
            'production_company',
            'classification',
            'catalogue_number',
            'country',
            'programme_duration',
            'music_duration',
        )


class CueCreationForm(forms.ModelForm):
    class Meta:
        model = Cue
        fields = (
            'title',
            'cue_position',
            'duration',
            'usage_code',
            'time_in',
            'time_out',
        )
