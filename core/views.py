from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# This view renders the home page
def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/home.html')


def history_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/history.html')

# This view renders the military sectors page
def sectors_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/sectors.html')


def land_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/land.html')

def air_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/air.html')

def navy_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/navy.html')

def airdefense_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/airdefense.html')

# This view renders the cyber security page
def cyber_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/cyber.html')


# This view renders the AI in defense page
def ai_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/ai.html')


# This view renders the vision and mission page
def vision_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/vision.html')


# This view renders the future defense page
def future_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/future.html')