.PHONY: dl-data notebook

BILLSTAT_PATH := data/BILLSTATUS/xml
BILLS_PATH := data/BILLS/xml
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
	wget $(BULKDATA_BASE_URI)/BILLSTATUS/115/s/BILLSTATUS-115-s.zip -O data/BILLSTATUS.zip
	wget $(BULKDATA_BASE_URI)/BILLS/115/1/s/BILLS-115-1-s.zip -O data/BILLS.zip
	# Unpack into data directory, updating existing files & creating new ones.
	unzip data/BILLSTATUS.zip -u -d $(BILLSTAT_PATH)
	unzip data/BILLS.zip -u -d $(BILLS_PATH)


# Startup local python notebook server
notebook: export PYTHONPATH=../src/python
notebook:
	cd notebooks && jupyter notebook
