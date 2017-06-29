#!/usr/bin/python
import sys
from lxml import etree

ns={'ns0':'http://www.deegree.org/datasource/feature/sql'}

tree = etree.parse(open(sys.argv[1]))

for featureType in tree.xpath('//ns0:FeatureTypeMapping', namespaces=ns):
  name=featureType.get('name').replace(':','.') + '_'
  for fidMapping in featureType.xpath('./ns0:FIDMapping', namespaces=ns):
    prefix=fidMapping.get('prefix')
    print prefix
    fidMapping.set('prefix',name)
  print name

tree.write(sys.stdout, encoding='utf-8', pretty_print=True)
