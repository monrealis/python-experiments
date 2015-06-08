import unittest
import xml.etree.ElementTree as ET

class XmlVisualizerTest(unittest.TestCase):
    def setUp(self):
        super(XmlVisualizerTest, self).setUp()

    def test_visualizes_root_element(self):
        self.assertEqual('root', XmlVisualizer('<root />').visualize())


class XmlVisualizer:
    def __init__(self, xml):
        self.tree = ET.fromstring(xml)

    def visualize(self):
        return str(self.tree.tag)