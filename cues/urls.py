from django.urls import path

from . import views

urlpatterns = [
    path('cue-sheets/', views.cue_sheets, name='cue-sheets'),
    path('cue-sheets/add', views.add_cue_sheet, name='add-cue-sheet'),
    path('cue-sheet/<int:sheet_id>', views.cue_sheet, name='cue-sheet'),
    path('cue-sheet/<int:sheet_id>/add-cue', views.add_cue, name='add-cue'),
]
