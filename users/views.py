from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import CustomUser, Pseudonym


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


def pseudonyms(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)

    if request.method == 'GET':
        pseudonyms = user.pseudonym_set.all()
        return render(
            request,
            'account/pseudonyms.html',
            {'pseudonyms': pseudonyms}
        )
    elif request.method == 'POST':
        Pseudonym.objects.create(
            name=request.POST.get('name'),
            user=user
        )
        return redirect(reverse('profile', kwargs={'user_id': user.id}))


def delete_pseudonym(request, pseudonym_id):
    pseudonym = get_object_or_404(Pseudonym, pk=pseudonym_id)
    pseudonym.delete()
    return redirect(reverse('profile', kwargs={'user_id': pseudonym.user.id}))


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


class CustomUserChangeForm(generic.UpdateView):
    model = CustomUser
    fields = ['name', 'email']
    template_name = 'account/edit_profile.html'


class PseudonymChangeForm(generic.UpdateView):
    model = Pseudonym
    fields = ['name']
    template_name = 'account/edit_pseudonym.html'
