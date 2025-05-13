# code_chunker

## Notes on Environment Removal

When using `make drop-env` to remove the conda environment, make sure you are **not** inside the environment you want to remove. Run the command from your base environment or a new terminal window. This is due to conda limitations in non-interactive shells and Makefiles.

Example:

```zsh
conda activate base  # or open a new terminal
make drop-env
```
