import unittest
import xml.etree.ElementTree as ET

class XmlVisualizerTest(unittest.TestCase):
    def setUp(self):
        super(XmlVisualizerTest, self).setUp()

    def test(self):
        ET.fromstring('<root />')