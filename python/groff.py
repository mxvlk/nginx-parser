import xml.etree.ElementTree as ET

title = "Nginx Configuration"
authors = "Max"

def convert_xml_to_groff(xml_str):
    root = ET.fromstring(xml_str)

    def process_element(element):
        output = ""

        if element.tag == 'NginxConf':
            for child in element:
                output += process_element(child)
        elif element.tag == 'Section':
            section_class = element.get('class', 'default')
            output += f'.NH\n{section_class}\n'
            for child in element:
                output += process_element(child)
        elif element.tag == 'Subsection':
            subsection_class = element.get('class', 'default')
            output += f'.SH \n {subsection_class}\n'
            for child in element:
                output += process_element(child)
        elif element.tag == 'Subsubsection':
            subsubsection_class = element.get('class', 'default')
            path = element.get('path', '')
            modifier = element.get('modifier', '')
            output += f'.SH \n {subsubsection_class} {path} {modifier}\n'
            for child in element:
                output += process_element(child)
        elif element.tag == 'Key':
            key_class = element.get('class', 'default')
            text = element.text.strip()
            output += f'.PP \n.B "{key_class}"\n{text}\n'

        return output

    document = ".TL\n" + title + "\n.AU\n" + authors + "\n" + ".NH\nglobal\n"
    groff_output = document + process_element(root)
    return groff_output


f = open("./output/output_xml.xml", "r")
text = f.read()

file = open("./output/output_groff.ms", "w")
file.write(convert_xml_to_groff(text))
file.close()