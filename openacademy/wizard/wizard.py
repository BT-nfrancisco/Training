from odoo import fields, models, api


class Wizard(models.TransientModel):
    _name = 'wizard'
    _rec_name = 'wizard_session'

    def get_default_session(self):
        return self._context.get('active_id')

    # wizard_session = fields.Many2one('session', string='Session', default=get_default_session)
    wizard_session = fields.Many2one('session', string='Session')
    attendees = fields.Many2many('res.partner', 'partners_ref',
                                 string="Attendees")

    @api.one
    def save_results_v10(self):
        for new_attendee in self.attendees:
            self.wizard_session.attendees.write({(4, new_attendee.id)})

    def save_results(self):
        self.wizard_session.attendees |= self.attendees
