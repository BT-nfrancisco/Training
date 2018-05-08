# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Session(models.Model):
    _name = 'session'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    start_date = fields.Date(string='Start date', default=fields.Date.today)
    duration = fields.Integer(string='Duration')
    number_of_seats = fields.Integer(string='Number of seats')
    related_course = fields.Many2one('course', string='Course')
    instructor = fields.Many2one('res.partner', string='Instructor')
    atendees = fields.Many2many('res.partner', 'session_partner_ref', string='Atendees')
