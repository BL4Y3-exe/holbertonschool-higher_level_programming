#!/usr/bin/python3
"""This module contains serialize_to_xml and deserialize_from_xml funcitons."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Function serializes dictoinary into xml document.

    Args:
        dictoinary: pyton object.
        filename: path to the xml document.
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    except Exception:
        return None


def deserialize_from_xml(filename):
    """
    Function deserializes aml document into dictionary.

    Args:
        filename: path to the xml document.

    Returns:
        dict: deserialized xml document.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        for child in root:
            result[child.tag] = child.text

        return result

    except Exception:
        return None
