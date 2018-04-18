from django.urls import path

from . import views

urlpatterns = [
    path('tracks/', views.tracks, name='tracks'),
    path('track/add', views.add_track, name='add-track'),
    path(
        'track/<int:pk>/edit',
        views.TrackChangeForm.as_view(),
        name='edit-track'
    ),
    path(
        'track/<int:track_id>/delete',
        views.delete_track,
        name='delete-track'
    )
]
