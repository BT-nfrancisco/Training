from odoo.tests import common
# from unittest2 import SkipIf

class TestWizard(common.TransactionCase):

    def setUp(self):
        super(TestWizard, self).setUp()
        # check sessions initial attendees
        self.initial_session_1 = self.env.ref('openacademy.session_1')
        self.initial_session_2 = self.env.ref('openacademy.session_2')
        # add attendees through wizard
        self.partner_1 = self.env.ref('base.res_partner_1')
        self.partner_2 = self.env.ref('base.res_partner_2')

        self.wizard_obj = self.env['openacademy.wizard']

        self.wizard = self.wizard_obj.create({'attendee_ids': [(4, self.partner_1.id),
                                                               (4, self.partner_2.id)],
                                              'session_ids': [(4, self.initial_session_1.id),
                                                              (4, self.initial_session_2.id)]})

    def tearDown(self):
        super(TestWizard, self).tearDown()

    def test_attendees_adding(self):
        self.wizard.subscribe()
        #check sessions final attendess
        attendee_list_ses1 = self.initial_session_1.attendee_ids
        attendee_list_ses2 = self.initial_session_2.attendee_ids
        self.assertIn(self.partner_1, attendee_list_ses1, 'Not p1 in session 1')
        self.assertIn(self.partner_2, attendee_list_ses1, 'Not p2 in session 1')
        self.assertIn(self.partner_1, attendee_list_ses2, 'Not p1 in session 2')
        self.assertIn(self.partner_2, attendee_list_ses2, 'Not p2 in session 2')
