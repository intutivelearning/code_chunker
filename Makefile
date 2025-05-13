# Makefile for code-chunker project

.PHONY: env clean drop-env chunk-py chunk-js

# Create conda environment in ./venv directory from environment.yml
env:
	conda env create -p ./venv -f environment.yml || conda env update -p ./venv -f environment.yml

# Remove conda environment in ./venv
drop-env:
	conda env remove -p ./venv -y || echo "Environment not found."

# Clean up output files
clean:
	rm -f *_chunks_all.txt

# Run code chunking script (example usage)
chunk-py:
	./venv/bin/python split_code.py base_events.py python

chunk-js:
	./venv/bin/python split_code.py MyScript.js javascript
