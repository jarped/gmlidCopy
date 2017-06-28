#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET
tree = ET.parse(sys.argv[1])

ns='{http://www.deegree.org/datasource/feature/sql}'

for featureType in tree.findall('.//'+ns+'FeatureTypeMapping'):
  name=featureType.attrib['name'].replace(':','.') + '_'
  featureType.find('./'+ns+'FIDMapping').attrib['prefix']=name

tree.write('test.xml')
