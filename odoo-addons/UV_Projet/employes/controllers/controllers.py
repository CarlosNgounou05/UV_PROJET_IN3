# -*- coding: utf-8 -*-
# from odoo import http


# class Employes(http.Controller):
#     @http.route('/employes/employes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employes/employes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employes.listing', {
#             'root': '/employes/employes',
#             'objects': http.request.env['employes.employes'].search([]),
#         })

#     @http.route('/employes/employes/objects/<model("employes.employes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employes.object', {
#             'object': obj
#         })

