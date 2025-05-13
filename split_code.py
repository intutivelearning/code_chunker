import os
import sys

from llama_index.core.node_parser import CodeSplitter

# Usage: python split_code.py <filename> <language> [max_chars]
# Example: python split_code.py base_events.py python
#          python split_code.py MyScript.js javascript
#          python split_code.py MyScript.js javascript 10000


def main():
    if len(sys.argv) < 3:
        print("Usage: python split_code.py <filename> <language> [max_chars]")
        sys.exit(1)
    file_path = sys.argv[1]
    language = sys.argv[2]
    # Allow optional max_chars argument
    max_chars = 50000  # Default to 50,000 if not provided
    if len(sys.argv) > 3:
        try:
            max_chars = int(sys.argv[3])
        except ValueError:
            print("max_chars must be an integer")
            sys.exit(1)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)
    with open(file_path, "r") as f:
        code = f.read()
    splitter = CodeSplitter(language=language, max_chars=max_chars)
    chunks = splitter.split_text(code)
    out_file_name = f"{os.path.splitext(os.path.basename(file_path))[0]}_chunks_all.txt"
    with open(out_file_name, "w") as out_file:
        for i, chunk in enumerate(chunks):
            out_file.write(f"\n--- Chunk {i+1} ---\n")
            out_file.write(chunk)
            out_file.write("\n")
    print(f"All chunks saved to {out_file_name}")


if __name__ == "__main__":
    main()
