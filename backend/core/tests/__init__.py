import unittest

from google.appengine.ext import testbed


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.tb = testbed.Testbed()
        self.tb.setup_env(current_version_id='testbed.version')
        self.tb.activate()
        self.tb.init_user_stub()
        self.tb.init_datastore_v3_stub()
        self.tb.init_memcache_stub()

    def tearDown(self):
        self.tb.deactivate()
