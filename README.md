## bill-analysis

Here lies python code and notebooks used in the analysis of legislation
data from the U.S. Senate and House of Representatives.


### Getting Started

Install the python dependencies. Use of a virtual environment highly
recommended

    pip install -r requirements.txt

Setup data folders and download dataset.

    make dl-data

Run XML parsing and text tokenization script. Should take a couple minutes
to finish running.

    python src/python/prep_data.py