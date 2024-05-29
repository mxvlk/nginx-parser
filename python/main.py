import re
from pypeg2 import *
from pypeg2.xmlast import thing2xml
import xml.dom.minidom

def remove_comments(text):
    lines = text.split("\n")

    for i in range(len(lines)):
        line = lines[i]

        comment_index = line.find("#")
        if comment_index != -1:
            lines[i] = line[:comment_index]

    return '\n'.join(lines)


value = re.compile(r"[\w|\s|\/|\.|\-|\:|\=|\"|\'|\[|\]|\$|\^|\\|\||\(|\)]+")
internal_value = re.compile(r"[\w|\/|\.|\-|\:|\=|\"|\'|\[|\]|\$|\^|\\|\||\(|\)]+")
path = re.compile(r"^\S+")

class Key(str):
    grammar = attr("class", Symbol), value, ";"

class Subsubsection(Namespace):
    grammar = attr("class", Symbol), attr("path", path), optional(attr("modifier", internal_value)), "{", endl, maybe_some(Key), "}"

class Subsection(Namespace):
    grammar = attr("class", Symbol), optional(attr("description",word)),"{", endl, maybe_some(Key), maybe_some(Subsubsection), "}"

class Section(Namespace):
    grammar = attr("class", Symbol), "{", endl, maybe_some(Key), maybe_some(Subsection) , "}"

class NginxConf(Namespace):
    grammar = maybe_some(Key), maybe_some(Section)


conf = open("./input/nginx.conf", "r")
text_without_comments = remove_comments(conf.read())
thing = parse(text_without_comments, NginxConf)

xml_file = open("./output/output_xml.xml", "w")
xml_file.write(xml.dom.minidom.parseString(thing2xml(thing, pretty=True).decode()).toprettyxml(indent="    "))
xml_file.close()

