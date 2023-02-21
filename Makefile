.PHONY: dl-data notebook

BILLSTAT_PATH := /home/jasond/bill-analysis/data/BILLSTATUS/xml
BILLS_PATH := /home/jasond/bill-analysis/data/BILLS/xml
BULKDATA_BASE_URI := https://www.gpo.gov/fdsys/bulkdata


all:
	@echo "Try one of the following commands: "
	@echo "-> dl-data			Setup data folder and download data from gpo.gov"
	@echo "-> notebook			Start jupyter notebook server"


# Download and unpack data files into `data`
dl-data:
	# Create directories
	@mkdir -p $(BILLS_PATH) && mkdir -p $(BILLSTAT_PATH)
	# Download zipped data files
	wget $(BULKDATA_BASE_URI)/BILLSTATUS/117/s/BILLSTATUS-117-s.zip -O /home/jasond/bill-analysis/data/BILLSTATUS.zip
	wget $(BULKDATA_BASE_URI)/BILLS/117/1/s/BILLS-117-1-s.zip -O /home/jasond/bill-analysis/data/BILLS.zip
	# Unpack into data directory, updating existing files & creating new ones.
	unzip /home/jasond/bill-analysis/data/BILLSTATUS.zip -d $(BILLSTAT_PATH)
	unzip /home/jasond/bill-analysis/data/BILLS.zip -d $(BILLS_PATH)


# Startup local python notebook server
notebook: export PYTHONPATH=../src/python
notebook:
	cd notebooks && jupyter notebook
