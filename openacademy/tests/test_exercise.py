from odoo.tests import common


class TestOpenacademy(common.TransactionCase):

    def setUp(self):
        print("setUp")
        super(TestOpenacademy, self).setUp()

    def tearDown(self):
        super(TestOpenacademy, self).tearDown()

    def test_numer_of_seats(self):
        self.assertTrue(False, "True is not False")
