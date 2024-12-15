from django.urls import path
from .views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('connecter/',Connecter_Compte,name='login'),
    path("creation/", Creation_Compte, name="creation"),
    path('verification/', Verification_Mail, name='verification'),
    path('modification-code/<str:email>/', Changement_Code, name="modifierCode"),
    path('deconnection/', Deconnection, name="deconnection"),
]
