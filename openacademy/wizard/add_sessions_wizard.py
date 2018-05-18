from odoo import fields, models, api


class AddSessionsWizard(models.TransientModel):
    _name = 'add_sessions_wizard'
    _rec_name = 'wizard_session'

    def get_default_session(self):
        return self._context.get('active_id')

    # wizard_session = fields.Many2one('session', string='Session', default=get_default_session)
    wizard_session = fields.Many2one('session', string='Session')
    wizard_session_attendees = fields.Many2many('res.partner',
                                                'wizard_partners_ref',
                                                string="Attendees")

    @api.multi
    def save_results_v10(self):
        for new_attendee in self.wizard_session_attendees:
            self.wizard_session.attendees.write({(4, new_attendee.id)})

    @api.multi
    def save_results(self):
        for new_attendee in self.wizard_session_attendees:
            self.wizard_session.attendees |= new_attendee
