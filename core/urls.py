from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('history/', views.history_view, name='history'),
    path('sectors/', views.sectors_view, name='sectors'),

    path('land-force/', views.land_view, name='land'),
    path('air-force/', views.air_view, name='air'),
    path('naval-force/', views.navy_view, name='navy'),
    path('air-defense/', views.airdefense_view, name='airdefense'),

    path('cyber-security/', views.cyber_view, name='cyber'),
    path('ai-defense/', views.ai_view, name='ai'),
    path('vision-mission/', views.vision_view, name='vision'),
    path('future-defense/', views.future_view, name='future'),
]