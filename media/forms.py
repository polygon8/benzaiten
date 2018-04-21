from django import forms
from .models import Track


class TrackCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrackCreationForm, self).__init__(*args, **kwargs)
        self.fields['bpm'].label = 'BPM'

    class Meta:
        model = Track
        fields = (
            'title',
            'description',
            'year',
            'duration',
            'bpm',
        )


class TrackChangeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrackCreationForm, self).__init__(*args, **kwargs)
        self.fields['bpm'].label = 'BPM'

    class Meta:
        model = Track
        exclude = ('created_at', 'updated_at',)
