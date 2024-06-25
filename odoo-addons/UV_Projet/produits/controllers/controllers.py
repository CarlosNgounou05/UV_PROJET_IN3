# -*- coding: utf-8 -*-
# from odoo import http


# class Produits(http.Controller):
#     @http.route('/produits/produits', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/produits/produits/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('produits.listing', {
#             'root': '/produits/produits',
#             'objects': http.request.env['produits.produits'].search([]),
#         })

#     @http.route('/produits/produits/objects/<model("produits.produits"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('produits.object', {
#             'object': obj
#         })

