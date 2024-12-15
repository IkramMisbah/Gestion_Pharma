from django.urls import path
from .views import * 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     #path acceuil
    path('',Acc,name='acc'),
    path('produit/',home,name='home'),
    #path('ajout/',ajout_donnees,name='ajout')
    path('ajout/',AjoutProduits.as_view(),name='ajout'),
    #path('modification/<int:id>/', modifier,name='modifier')
    #id : C'est le nom du paramètre dynamique qui sera capturé dans l'URL et envoyé à la vue.
    #Exemple : Si l'URL est http://localhost:8000/modification/5/, Django capture 5 et le passe à la vue comme une variable nommée id.
    path('modification/<int:pk>/',Update_donnees.as_view(),name='modifier'),
    # path('supprimer/<int:id>/',supprimer,name='supprimer'),
    #path('detail/<int:id>/',detail,name='detail'),
    path('deelete/<int:pk>/',delete.as_view(),name='delete'),
    path('detail/<int:pk>/',details.as_view(),name='detail'),
    path('recherche/',recherche,name='recherche'),
      path('ajoutvente/<int:id>/', VenteProduits, name='ajoutvente'),
    path('saverecu/<int:id>/', SaveRecu, name='saverecu'),
    path('facture/<int:sale_id>/', Facture, name='facture'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
