# -*- coding: utf-8 -*-
# from odoo import http


# class UvProjet(http.Controller):
#     @http.route('/uv__projet/uv__projet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uv__projet/uv__projet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('uv__projet.listing', {
#             'root': '/uv__projet/uv__projet',
#             'objects': http.request.env['uv__projet.uv__projet'].search([]),
#         })

#     @http.route('/uv__projet/uv__projet/objects/<model("uv__projet.uv__projet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uv__projet.object', {
#             'object': obj
#         })

