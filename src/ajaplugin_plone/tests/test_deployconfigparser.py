import os
import unittest
from ajaplugin_plone.config import DeployConfigParser

config_path = "{path}/config.cfg".format(
    path=os.path.dirname(os.path.abspath(__file__)))


class DeployConfigParserTests(unittest.TestCase):

    def setUp(self):
        self.parser = DeployConfigParser()

    def test_parser_tuple(self):
        self.assertTrue(hasattr(self.parser, 'get_tuple'))

    def test_parser_list(self):
        self.assertTrue(hasattr(self.parser, 'get_list'))
        self.assertTrue(hasattr(self.parser, 'get_list_int'))

    def test_parser_read(self):
        self.parser.read(config_path)
        testconfig_ignores = self.parser.get_list('plone:deploy', "ignores")
        expected_list = ["*.old", "*.pid", "var/filestorage", "var/blobstorage"]
        self.assertEqual(expected_list, testconfig_ignores)


if __name__ == '__main__':
    unittest.main()