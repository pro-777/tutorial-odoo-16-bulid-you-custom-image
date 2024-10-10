# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class Users(models.Model):
    _inherit = 'res.users'

    custom_number = fields.Char(string="Number", readonly=True, copy=False)

    def init(self): #for old users generation of number.
        print('---------start---------')
        search_user = self.env['res.users'].search([('custom_number', '=', False)])
        for user in search_user:
            if user.has_group('base.group_user'):
                user.custom_number = self.env['ir.sequence'].next_by_code('res.users.sequence.code')
            elif user.has_group('base.group_portal'):
                user.custom_number = self.env['ir.sequence'].next_by_code('res.users.sequence.code.portal')

        

    @api.model_create_multi
    def create(self, vals_list):
        users = super(Users, self).create(vals_list)
        for user in users:
            if user.has_group('base.group_user'):
                user.custom_number = self.env['ir.sequence'].next_by_code('res.users.sequence.code')
            elif user.has_group('base.group_portal'):
                user.custom_number = self.env['ir.sequence'].next_by_code('res.users.sequence.code.portal')

        return users
    
