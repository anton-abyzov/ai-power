#!/bin/bash
# Convert Markdown resume to PDF with professional formatting

# Check if input file is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <input.md> [output.pdf]"
    echo "Example: $0 resume.md resume.pdf"
    exit 1
fi

INPUT_FILE="$1"
OUTPUT_FILE="${2:-${INPUT_FILE%.md}.pdf}"

# Check if input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: Input file '$INPUT_FILE' not found"
    exit 1
fi

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "Error: pandoc is not installed"
    echo "Install pandoc:"
    echo "  Mac: brew install pandoc"
    echo "  Ubuntu/Debian: sudo apt-get install pandoc"
    echo "  Other: https://pandoc.org/installing.html"
    exit 1
fi

echo "Converting $INPUT_FILE to $OUTPUT_FILE..."

# Professional PDF settings for resumes
pandoc "$INPUT_FILE" \
    -o "$OUTPUT_FILE" \
    --pdf-engine=xelatex \
    -V geometry:margin=0.75in \
    -V fontsize=11pt \
    -V mainfont="Arial" \
    -V monofont="Courier New" \
    -V linestretch=1.15 \
    -V documentclass=article \
    -V colorlinks=true \
    -V linkcolor=blue \
    -V urlcolor=blue \
    --highlight-style=kate \
    --metadata title="" \
    --metadata author="" \
    --metadata date=""

# Check if conversion was successful
if [ $? -eq 0 ]; then
    echo "✅ Successfully converted to: $OUTPUT_FILE"
    echo "File size: $(du -h "$OUTPUT_FILE" | cut -f1)"

    # Open PDF if on Mac
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "Opening PDF..."
        open "$OUTPUT_FILE"
    fi
else
    echo "❌ Conversion failed. Check error messages above."
    echo ""
    echo "Common issues:"
    echo "1. Missing LaTeX: Install with 'brew install --cask mactex' (Mac) or 'sudo apt-get install texlive-full' (Linux)"
    echo "2. Missing fonts: The script uses Arial by default. Modify -V mainfont if needed."
    echo "3. Complex formatting: Simplify markdown if conversion fails."
    exit 1
fi