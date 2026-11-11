@echo off
REM Converts Markdown from doc/ to Word .docx using pandoc.
REM Usage: md2docx.bat [input.md] [output.docx]
REM   If no args: converts doc\KoppelvlakSpecificatieDocument.md to doc\KoppelvlakSpecificatieDocument.docx
REM   One arg: input file, output = same name with .docx
REM   Two args: input file, output file

where pandoc >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Pandoc niet gevonden. Installeer pandoc: https://pandoc.org/installing.html
    exit /b 1
)

set "SCRIPT_DIR=%~dp0"
set "DOC_DIR=%SCRIPT_DIR%..\doc"

if "%~1"=="" (
    set "INPUT=%DOC_DIR%\KoppelvlakSpecificatieDocument.md"
    set "OUTPUT=%DOC_DIR%\KoppelvlakSpecificatieDocument.docx"
) else if "%~2"=="" (
    set "INPUT=%~1"
    set "OUTPUT=%~dpn1.docx"
) else (
    set "INPUT=%~1"
    set "OUTPUT=%~2"
)

echo Converting: %INPUT%
echo Output:     %OUTPUT%
pandoc -o "%OUTPUT%" "%INPUT%" --from markdown --to docx
if %ERRORLEVEL% neq 0 (
    echo Conversie mislukt.
    exit /b 1
)
echo Gereed.
