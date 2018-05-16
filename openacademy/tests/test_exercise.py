from datetime import datetime, timedelta

from odoo.tests import common
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT


def create_two_partners(self):
    self.env['res.partner'].create({
        'name': 'New Partner 1',
        'email': 'newpartnerm@example.com',
    })

    self.env['res.partner'].create({
        'name': 'New Partner 2',
        'email': 'newpartnerm@example.com',
    })


class TestOpenacademy(common.TransactionCase):

    def setUp(self):
        super(TestOpenacademy, self).setUp()

    def tearDown(self):
        super(TestOpenacademy, self).tearDown()

    def test_numer_of_seats(self):
        session_model = self.env['session']
        sessions_ids = session_model.search([])

        partner_model = self.env['res.partner']
        create_two_partners(self)
        partner = partner_model.search([('name', '=', 'New Partner 1')])

        first_session = sessions_ids[0]
        attendees_num_before = len(first_session.attendees)

        first_session.write({'attendees': [(4, partner.id)]})
        # first_session.attendees |= partner #V11

        found = False

        for attendee in first_session.attendees:
            if attendee.id == partner.id:
                found = True

        self.assertTrue(found,
                        "Added partner not found in first session attendees list")

        attendees_num_after = len(first_session.attendees)

        self.assertEqual(attendees_num_before, attendees_num_after - 1,
                         "Attendees have not incremented correctly")

    def test_duration_update(self):
        session_model = self.env['session']
        sessions = session_model.search([])

        first_session = sessions[0]

        duration_before_change = first_session.duration
        end_date_before_change = first_session.end_date

        end_date_object = datetime.strptime(end_date_before_change,
                                            DATE_FORMAT)
        update_days = timedelta(days=2)

        end_date_object = end_date_object + update_days

        end_date_string = end_date_object.strftime(DATE_FORMAT)

        first_session.write({'end_date': end_date_string})

        duration_after_change = first_session.duration

        self.assertNotEqual(duration_before_change, duration_after_change,
                            "Duration has not changed after increasing the end date by 2 days")

    def test_adding_attendes_wizard(self):
        session_model = self.env['session']
        wizard_model = self.env['wizard']
        partner_model = self.env['res.partner']

        sessions = session_model.search([])
        first_session = sessions[0]

        create_two_partners(self)

        partner1 = partner_model.search([('name', '=', 'New Partner 1')])
        partner2 = partner_model.search([('name', '=', 'New Partner 2')])

        # first_session.write({'attendees': [(4, partner.id)]})

        my_wizard = wizard_model.create({
            'wizard_session': first_session.id,
            'attendees': [(4, partner1.id), (4, partner2.id)]
        })

        my_wizard.save_results()

        sessions = session_model.search([])
        first_session = sessions[0]

        self.assertIn(partner1, first_session.attendees,
                      'Parter1 not in session')
        self.assertIn(partner2, first_session.attendees,
                      'Parter2 not in session')
