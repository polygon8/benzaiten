from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, IpiNumberCreationForm
from .models import CustomUser, Pseudonym, IpiNumber


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


def ipi_numbers(request):
    if request.method == 'GET':
        form = IpiNumberCreationForm()

        return render(
            request,
            'account/ipi_numbers.html',
            {'form': form}
        )
    elif request.method == 'POST':
        form = IpiNumberCreationForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.ipi_type = IpiNumber.clean_ipi_type(post.number)
            post.save()
            return redirect(
                reverse(
                    'profile',
                    kwargs={'user_id': request.user.id}
                )
            )

        return render(
            request,
            'account/ipi_numbers.html',
            {'form': form}
        )


def delete_ipi_number(request, ipi_number_id):
    ipi_number = get_object_or_404(IpiNumber, pk=ipi_number_id)
    ipi_number.delete()
    return redirect(reverse('profile', kwargs={'user_id': ipi_number.user.id}))


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


class IpiNumberChangeForm(generic.UpdateView):
    model = IpiNumber
    fields = ['number']
    template_name = 'account/edit_ipi_number.html'
