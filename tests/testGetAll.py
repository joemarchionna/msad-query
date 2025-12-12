from unittest import TestCase
from msad_query import getAllUsers
from msad_query.msadqExceptions import MSADQueryException
from tests.common import loadUnittestParameters, emptyList

PARAMETERS = loadUnittestParameters()


class TestGetAll(TestCase):
    def test_a_all(self):
        users = getAllUsers(PARAMETERS.get("domainController", "localhost"))
        self.assertIsInstance(users, list)
        self.assertLess(0, len(users))
        self.assertIsInstance(users[0], dict)

    def test_b_none(self):
        users = getAllUsers("myDC", onError=emptyList)
        self.assertIsInstance(users, list)
        self.assertEqual(0, len(users))

    def test_c_fail(self):
        self.assertRaises(MSADQueryException, getAllUsers, "myDC")
