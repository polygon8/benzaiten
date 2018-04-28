from django.shortcuts import (
    get_object_or_404,
    redirect,
    render
)
from django.urls import reverse

from .models import CueSheet
from .forms import CueSheetCreationForm, CueCreationForm


def cue_sheets(request):
    cue_sheets = CueSheet.objects.filter(user=request.user)
    display_name = request.user.name if request.user.name else request.user.email.split('@')[0] # noqa

    return render(
        request,
        'cues/cue_sheets.html',
        {
            'cue_sheets': cue_sheets,
            'display_name': display_name
        }
    )


def cue_sheet(request, sheet_id):
    cue_sheet = get_object_or_404(CueSheet, pk=sheet_id)

    return render(
        request,
        'cues/cue_sheet.html',
        {
            'cue_sheet': cue_sheet,
            'cues': cue_sheet.cue_set.all()
        }
    )


def add_cue_sheet(request):
    if request.method == 'GET':
        return render(
            request,
            'cues/edit_cue_sheet.html',
            {'form': CueSheetCreationForm()}
        )
    elif request.method == 'POST':
        form = CueSheetCreationForm(request.POST)

        if form.is_valid():
            cue_sheet = form.save(commit=False)
            cue_sheet.user = request.user
            cue_sheet.save()
            return redirect(reverse('cue-sheets'))

        return render(
            request,
            'cues/edit_cue_sheet.html',
            {'form': form}
        )


def add_cue(request, sheet_id):
    if request.method == 'GET':
        return render(
            request,
            'cues/cue.html',
            {
                'form': CueCreationForm(),
                'sheet_id': sheet_id
            }
        )
    elif request.method == 'POST':
        form = CueCreationForm(request.POST)
        if form.is_valid():
            cue = form.save(commit=False)
            cue.cue_sheet = get_object_or_404(CueSheet, pk=sheet_id)
            cue.save()
            return reverse(
                    'cue-sheet',
                    kwargs={'sheet_id': sheet_id}
                )

        return render(
            request,
            'cues/cue.html',
            {
                'form': form,
                'sheet_id': sheet_id
            }
        )
