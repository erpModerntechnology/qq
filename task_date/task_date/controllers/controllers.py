# -*- coding: utf-8 -*-
# from odoo import http


# class TaskDate(http.Controller):
#     @http.route('/task_date/task_date/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_date/task_date/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_date.listing', {
#             'root': '/task_date/task_date',
#             'objects': http.request.env['task_date.task_date'].search([]),
#         })

#     @http.route('/task_date/task_date/objects/<model("task_date.task_date"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_date.object', {
#             'object': obj
#         })
