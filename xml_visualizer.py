import unittest
import xml.etree.ElementTree as ET

class XmlVisualizerTest(unittest.TestCase):
    def setUp(self):
        super(XmlVisualizerTest, self).setUp()


    def test_visualizes_root_element(self):
        self.assertEqual('root', self.visualize('<root />'))

    @unittest.SkipTest
    def test_visualizes_root_element_with_ns(self):
        self.assertEqual('root', self.visualize('<root xmlns="urn:test:test" />'))

    @unittest.SkipTest
    def test_visualizes_root_element_with_prefix(self):
        self.assertEqual('root', self.visualize('<r:root xmlns:r="urn:test:test" />'))

    def visualize(self, xml):
        return XmlVisualizer(xml).visualize()


class XmlVisualizer:
    def __init__(self, xml):
        self.tree = ET.fromstring(xml)

    def visualize(self):
        return str(self.tree.tag)


    def dump(self, obj):
        for attr in dir(obj):
            print("obj.%s = %s" % (attr, getattr(obj, attr)))

