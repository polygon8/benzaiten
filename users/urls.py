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
    path('pseudonyms/', views.pseudonyms, name='pseudonyms'),
    path(
        'pseudonyms/<int:pk>/edit>',
        views.PseudonymChangeForm.as_view(),
        name='edit-pseudonym'
    ),
    path(
        'pseudonyms/<int:pseudonym_id>/delete',
        views.delete_pseudonym,
        name='delete-pseudonym'
    ),
    path('ipi-numbers/', views.ipi_numbers, name='ipi-numbers'),
    path(
        'ipi-numbers/<int:pk>/edit',
        views.IpiNumberChangeForm.as_view(),
        name='edit-ipi-number'
    ),
    path(
        'ipi-numbers/<int:ipi_number_id>/delete',
        views.delete_ipi_number,
        name='delete-ipi-number'
    )
]
