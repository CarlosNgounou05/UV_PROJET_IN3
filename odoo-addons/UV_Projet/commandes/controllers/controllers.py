# -*- coding: utf-8 -*-
# from odoo import http


# class Commandes(http.Controller):
#     @http.route('/commandes/commandes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/commandes/commandes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('commandes.listing', {
#             'root': '/commandes/commandes',
#             'objects': http.request.env['commandes.commandes'].search([]),
#         })

#     @http.route('/commandes/commandes/objects/<model("commandes.commandes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('commandes.object', {
#             'object': obj
#         })

