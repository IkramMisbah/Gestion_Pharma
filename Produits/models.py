from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name

#class pour les produits
class Produits(models.Model):
    name=models.CharField(max_length=250)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    price=models.IntegerField()
    quantite=models.PositiveBigIntegerField(default=0)
    date_ajout=models.DateTimeField(auto_now_add=True)
    date_expiration=models.DateField()
    image=models.ImageField(null=True,blank=True,upload_to='media/')
    description=models.TextField()

    class Meta:
        ordering=['-date_ajout']


    def statut_quantite(self):
        if self.quantite==0:
            return 'red'
        elif self.quantite<=10:
            return 'orange'
        else :
            return 'green'
    def __str__(self):
        return self.name


class Customers(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Vente(models.Model):
    produit=models.ForeignKey(Produits,on_delete=models.CASCADE)
    sale_date=models.DateTimeField(auto_now_add=True)
    quantite=models.PositiveBigIntegerField()
    customer=models.CharField(max_length=100)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    

    def __str__(self):
        return self.produit
    
#class des factures 

class Facture_Client(models.Model):
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE)
    quantite=models.PositiveBigIntegerField()
    date_achat=models.DateTimeField(auto_now_add=False)
    total_amount=models.ForeignKey(Produits,on_delete=models.CASCADE)
    produit=models.ForeignKey(Produits,on_delete=models.CASCADE,related_name='facture_produit')

    def __str__(self):
        return f"le recu de {self.customer.name}"
    