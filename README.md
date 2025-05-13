# Code Chunker

A tool for splitting code files into semantically meaningful chunks using LlamaIndex and Tree Sitter.

## Features

- Split code files into semantic chunks based on language structure
- Support for multiple programming languages including Python and JavaScript
- Configurable chunk size
- Output chunks to text files for further processing

## Environment Setup

### Prerequisites

- Conda or Miniconda installed
- Git (for cloning the repository)

### Setup Instructions

1. Clone this repository:
   ```zsh
   git clone https://github.com/intutivelearning/code_chunker.git
   cd code_chunker
   ```

2. Create and activate the Conda environment:
   ```zsh
   make env
   conda activate ./venv
   ```

The environment includes:
- Python 3.12
- llama-index for code chunking
- tree_sitter and tree_sitter_language_pack for language parsing

## Usage

### Chunking Code Files

Use the provided Makefile commands to chunk sample files:

```zsh
# Chunk a Python file
make chunk-py

# Chunk a JavaScript file
make chunk-js
```

Or run the script directly with custom parameters:

```zsh
python split_code.py <filename> <language> [max_chars]
```

Examples:
```zsh
python split_code.py base_events.py python
python split_code.py MyScript.js javascript
python split_code.py large_file.py python 10000  # With custom max characters
```

The chunked output will be saved to a file named `<filename>_chunks_all.txt`.

## Notes on Environment Removal

When using `make drop-env` to remove the conda environment, make sure you are **not** inside the environment you want to remove. Run the command from your base environment or a new terminal window. This is due to conda limitations in non-interactive shells and Makefiles.

Example:

```zsh
conda activate base  # or open a new terminal
make drop-env
```
