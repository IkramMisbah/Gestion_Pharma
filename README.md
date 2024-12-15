# 💊 Application de Gestion de Pharmacie avec Django


Cette application a été conçue pour simplifier et automatiser les processus de gestion d'une pharmacie. Elle offre une solution complète et intuitive pour gérer les stocks de médicaments, les transactions et les données des clients, tout en garantissant sécurité et performance.

## Principales fonctionnalités

### Gestion des médicaments
- Ajouter, modifier et supprimer des médicaments avec des informations détaillées (nom, dosage, quantité, prix, date d'expiration, etc.).
- Suivi des stocks en temps réel, avec alertes pour les médicaments en rupture ou expirés.

### Gestion des ventes
- Enregistrement des ventes quotidiennes avec détails des transactions (produits achetés, quantités, prix total, date).
- Génération de reçus pour les clients.

### Gestion des utilisateurs
- Ajout de rôles et de permissions pour différents utilisateurs (administrateurs, pharmaciens, assistants).
- Authentification sécurisée pour protéger les données sensibles.

### Recherche et filtrage
- Fonctionnalité de recherche avancée pour retrouver facilement un médicament ou une transaction spécifique.
- Filtres personnalisés pour analyser les ventes ou les stocks.



## Technologies utilisées
- **Django (Backend)** : pour la gestion des données et des fonctionnalités métier.
- **HTML/CSS/JavaScript/Bootstrap (Frontend)** : pour des interfaces utilisateur attrayantes et interactives.
- **SQLite/MySQL** : pour le stockage des données.
- **Django ORM** : pour la gestion des bases de données.

## Objectif de l'application
L'application vise à simplifier la gestion quotidienne d'une pharmacie, réduire les erreurs humaines et augmenter l'efficacité opérationnelle. Elle est idéale pour les petites et moyennes pharmacies souhaitant moderniser leur gestion.


## 📚 Contenu du Tutoriel

### Partie 1 : Premiers Pas avec Django  
- **Installation et configuration :**  
  - Apprenez à installer Python, Django, et configurer un environnement virtuel.  
  - Commandes essentielles pour démarrer un projet Django :
    - Créer un environnement virtuel : `python -m venv nom_de_la_machine_virtuelle`
    - Installer Django : `pip install django`
    - Lancer le serveur Django : `python manage.py runserver`

### Partie 2 : Structure de l’Application  
- **Modélisation des données :**  
  - Créez des modèles pour gérer les médicaments, les clients, et les transactions.  
- **ORM (Object-Relational Mapping) :**  
  - Manipulez vos bases de données en Python grâce aux ORM de Django.  
  - Générez des migrations avec : `python manage.py makemigrations` et `python manage.py migrate`.  

### Partie 3 : Interfaces Utilisateur  
- **Templates et fichiers statiques :**  
  - Utilisez HTML, CSS, et JavaScript pour concevoir des interfaces modernes.  
  - Optimisez vos templates avec `extends` et `include` pour un code plus fluide.  

### Partie 4 : Gestion des Formulaires  
- **Formulaires personnalisés et générés :**  
  - Gérez les formulaires HTML avec des vues Django et `ModelForm`.  
  - Ajoutez des validations et affichez des erreurs personnalisées.

### Partie 5 : Sécurisation de l’Application  
- Intégrez des **tokens CSRF** pour sécuriser les formulaires.  
- Implémentez des fonctionnalités avancées comme l'authentification et l'autorisation.  

### Partie 6 : Fonctionnalités Avancées  
- **Recherche et filtres :**  
  - Ajoutez une barre de recherche pour permettre aux utilisateurs de trouver facilement des produits.  
- **CRUD (Create, Read, Update, Delete) :**  
  - Gérez les données avec des vues fonctionnelles et génériques.  
  - Supprimez des produits de manière sécurisée avec **AJAX et jQuery** pour une expérience utilisateur fluide.  
- **Détails Produit :**  
  - Créez des vues pour afficher les informations détaillées des produits.  

### Partie 7 : Déploiement 🚀  
- Préparez et déployez votre application sur un serveur de production (ex. : Heroku, AWS).  

---

## 🛠️ Prérequis  
- Python 3.10+  
- Django 4.x  
- Visual Studio Code avec les extensions Python et Django  

## 📋 Commandes Essentielles Rappelées  
- **Naviguer dans un dossier :** `cd nom_du_dossier`  
- **Revenir au dossier précédent :** `cd ..`  

---


## 🚀 Ce que vous allez apprendre  
À la fin de ce tutoriel, vous serez capable de :  
- Créer et configurer un projet Django.  
- Modéliser des données pour une application métier.  
- Concevoir des interfaces utilisateurs modernes.  
- Gérer les formulaires et sécuriser les données.  
- Mettre en place des fonctionnalités avancées comme la recherche et la gestion de produits.  

## 🤝 Contributions  
Vous avez des idées ou des suggestions ? Ouvrez une **issue** ou soumettez une **pull request** !  

## 📧 Contact  
Pour toute question ou suggestion,  contactez-nous : [tel:+212 762153520](mailto:ikrammisbah65@gmail.com).  

---

Commencez dès maintenant et devenez un expert Django tout en créant une application utile et pratique ! 🎉
