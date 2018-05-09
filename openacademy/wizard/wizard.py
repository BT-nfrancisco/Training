from odoo import fields, models, api


class Wizard(models.TransientModel):
    _name = 'wizard'
    _rec_name = 'wizard_session'

    wizard_session = fields.Many2one('session', string='Session')
    attendees = fields.Many2many('res.partner', 'partners_ref', string="Attendees")
