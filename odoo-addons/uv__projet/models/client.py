from odoo import models, fields, api

class Client(models.Model):
    _name="uv__projet.client"
    _description="AGRIPro clients"

    id=fields.Integer("Identifiant",required=True)
    nom=fields.Char("Nom",required=True)
    prenom=fields.Char("Prenom")
    adresse=fields.Char("Adresse",required=True)
    contact=fields.Char("Contact",required=True)
    ville=fields.Char("ville",required=True)

    