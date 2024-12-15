from django.forms import ModelForm
from .models import Produits,Vente
from django import forms


#class pour creer le formulaire genere par django(pls securisé que les formulairs personnalisé avec html)
class AjoutProduit(ModelForm):
  
    class Meta:
        model = Produits
        fields = ['name', 'category', 'price', 'quantite', 'date_expiration', 'image', 'description']
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'placeholder': 'Entrez le nom du produit',
                    'class':'form-control'
                }
            ),

            'category': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),

            'price' : forms.NumberInput(
                attrs= {
                    'placeholder': 'Entrez le prix du prodtuit',
                    'class': 'form-control'
                }
            ),
            
            'quantite': forms.NumberInput(
                attrs={
                    'placeholder': 'Entrez la quantité',
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'class': 'form-control',
                    'rows': 2
                }
            ),
            'date_expiration': forms.DateInput(
                attrs={
                    'placeholder': 'Date d\'expiration',
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control-file'
                }
            )
        }


    def __init__(self, *args, **kwargs):
        super(AjoutProduit, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages = {
            'required': 'Le nom du produit est obligatoire',
            'invalid': 'Veuillez entrer un nom correct.'
        }
        self.fields['category'].error_messages = {
            'required': 'La catégorie est obligatoire',
            'invalid': 'Veuillez sélectionner une catégorie valide'
        }
        self.fields['price'].error_messages = {
            'required': 'Le prix du produit est obligatoire',
            'invalid': 'Veuillez entrer un prix correct.'
        }
        self.fields['quantite'].error_messages = {
            'required': 'La quantité est obligatoire.',
            'invalid': 'Veuillez entrer une quantité valide.'
        }
        self.fields['description'].error_messages = {
            'required': 'La description est obligatoire.',
            'invalid': 'Veuillez entrer une description valide.'
        }
        self.fields['date_expiration'].error_messages = {
            'required': "La date d'expiration du produit est obligatoire.",
            'invalid': 'Veuillez entrer une date d\'expiration valide.'
        }



# Définition de la classe de formulaire AjoutVente
class AjoutVente(forms.ModelForm):
    # Champ pour saisir la quantité de produit
    quantite = forms.IntegerField(
        # Texte d'aide affiché à côté du champ
        help_text='Veuillez entrer la quantité de produit',
        # Spécifie que ce champ est obligatoire
        required=True,
        # Messages d'erreur personnalisés pour ce champ
        error_messages={
            'required': 'La quantité est obligatoire.',  # Si le champ est vide
            'invalid': 'Veuillez entrer une quantité raisonnable.'  # Si la saisie n'est pas un entier
        }
    )
 
    # Champ pour saisir le nom du client
    customer = forms.CharField(
        # Texte d'aide affiché à côté du champ
        help_text='Veuillez entrer le nom',
        # Spécifie que ce champ est obligatoire
        required=True,
        # Limite la longueur maximale de la saisie à 100 caractères
        max_length=100,
        # Messages d'erreur personnalisés pour ce champ
        error_messages={
            'required': 'Le nom du client est obligatoire.',  # Si le champ est vide
            'invalid': 'Veuillez entrer un nom correct.'  # Si la saisie est invalide
        }
    )
    
    # Classe interne Meta pour configurer le formulaire
    class Meta:
        # Lien avec le modèle Vente
        model = Vente  # Assurez-vous que Vente est le modèle correct
        # Définition des champs du modèle à inclure dans le formulaire
        fields = ['quantite', 'customer']

        # Personnalisation de l'apparence des champs via des widgets
        widgets = {
            'customer': forms.TextInput(attrs={
                'placeholder': "Nom du client",  # Texte d'exemple affiché dans le champ
                'class': 'form-control'  # Classe CSS pour styliser le champ (par ex. Bootstrap)
            }),
            'quantite': forms.TextInput(attrs={
                'placeholder': "La quantité",  # Texte d'exemple affiché dans le champ
                'class': 'form-control'  # Classe CSS pour styliser le champ
            }),
        }


