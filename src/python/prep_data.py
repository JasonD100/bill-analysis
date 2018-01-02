# -*- coding: utf-8 -*-
""" Script to prep XML files for text analysis """
import os
import pickle

import click
from analysis.parser import parse_bill_xml
from analysis.settings import TXT_FOLDER, XML_FOLDER, TOKEN_FOLDER
from analysis.corpus import txt_to_token


def check_file( filename: str, ext: str ) -> str:
    """ Check to see if <filename> matches <ext> and returns the filename
        without the extension if so.
    """
    # Grab the filename without the extension.
    (root, file_ext) = os.path.splitext( filename )
    if file_ext != f'.{ext}':
        return None
    return root


@click.command()
@click.argument('data_folder')
def main(data_folder=None):
    """ Setup intermediary data for analysis.

        1. Parse BILL xml data into plain txt and store results.
        2. Tokenzize the plain txt and store results.
    """
    xml_path = os.path.join( data_folder, XML_FOLDER )
    txt_path = os.path.join( data_folder, TXT_FOLDER )
    token_path = os.path.join( data_folder, TOKEN_FOLDER )

    # Loop through each XML file in the data_folder.
    click.secho( f'Parsing XML files in "{xml_path}"', fg='green' )
    with click.progressbar( os.listdir( xml_path ) ) as file_list:
        for filename in file_list:
            root = check_file( filename, 'xml' )
            if not root:
                continue

            # Skip over files we've already processed.
            output_file = os.path.join( txt_path, f'{root}.txt' )
            if os.path.exists( output_file ):
                continue

            # Parse the bill XML
            text_content = parse_bill_xml( os.path.join( xml_path, filename ) )
            if text_content is None:
                continue

            # Write the text content to a txt file.
            with open( output_file, 'w' ) as fhand:
                fhand.write( text_content.strip() )

    # Loop through each txt file and tokenize the plain text
    click.secho( f'Tokenizing plain txt files in "{txt_path}"', fg='green' )
    with click.progressbar( os.listdir( txt_path ) ) as file_list:
        for filename in file_list:
            root = check_file( filename, 'txt' )
            if not root:
                continue

            # Skip over files we've already processed.
            output_file = os.path.join( token_path, f'{root}.pickle' )
            if os.path.exists( output_file ):
                continue

            # Tokenize the plain txt
            txt_in = os.path.join( txt_path, filename )
            txt_out = os.path.join( token_path, f'{root}.pickle' )
            with open( txt_in, 'r' ) as fhand:
                tokens = txt_to_token( fhand.read() )
                # Pickle the tokens for later use.
                with open( txt_out, 'wb' ) as output:
                    pickle.dump( tokens, output )


if __name__ == '__main__':
    main()
