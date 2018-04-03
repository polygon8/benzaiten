from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .forms import CustomUserCreationForm
from .models import CustomUser


def profile(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    pseudonyms = user.pseudonym_set.all()
    ipi_numbers = user.ipinumber_set.all()
    return render(
        request,
        'account/profile.html',
        {
            'user': user,
            'pseudonyms': pseudonyms,
            'ipi_numbers': ipi_numbers
        }
    )


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'
