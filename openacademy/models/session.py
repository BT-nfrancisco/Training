# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT


class Session(models.Model):
    _name = 'session'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    start_date = fields.Date(string='Start date', default=fields.Date.today)
    duration = fields.Integer(string='Duration')
    number_of_seats = fields.Integer(string='Number of seats')
    related_course = fields.Many2one('course', string='Course')
    instructor = fields.Many2one('res.partner', string='Instructor')
    attendees = fields.Many2many('res.partner', 'session_partner_ref', string='Attendees')
    taken_seats = fields.Float(compute='_apply_taken_seats', string='Taken seats')
    end_date = fields.Date(string='End Date', compute='_apply_end_date', inverse='_set_duration')
    course_description = fields.Text(related='related_course.description', store=False, string='Course description')

    @api.depends('number_of_seats', 'attendees')
    def _apply_taken_seats(self):
        for rec in self:
            rec.taken_seats = len(rec.attendees) * 100 / rec.number_of_seats

    @api.depends('start_date', 'taken_seats')
    def _apply_end_date(self):
        for rec in self:
            duration = rec.duration
            update_days = timedelta(days=duration)

            datetime_object = datetime.strptime(rec.start_date, DATE_FORMAT)
            datetime_object = datetime_object + update_days

            rec.end_date = datetime_object.strftime(DATE_FORMAT)

    def _set_duration(self):
        for rec in self:
            end_date_object = datetime.strptime(rec.end_date, DATE_FORMAT)
            duration_object = timedelta(days=rec.duration)
            start_date = end_date_object + duration_object
            rec.start_date = start_date.strftime(DATE_FORMAT)
