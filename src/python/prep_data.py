# -*- coding: utf-8 -*-
""" Short script to prep XML files for text analysis """
import os

import click
from analysis.parser import parse_bill_xml
from analysis.settings import TXT_FOLDER, XML_FOLDER

@click.command()
@click.argument('data_folder')
def main(data_folder=None):
    """ Prep BILL xml data for analysis """
    input_folder = os.path.join(data_folder, XML_FOLDER)
    output_folder = os.path.join(data_folder, TXT_FOLDER)

    click.secho( f'Parsing & prepping files in "{data_folder}"', fg='green' )

    # Loop through each XML file in the data_folder.
    with click.progressbar( os.listdir( input_folder ) ) as file_list:
        for filename in file_list:
            # Grab the filename without the extension.
            (root, ext) = os.path.splitext( filename )
            # Only parse XML files.
            if ext != '.xml':
                continue
            # Parse the bill XML
            text_content = parse_bill_xml( os.path.join( input_folder, filename ) )
            if text_content is None:
                continue

            # Write the text content to a txt file.
            with open( os.path.join( output_folder, f'{root}.txt' ), 'w' ) as fhand:
                fhand.write( text_content )


if __name__ == '__main__':
    main()
