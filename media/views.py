from django.shortcuts import (
    get_object_or_404,
    redirect,
    render
)
from django.urls import reverse
from django.views import generic

from .models import Track, IsrcNumber
from .forms import TrackCreationForm


def tracks(request):
    tracks = Track.objects.filter(user=request.user)
    display_name = request.user.name if request.user.name else request.user.email.split('@')[0] # noqa

    return render(
        request,
        'media/tracks.html',
        {
            'tracks': tracks,
            'display_name': display_name
        }
    )


def add_track(request):
    if request.method == 'GET':
        return render(
            request,
            'media/track.html',
            {'form': TrackCreationForm()}
        )
    elif request.method == 'POST':
        form = TrackCreationForm(request.POST)

        if form.is_valid():
            track = form.save(commit=False)
            track.user = request.user
            track.save()
            IsrcNumber.objects.create(track=track)
            return redirect(reverse('tracks'))

        return render(
            request,
            'media/track.html',
            {'form': form}
        )


def delete_track(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    track.delete()
    return redirect(reverse('tracks'))


class TrackChangeForm(generic.UpdateView):
    model = Track
    fields = [
        'title',
        'description',
        'year',
        'duration',
        'bpm',
        'origin_code'
    ]
    template_name = 'media/edit_track.html'
