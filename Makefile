.PHONY: notebook

# Startup local python notebook server
notebook: export PYTHONPATH=../src/python
notebook:
	cd notebooks && jupyter notebook
