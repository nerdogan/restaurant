# -*- coding: utf-8 -*-



string1="SIRMAGRUP İÇECEK A.Ş DENİZBANK SIRMA ASAS YEME ICME ODEME havale bedeli"
string2="SIRMAGRUP İÇECEK SAN TİC AŞ "
elem1 = [x for x in string1.split()]
elem2 = [x for x in string2.split()]

for item in elem1:
    print "1"
    if item in elem2:
        print "2"
        print item