#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Verilmi dictionary-ni XML formatına serialize edib fayla yazır.
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    result = {}
    for child in root:
        # Hamısını string kimi saxlayırıq (XML yalnız mətn saxlayır)
        result[child.tag] = child.text

    return result

if __name__ == "__main__":
    sample_dict = {"ad": "Ali", "yas": 25, "seher": "Baki"}

    # Serialize
    serialize_to_xml(sample_dict, "data.xml")
    print("XML faylı yaradıldı: data.xml")

    # Deserialize
    loaded_dict = deserialize_from_xml("data.xml")
    print("XML-dən oxunan dictionary:", loaded_dict)

