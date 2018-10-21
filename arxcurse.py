import click
import requests
from xml.etree import ElementTree as ET
import re

def recurselem(elem, lambdaf, indent=0):
    for child in elem.findall('*'):
        lambdaf(child,indent)
        recurselem(child, lambdaf, indent + 1)

@click.group()
def main():
    """
    bla
    """
    pass

@main.command()
@click.argument('field')
def search(field):
    """search id"""
    url = 'http://export.arxiv.org/api/query?search_query=all:'+str(field)+'&start=0&max_results=1'
    xml_data = requests.get(url).text
    print(xml_data)

    global xml
    xml = ET.fromstring(xml_data)
    recurselem(xml, lambda a,b : print(' ' * 5 *  b + a.tag) ) 


if __name__ == "__main__":
    main()
