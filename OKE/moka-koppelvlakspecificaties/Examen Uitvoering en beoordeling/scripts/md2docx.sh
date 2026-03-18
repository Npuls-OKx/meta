#!/usr/bin/env bash
# Converts Markdown from doc/ to Word .docx using pandoc.
# Usage: ./md2docx.sh [input.md] [output.docx]
#   If no args: converts doc/KoppelvlakSpecificatieDocument.md to doc/KoppelvlakSpecificatieDocument.docx
#   One arg: input file, output = same name with .docx
#   Two args: input file, output file

if ! command -v pandoc &> /dev/null; then
    echo "Pandoc niet gevonden. Installeer pandoc: https://pandoc.org/installing.html"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOC_DIR="${SCRIPT_DIR}/../doc"

if [ -z "$1" ]; then
    INPUT="${DOC_DIR}/KoppelvlakSpecificatieDocument.md"
    OUTPUT="${DOC_DIR}/KoppelvlakSpecificatieDocument.docx"
elif [ -z "$2" ]; then
    INPUT="$1"
    OUTPUT="${1%.md}.docx"
else
    INPUT="$1"
    OUTPUT="$2"
fi

echo "Converting: $INPUT"
echo "Output:     $OUTPUT"
pandoc -o "$OUTPUT" "$INPUT" --from markdown --to docx
if [ $? -ne 0 ]; then
    echo "Conversie mislukt."
    exit 1
fi
echo "Gereed."
