def startWarpperElement(nameSpace, elName):
    return '<?xml version="1.0" encoding="UTF-8"?><xsd:schema targetNamespace="%s" xmlns="%s" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><xsd:complexType name="%s"><xsd:sequence>' % (nameSpace, nameSpace, elName)


def endWarpperElement():
    return '</xsd:sequence></xsd:complexType></xsd:schema>'


def createStringElement(elName):
    return '<xsd:element name="%s" type="xsd:string" minOccurs="0" />' % (elName)


def startComplexElement(elName):
    return '<xsd:element name="%s" minOccurs="0" ><xsd:complexType><xsd:sequence>' % (elName)


def endComplexElement():
    return '</xsd:sequence></xsd:complexType></xsd:element>'
