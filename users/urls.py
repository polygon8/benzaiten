from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path(
        'profile/<int:pk>/edit',
        views.CustomUserChangeForm.as_view(),
        name='edit-profile'
    ),
    path(
        'pseudonyms/<int:user_id>',
        views.pseudonyms,
        name='pseudonyms'
    ),
    path(
        'pseudonyms/<int:pk>/edit>',
        views.PseudonymChangeForm.as_view(),
        name='edit-pseudonym'
    ),
    path(
        'pseudonyms/<int:pseudonym_id>/delete',
        views.delete_pseudonym,
        name='delete-pseudonym'
    )
]
