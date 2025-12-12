from unittest import TestCase
from msad_query import getUser, MSAD_USER_FIELDS
from msad_query.msadqExceptions import MSADQueryException
from tests.common import loadUnittestParameters, emptyDict
import getpass

PARAMETERS = loadUnittestParameters()


class TestGetUser(TestCase):
    def test_a_usr(self):
        user = getUser(
            PARAMETERS.get("domainUser", getpass.getuser()), PARAMETERS.get("domainController", "localhost")
        )
        self.assertIsInstance(user, dict)
        self.assertTrue(MSAD_USER_FIELDS.GUID in user)

    def test_b_none(self):
        user = getUser("sjaqp887408cvd", PARAMETERS.get("domainController", "localhost"), onError=emptyDict)
        self.assertFalse(user)

    def test_c_fail(self):
        self.assertRaises(
            MSADQueryException, getUser, "sjaqp887408cvd", PARAMETERS.get("domainController", "localhost")
        )
