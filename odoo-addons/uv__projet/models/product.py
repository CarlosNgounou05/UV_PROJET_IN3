from odoo import models, fields, api

class Products(models.Model):
    _name="uv__projet.products"
    _description="AGRIPro Products"

    id=fields.Integer("Identifiant",required=True)
    libelle=fields.Char("Libelle",required=True)
    description=fields.Char("Description",required=True)
    prix_unitaire=fields.Integer("Prix unitaire(XAF)",required=True)
    type=fields.Selection([('Produit Fini','Produit Fini'),('Intrant','Intrant')],"Type Du Produit")
    quantite=fields.Integer("Quantite Du Produit(Kg)",required=True)

    