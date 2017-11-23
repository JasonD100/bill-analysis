# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from typing import List


def grab_text(root: ET.Element) -> str:
    """ Grab all text data in a <text> tag """
    text = []

    if root.text:
        text.append( root.text.strip() )

    for child in root.getchildren():
        text.append(grab_text(child))

    return ' '.join(text)


def find_text_tags(root: ET.Element) -> List[str]:
    """ Find all <text> tag children and grab the text content

    Args:
        root (ElementTree.Element): Root XML tag to start search
    """
    text = []
    for child in root:
        if child.getchildren():
            text.extend( find_text_tags( child.getchildren() ) )

        if child.tag == 'text':
            text.append( grab_text( child ) )

    return text


def parse_bill_xml(file_path: str) -> str:
    """ Read & parse a bill xml file

    Args:
        file_path (str): XML file path.

    Returns:
        str: A combined text
    """
    bill_text = open( file_path, 'r' ).read()

    legislation = ET.fromstring( bill_text ).find( './legis-body' )
    if legislation is None:
        return None

    return ' '.join( find_text_tags( legislation ) )