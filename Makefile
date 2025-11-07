.PHONY: env html clean help

# Default target
help:
	@echo "Available targets:"
	@echo "  env    - Create/update conda environment"
	@echo "  html   - Build HTML documentation"
	@echo "  clean  - Clean generated files"
	@echo "  help   - Show this help message"

# Environment setup (no activation)
env:
	@echo "Creating or updating environment..."
	conda env update --file environment.yml --prune

# Build HTML documentation using MyST
html:
	@echo "Building site..."
	myst build --html

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -rf figures
	rm -rf audio
	rm -rf _build
	@echo "Clean complete!"