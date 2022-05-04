

import xml.dom.minidom as md

def main(x,y):
    file = md.parse("test_payload1.xml")


    file.getElementsByTagName("DEPART")[ 0 ].childNodes[ 0 ].nodeValue = str(x)
    file.getElementsByTagName("RETURN")[ 0 ].childNodes[ 0 ].nodeValue = str(y)

    with open( "test_payload.xml", "w" ) as fs: 
        fs.write(file.toxml())
        fs.close()

    
x = int(input())
y = int(input())

main(x,y)





















