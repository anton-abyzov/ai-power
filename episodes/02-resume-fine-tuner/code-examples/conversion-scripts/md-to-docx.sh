#!/bin/bash
# Convert Markdown resume to DOCX (Microsoft Word) format

# Check if input file is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <input.md> [output.docx]"
    echo "Example: $0 resume.md resume.docx"
    exit 1
fi

INPUT_FILE="$1"
OUTPUT_FILE="${2:-${INPUT_FILE%.md}.docx}"

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

# Create a reference DOCX with proper styling (optional)
# You can provide a custom reference.docx file for consistent formatting
REFERENCE_DOC=""
if [ -f "resume-template.docx" ]; then
    REFERENCE_DOC="--reference-doc=resume-template.docx"
    echo "Using reference template: resume-template.docx"
fi

# Convert with professional settings
pandoc "$INPUT_FILE" \
    -o "$OUTPUT_FILE" \
    -f markdown \
    -t docx \
    $REFERENCE_DOC \
    --highlight-style=kate

# Check if conversion was successful
if [ $? -eq 0 ]; then
    echo "✅ Successfully converted to: $OUTPUT_FILE"
    echo "File size: $(du -h "$OUTPUT_FILE" | cut -f1)"

    # Provide formatting tips
    echo ""
    echo "📝 Post-conversion tips:"
    echo "1. Open in Word and check formatting"
    echo "2. Adjust margins if needed (Layout → Margins → Narrow)"
    echo "3. Ensure consistent font (Calibri 11pt is standard)"
    echo "4. Check that hyperlinks are clickable"
    echo "5. Save as PDF from Word for best compatibility"

    # Open DOCX if on Mac
    if [[ "$OSTYPE" == "darwin"* ]]; then
        if command -v open &> /dev/null; then
            echo ""
            echo "Opening document..."
            open "$OUTPUT_FILE"
        fi
    fi

    # Open DOCX if on Windows (WSL)
    if grep -qi microsoft /proc/version 2>/dev/null; then
        echo ""
        echo "Opening document in Windows..."
        cmd.exe /c start "$OUTPUT_FILE" 2>/dev/null
    fi
else
    echo "❌ Conversion failed. Check error messages above."
    exit 1
fi

echo ""
echo "💡 Pro tip: For best ATS compatibility, keep formatting simple:"
echo "  - Use standard fonts (Arial, Calibri, Times New Roman)"
echo "  - Avoid tables, text boxes, headers/footers"
echo "  - Use simple bullet points"
echo "  - Save final version as both DOCX and PDF"