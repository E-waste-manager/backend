from xml.etree import ElementTree as ET

source = '''<root>
<level>
  <name>Matthias</name>
  <age>23</age>
  <gender>Male</gender>
</level>
<level>
  <name>Foo</name>
  <age>24</age>
  <gender>Male</gender>
</level>
<level>
  <name>Bar</name>
  <age>25</age>
  <gender>Male</gender>
</level>
</root>'''

root = ET.fromstring(source)
levels = root.findall('.//level')
print(levels)
for level in levels:
    name = level.find('name').text
    age = level.find('age').text
    print (name, age)