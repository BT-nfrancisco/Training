from datetime import datetime, timedelta

from odoo.tests import common
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT


class TestOpenacademy(common.TransactionCase):

    def setUp(self):
        super(TestOpenacademy, self).setUp()

        self.env['res.partner'].create({
            'name': 'New Partner',
            'email': 'newpartnerm@example.com',
        })

    def tearDown(self):
        super(TestOpenacademy, self).tearDown()

    def xtest_numer_of_seats(self):
        session_model = self.env['session']
        sessions_ids = session_model.search([])

        partner_model = self.env['res.partner']
        partner = partner_model.search([('name', '=', 'New Partner')])

        # initial_session.write({'attendee_ids': [(4, partner.id)]})

        first_session = sessions_ids[0]
        attendees_num_before = len(first_session.attendees)
        # first_session.write({'attendees': [4, partner.id]})

        first_session.attendees |= partner

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
        sessions_ids = session_model.search([])

        first_session = sessions_ids[0]

        duration_before_change = first_session.duration
        end_date_before_change = first_session.end_date

        end_date_object = datetime.strptime(end_date_before_change, DATE_FORMAT)
        update_days = timedelta(days=2)

        end_date_object = end_date_object + update_days

        end_date_string = end_date_object.strftime(DATE_FORMAT)

        first_session.write({'end_date': end_date_string})

        duration_after_change = first_session.duration

        self.assertNotEqual(duration_before_change, duration_after_change,
                            "BAD")
