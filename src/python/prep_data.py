# -*- coding: utf-8 -*-
""" Short script to prep XML files for text analysis """
import os
import sys

import click
from analysis.parser import parse_bill_xml


def main():
    """ Prep BILL xml data for analysis """
    data_folder = sys.argv[1]
    click.secho( f'Parsing & prepping files in "{data_folder}"', fg='green' )

    # Loop through each XML file in the data_folder.
    with click.progressbar( os.listdir( data_folder ) ) as file_list:
        for filename in file_list:
            # Grab the filename without the extension.
            (root, ext) = os.path.splitext( filename )
            # Only parse XML files.
            if ext != '.xml':
                continue
            # Parse the bill XML
            text_content = parse_bill_xml( os.path.join( data_folder, filename ) )
            if text_content is None:
                continue
            # Write the text content to a txt file.
            with open( os.path.join( data_folder, f'{root}.txt' ), 'w' ) as fhand:
                fhand.write( text_content )


if __name__ == '__main__':
    main()
