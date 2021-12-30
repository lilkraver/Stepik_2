from xml.etree import ElementTree
a = input()
root = ElementTree.fromstring(a)

d = {'red': 0, 'green': 0, 'blue': 0}   

def getChildren(root, level=1):
   d[root.attrib['color']] += level
   for child in root:
     getChildren(child, level + 1)

getChildren(root)
print(d.get('red'), d.get('green'), d.get('blue'), end = " ")
