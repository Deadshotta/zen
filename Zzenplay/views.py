# views.py
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST

@require_POST
def order_movie(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    movie_title = request.POST.get('movieTitle')
    message = request.POST.get('message')

    subject = f"New movie order from {name}"
    body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMovie Title: {movie_title}\nMessage: {message}"

    try:
        send_mail(subject, body, 'birirmichael@gmail.com', ['recipient@example.com'])  # Update with the recipient email
        return HttpResponse("Order sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error sending order: {e}")
@require_POST
def order_game(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    game_title = request.POST.get('gameTitle')
    message = request.POST.get('message')

    subject = f"New game order from {name}"
    body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nGame Title: {game_title}\nMessage: {message}"

    try:
        send_mail(subject, body, 'birirmichael@gmail.com', ['recipient@example.com'])  # Update with the recipient email
        return HttpResponse("Order sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error sending order: {e}")
    
@require_POST
def send_email(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    service = request.POST.get('service')
    email = request.POST.get('email')
    message = request.POST.get('message')

    subject = f"New contact from {name}"
    body = f"Name: {name}\nPhone: {phone}\nService: {service}\nEmail: {email}\nMessage: {message}"

    send_mail(subject, body, 'birirmichael@gmail.com', ['recipient@example.com'])

    return HttpResponse("Email sent successfully!")


def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})
def service(request):
    return render(request, 'service.html', {})

def team(request):
    return render(request, 'team.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def movies(request):
    return render(request, 'movies.html', {})

def games(request):
    return render(request, 'games.html', {})

def VR(request):
    return render(request, 'VR.html', {})
def login(request):
    return render(request, 'login.html', {})

