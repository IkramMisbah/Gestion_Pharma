from django.shortcuts import render, redirect

from django.contrib.auth import login,authenticate, logout
from django.contrib import messages

import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



# Create your views here.

# fonction pour créer un compte 

def Creation_Compte(request):

    if request.method ==  "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # verification des mots de passe

        if password != password_confirm:
            messages.error(request, "Les mots de passe ne sont pas identiques. veuillez réessayer.")
            return redirect ("creation")

        # verification de la longeur et des caractères du mot de passe  

        if len(password) < 8 or not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password) or not re.search(r'[!@#$%(),.?":{}`|<>]', password):
            messages.error(request, 'Le mot de passse doit contenir au moins 8 caractères, incluant des lettres, des chiffres et des caractères spéciaux.')
            return redirect("creation")
        
        # verification du format de l'adresse mail

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "L'adresse e-mail invalide. Veuillez réessayer.")
            return redirect("creation")
        
        # verification de l'existence de l'utilisateur et de l'adresse mail
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà. Veuillez réessayer.")
            return redirect("creation")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Cette adresse e-mail est déjà utilisée. Veuullez en choisir une autre.")
            return redirect("creation")
        
        # création de l'utilisateur

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Compte crée avec succès. Connectez-vous maintenant.")

        return redirect('login')
    
    return render(request, "creation.html")



# Fonction pour gérer la connexion d'un utilisateur
def Connecter_Compte(request):

    # Vérifie si la requête envoyée est de type POST (soumission du formulaire)
    if request.method == 'POST':

        # Récupère les données envoyées par l'utilisateur dans le formulaire de connexion
        username = request.POST.get('username')  # Récupère le nom d'utilisateur
        password = request.POST.get('password')  # Récupère le mot de passe

        # Utilise la fonction authenticate pour vérifier les identifiants de l'utilisateur
        # Si l'utilisateur est trouvé et les informations sont correctes, authenticate retourne un utilisateur
        user = authenticate(request, username=username, password=password)

        # Vérifie si un utilisateur valide a été trouvé
        if user is not None:
            # Si l'utilisateur est authentifié, connecte l'utilisateur à la session
            login(request, user)
            
            # Redirige l'utilisateur vers la page d'accueil ou une autre page après connexion réussie
            return redirect('acc')
        
        else:
            # Si les identifiants sont incorrects, un message d'erreur est généré et affiché
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            
            # Redirige l'utilisateur vers la page de connexion en cas d'erreur
            return redirect("login")
    
    # Si la requête n'est pas de type POST (par exemple lors de la première visite ou requête GET),
    # le formulaire de connexion est affiché
    return render(request, 'login.html')


# Fonction pour la vérification de l'adresse mail
def Verification_Mail(request):
    # Vérifie si la méthode de la requête est POST
    if request.method == "POST":
        # Récupère l'adresse email saisie par l'utilisateur dans le formulaire
        email = request.POST.get('email')

        # Vérifie si un email a été entré
        if not email:
            # Affiche un message d'erreur si le champ email est vide
            messages.error(request, "Veuillez rentrer une adresse mail valide.")
            # Retourne la page de vérification
            return render(request, "verificaionMail.html")
        
        # Recherche un utilisateur avec l'email saisi
        user = User.objects.filter(email=email).first()

        # Si un utilisateur avec cet email existe
        if user:
            # Redirige vers la page de modification du code avec l'email en paramètre
            return redirect("modifierCode", email=email)
        else:
            # Sinon, affiche un message d'erreur
            messages.error(request, "Cette adresse ne correspond à aucun compte. Veuillez réessayez avec une autre ou créez un compte")
            # Redirige vers la page de vérification
            return redirect("verification")
    
    # Si la méthode n'est pas POST, affiche la page de vérification
    return render(request, "verificaionMail.html")


# Fonction pour changer le mot de passe après vérification de l'email
def Changement_Code(request, email):
    try:
        # Recherche l'utilisateur correspondant à l'email donné
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # Si aucun utilisateur n'est trouvé, affiche un message d'erreur
        messages.error(request, "L'utilisateur introuvable.")
        # Redirige vers la page de vérification
        return redirect("verification")
    
    # Si la méthode de la requête est POST, traite les données du formulaire
    if request.method == "POST":
        # Récupère les mots de passe saisis
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Vérifie si les mots de passe correspondent
        if password == password_confirm:
            # Vérifie si le mot de passe respecte les règles de sécurité
            if len(password) < 8:
                messages.error(request, "Le mot de passe doit contenir au moins 8 caractères.")
            elif not any(char.isdigit() for char in password):
                messages.error(request, "Le mot de passe doit contenir au moins un chiffre.")
            elif not any(char.isalpha() for char in password):
                messages.error(request, "Le mot de passe doit contenir au moins une lettre.")
            else:
                # Si toutes les vérifications passent, met à jour le mot de passe de l'utilisateur
                user.set_password(password)
                user.save()
                # Affiche un message de succès
                messages.success(request, "Le mot de passe a bien été modifié. Connectez-vous maintenant.")
                # Redirige vers la page de connexion
                return redirect("login")
        else:
            # Si les mots de passe ne correspondent pas, affiche un message d'erreur
            messages.error(request, "Les mots de passe ne correspondent pas. Réessayez.")
    
    # Si la méthode n'est pas POST ou en cas d'erreur, affiche le formulaire avec l'email
    context = {'email': email}
    return render(request, "nouveauMDP.html", context)



# fonction pour la deconnection

def Deconnection(request):

    logout(request)
    return redirect("login")