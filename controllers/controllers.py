# -*- coding: utf-8 -*-
#from openerp import http

# class Autoservice(http.Controller):
#     @http.route('/autoservice/autoservice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/autoservice/autoservice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('autoservice.listing', {
#             'root': '/autoservice/autoservice',
#             'objects': http.request.env['autoservice.autoservice'].search([]),
#         })

#     @http.route('/autoservice/autoservice/objects/<model("autoservice.autoservice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('autoservice.object', {
#             'object': obj
#         })