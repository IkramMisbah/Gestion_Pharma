from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from datetime import datetime

from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from .forms import AjoutProduit,AjoutVente
from django.urls import reverse_lazy
#pour la modif
from django.core.files.storage import FileSystemStorage
#pour la suppression
from django.http import JsonResponse

#pour forcer le login
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

#importer les models (tables)
from .models import *




@login_required(login_url='login')
#fonction pour aller vers la page d'acceuil:
def Acc(request):
    return render(request,'acc.html')




@login_required(login_url='login')
# Create your views here.
def home(request):
    donnees=Produits.objects.all()
    context={
        'donnees':donnees
    }
    return render(request,'home.html',context)


# def ajout_donnees(request):
# #creation de la variable pour la gestion des erreurs :
#     category=Categories.objects.all()
#     errors={}
#     if request.method=='POST':
#         name=request.POST.get('name')
#         price=request.POST.get('price')
#         quantite=request.POST.get('quantite')
#         date_expiration=request.POST.get('date_expiration')
#         description=request.POST.get('description')
#         image = request.FILES.get('image')


#         #validation de la date:
#         try:
#             date_expiration=datetime.strptime(date_expiration,"%Y-%m-%d")
#         except ValueError:
#             errors["date_expiration"]="le format de la date est invalide .Essayer:AAAA-MM-DD"

#         #validation du prix:
#         try:
#             price=float(price)
#             if price < 0:
#                 errors['price']="le prix ne peut pas etre négatif"
#         except ValueError:
#             errors['price']="Entrer un prix valide svp"

#         try:
#             quantite=float(quantite)
#             if quantite < 0:
#                 errors['quantite']="le prix ne peut pas etre négatif"
#         except ValueError:
#             errors['quantite']="Entrer un prix valide svp"
#         #si aucune erreur
#         if not errors:
#             try:
#                 category=Categories.objects.get(pk=request.POST['category'])

#                 savedonnees=Produits(name=name,price=price,quantite=quantite,date_expiration=date_expiration,category=category,image=image,description=description)
#                 savedonnees.save()
#                 return redirect('home')
#             except Categories.DoesNotExist:
#                 errors['category']=f'la catégorie specifié est introuvable'
#             except KeyError as e:
#                 errors[str(e)]=f'le champ {e} est manquant dans la requete'
#             except Exception as e:
#                 messages.error(request,f'une erreur {e} est survenue')
        
#         else:
#             category=Categories.objects.all()

#     return render(request,'ajout_donnee.html',{'category':category,'errors':errors})



# Fonction pour modifier un produit existant
# def modifier(request, id):

#     # Recherche le produit correspondant à l'id ou renvoie une erreur 404 s'il n'existe pas
#     produit = get_object_or_404(Produits, id=id)

#     # Récupère toutes les catégories disponibles pour les afficher dans le formulaire
#     categories = Categories.objects.all()

#     # Initialise un dictionnaire pour stocker les erreurs de validation
#     errors = {}

#     # Vérifie si la méthode HTTP utilisée est POST (indiquant que l'utilisateur a soumis le formulaire)
#     if request.method == 'POST':

#         # Récupère les données soumises par l'utilisateur depuis le formulaire
#         name = request.POST.get('name')  # Nom du produit
#         category_id = request.POST.get('category')  # ID de la catégorie
#         price = request.POST.get('price')  # Prix du produit
#         quantite = request.POST.get('quantite')  # Quantité disponible
#         description = request.POST.get('description')  # Description du produit
#         date_expiration = request.POST.get('date_expiration')  # Date d'expiration
#         image = request.FILES.get('image')  # Fichier image uploadé (optionnel)

#         # Validation des champs obligatoires
#         if not name:  # Vérifie si le nom est vide
#             errors['name'] = "Le nom est requis"

#         if not category_id:  # Vérifie si aucune catégorie n'a été sélectionnée
#             errors['category'] = "La catégorie est requise"

#         if not price:  # Vérifie si le prix n'est pas renseigné
#             errors['price'] = "Le prix est requis"

#         if not quantite:  # Vérifie si la quantité n'est pas renseignée
#             errors['quantite'] = "La quantité est requise"

#         if not description:  # Vérifie si la description est vide
#             errors['description'] = "La description est requise"

#         # Validation du format de la date d'expiration si elle est renseignée
#         if date_expiration:
#             try:
#                 # Vérifie que la date respecte le format 'AAAA-MM-JJ'
#                 datetime.strptime(date_expiration, '%Y-%m-%d')
#             except ValueError:
#                 # Ajoute une erreur si le format est incorrect
#                 errors['date_expiration'] = (
#                     "Le format de la date d'expiration est incorrect. Utilisez le format AAAA-MM-JJ."
#                 )

#         # Si aucune erreur n'a été détectée, on peut modifier le produit
#         if not errors:
#             # Récupère la catégorie sélectionnée
#             category = get_object_or_404(Categories, id=category_id)

#             # Met à jour les informations du produit avec les nouvelles données
#             produit.name = name
#             produit.category = category
#             produit.price = price
#             produit.quantite = quantite
#             produit.description = description
#             produit.date_expiration = date_expiration

#             # Si une nouvelle image a été uploadée
#             if image:
#                 # Sauvegarde l'image sur le serveur
#                 fs = FileSystemStorage()
#                 filname = fs.save(image.name, image)
#                 # Met à jour l'URL de l'image dans le produit
#                 produit.image = fs.url(filname)

#             # Sauvegarde les modifications dans la base de données
#             produit.save()

#             # Ajoute un message de succès à afficher à l'utilisateur
#             messages.success(request, "Le produit a été modifié avec succès !")

#             # Redirige l'utilisateur vers la page d'accueil après la modification
#             return redirect("home")
#         else:
#             # Si des erreurs ont été détectées, elles sont ajoutées aux messages
#             for key, error in errors.items():
#                 messages.error(request, error)

#     # Charge la page de modification avec les informations actuelles du produit, 
#     # les catégories disponibles et les éventuelles erreurs détectées
#     return render(request, "modification.html", {
#         'produit': produit, 
#         'categories': categories, 
#         'errors': errors
#     })

# @login_required(login_url='login')
#fpnction por supprimer un produit
# def supprimer(request,id):
#     if request.method =='POST':
#         produit=get_object_or_404(Produits,id=id)
#         produit.delete()
#         return JsonResponse(
#             {
#                 'success':True,
#                 'message':'le produit a été supprimé avec succes'
#             }
#         )
#     return JsonResponse(
#         {
#             'success':False,
#             'message':'Méthode non autorisé'
#         }
#     )


#fonction pour afficher les details:
# def detail(request,id):
#     n=Produits.objects.get(id=id)
#     return render(request,'detail.html',{'n':n})


#class pour ajouter les produit entre par le formulaire

class AjoutProduits(LoginRequiredMixin,CreateView):
     # utilisation du modele
    model = Produits
    # specifier le forulaire à utiliser
    form_class = AjoutProduit
    # afichage du template
    template_name = 'ajout_donnee.html'
    # redirection après enregistrement 
    success_url = reverse_lazy('home') 

#class pour modifier les produits par le formulaire
#import UpdatevIEW
class Update_donnees(LoginRequiredMixin,UpdateView):
    # utilisation du modele
    model = Produits
    # specifier le forulaire à utiliser
    form_class = AjoutProduit
    # afichage du template
    template_name = 'modification_2.html'
    # redirection après enregistrement 
    success_url = reverse_lazy('home') 


# class pour supprimer les données
class delete(LoginRequiredMixin, DeleteView):

    model = Produits
    template_name = "delete.html"
    success_url = reverse_lazy('home')



#class pour afficher les details:
class details(LoginRequiredMixin,DetailView):
    model=Produits
    template_name='detail.html'
    context_object_name='n'


@login_required(login_url='login')
#fonction pour rechercher un produit:
def recherche(request):
    #recupere le produit depuis  la barre de recherche 'c est produit =(name=produit ds header.html)
    query=request.GET.get('produit')
    donnees=Produits.objects.filter(name__icontains=query)
    context={
        'donnees':donnees
    }
    return render(request,'resultat_recherche.html',context)




# Fonction pour gérer la vente d'un produit
def VenteProduits(request, id):
    # Récupérer le produit correspondant à l'ID ou renvoyer une erreur 404 si non trouvé
    produit = get_object_or_404(Produits, id=id)

    # Variable pour stocker les messages d'erreur ou d'avertissement à afficher dans le template
    message = None

    # Vérification si la méthode de requête est POST (soumission d'un formulaire)
    if request.method == 'POST':
        # Instanciation du formulaire AjoutVente avec les données soumises
        form = AjoutVente(request.POST)
        
        # Vérification de la validité des données soumises
        if form.is_valid():
            # Récupérer les données nettoyées (validées) du formulaire
            quantite = form.cleaned_data['quantite']
            customer_name = form.cleaned_data['customer']

            # Vérification si la quantité demandée dépasse le stock disponible
            if quantite > produit.quantite:
                # Message d'erreur pour signaler que le stock est insuffisant
                message = "La quantité demandée dépasse le stock disponible !"
            else:
                # Rechercher ou créer un client dans la base de données
                customer, _ = Customers.objects.get_or_create(name=customer_name)

                # Calcul du montant total de la vente
                total_amount = produit.price * quantite

                # Enregistrer une nouvelle vente dans la base de données
                sale = Vente(
                    produit=produit,
                    quantite=quantite,
                    total_amount=total_amount,
                    customer=customer
                )
                sale.save()

                # Mettre à jour le stock du produit après la vente
                produit.quantite -= quantite
                produit.save()

                # Rediriger vers la page de facture avec l'ID de la vente
                return redirect('facture', sale_id=sale.id)
    else:
        # Si la méthode de requête est GET, afficher un formulaire vide
        form = AjoutVente()

    # Vérification si le stock est bas (par exemple, inférieur ou égal à 5)
    if produit.quantite <= 5 and not message:
        # Message d'avertissement pour signaler un stock faible
        message = "Attention, le stock est bas !"

    # Contexte à transmettre au template HTML
    context = {
        'produit': produit,  # Le produit concerné
        'form': form,  # Le formulaire de vente
        'message': message  # Les messages d'erreur ou d'avertissement
    }

    # Rendu de la page HTML avec le contexte fourni
    return render(request, 'fomulaire_vente.html', context)

def SaveRecu(request, id):

    vente = get_object_or_404(Vente, id=id)
    customer = vente.customer
    quantite = vente.quantite
    total_amount = vente.total_amount
    produit = vente.produit

    recu = Facture_Client(
        customer = customer,
        quantite = quantite,
        total_amount = total_amount,
        produit = produit
    )

    recu.save()

    return redirect('facture', sale_id = id)

# Fonction pour afficher les détails d'une vente spécifique sous forme de facture
def Facture(request, sale_id):
    # Récupérer la vente correspondante à l'ID ou renvoyer une erreur 404 si non trouvée
    sale = get_object_or_404(Vente, id=sale_id)
    
    # Récupérer les informations associées à la vente
    customer = sale.customer  # Le client ayant effectué l'achat
    produit = sale.produit    # Le produit vendu
    quantite = sale.quantite  # Quantité du produit vendue
    sale_date = sale.sale_date  # Date de la vente
    total_amount = sale.total_amount  # Montant total de la vente (prix unitaire x quantité)

    # Créer un dictionnaire pour transmettre ces informations au template
    context = {
        'sale': sale,  # Objet complet de la vente
        'customer': customer,  # Nom ou informations du client
        'produit': produit,  # Détails du produit
        'quantite': quantite,  # Quantité vendue
        'sale_date': sale_date,  # Date de la vente
        'id': sale.id,  # ID unique de la vente
        'prix_unitaire': produit.price,  # Prix unitaire du produit
        'total_amount': total_amount  # Montant total de la vente
    }
    
    # Rendre le template HTML 'facture-client.html' avec les données contenues dans le contexte
    return render(request, 'facture-client.html', context)
