from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Country, State
from .forms import CountryForm, StateForm
from django.contrib.auth.decorators import login_required

@login_required
def country_list(request):
    user = request.user
    countries = Country.objects.all()
    return render(request, 'countries/country_list.html', {'countries': countries, 'user': user, 'segment': 'countries'})

@login_required
def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(request, 'countries/country_detail.html', {'country': country, 'segment': 'countries'})

@login_required
def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('country_list')
        else:
            print("Form errors:", form.errors)  # Debug line
            return render(request, 'countries/country_form.html', {'form': form, 'segment': 'countries'})
    else:
        form = CountryForm()
    return render(request, 'countries/country_form.html', {'form': form, 'segment': 'countries'})

@login_required
def country_update(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country_list')
        else:
            print("Form errors:", form.errors)  # Debug line
            return render(request, 'countries/country_form.html', {'form': form, 'segment': 'countries'})
    else:
        form = CountryForm(instance=country)
    return render(request, 'countries/country_form.html', {'form': form, 'segment': 'countries'})

def country_delete(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        country.delete()
        return redirect('country_list')
    return render(request, 'countries/country_confirm_delete.html', {'country': country, 'segment': 'countries'})

# State Views
@login_required
def state_list(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    states = State.objects.filter(country=country)
    return render(request, 'countries/state_list.html', {'states': states, 'country': country, 'segment': 'countries'})

@login_required
def state_detail(request, pk):
    state = get_object_or_404(State, pk=pk)
    return render(request, 'countries/state_detail.html', {'state': state, 'country': state.country, 'segment': 'countries'})

@login_required
def state_create(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            state = form.save(commit=False)
            state.country = country
            state.save()
            return redirect('state_list', country_id=country.id)
        else:
            print("Form errors:", form.errors)  # Debug line
            return render(request, 'countries/state_form.html', {'form': form, 'country': country, 'segment': 'countries'})
    else:
        form = StateForm()
    return render(request, 'countries/state_form.html', {'form': form, 'country': country, 'segment': 'countries'})

@login_required
def state_update(request, country_pk, state_pk):
    country = get_object_or_404(Country, pk=country_pk)
    state = get_object_or_404(State, pk=state_pk, country=country)
    if request.method == 'POST':
        form = StateForm(request.POST, instance=state)
        if form.is_valid():
            form.save()
            return redirect('state_list', country_id=country.id)
        else:
            print("Form errors:", form.errors)  # Debug line
            return render(request, 'countries/state_form.html', {'form': form, 'country': country, 'segment': 'countries'})
    else:
        form = StateForm(instance=state)
    return render(request, 'countries/state_form.html', {'form': form, 'country': country, 'segment': 'countries'})

@login_required
def state_delete(request, country_pk, state_pk):
    country = get_object_or_404(Country, pk=country_pk)
    state = get_object_or_404(State, pk=state_pk, country=country)
    if request.method == 'POST':
        state.delete()
        return redirect('state_list', country_id=country.id)
    return render(request, 'countries/state_confirm_delete.html', {'state': state, 'country': country, 'segment': 'countries'})
