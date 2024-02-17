from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import CarDealer, DealerReview
from .restapis import get_dealer_reviews_from_cf, get_dealers_from_cf
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json


# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create an `about` view to render a static about page
def about(request):
    return render(request, 'djangoapp/about.html')

# Create a `contact` view to return a static contact page
def contact_us(request):
    return render(request, 'djangoapp/contact_us.html')

# Create a `login_request` view to handle sign in request
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('djangoapp:index')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'djangoapp/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('djangoapp:index')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! You have been successfully registered.")
            return redirect('djangoapp:index')
        else:
            messages.error(request, "Invalid form submission. Please check the form.")
    else:
        form = UserCreationForm()
    return render(request, 'djangoapp/registration.html', {'form': form})

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        url = "https://iprogramco-3000.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/dealerships/get"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        # Concat all dealer's short name
        dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        return HttpResponse(dealer_names)
        # Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    context = {}
    if request.method == "GET":
        print("dealerid:", dealer_id)
        url = "https://iprogramco-3000.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/dealerships/get"  # Replace with your actual URL
        # Get reviews by dealer id
        reviews = get_dealer_reviews_from_cf(url, dealer_id)
        context["reviews"] = reviews
        print("Dealer:", dealer_id)
        print("Reviews:", reviews)
        # Return HttpResponse with the reviews as context
        return render(request, 'djangoapp/dealer_details.html', context)

# Create an `add_review` view to submit a review
# def add_review(request, dealer_id):
#     if request.method == 'POST':
#         # Handle review submission logic here
#     else:
#         return render(request, 'djangoapp/add_review.html')

