@setlocal enableextensions
@cd /d "%~dp0"

IF NOT EXIST OK.txt (
    pip install -r requirements.txt
    echo "OK" > OK.txt
) ELSE (
    python words_all_files.py
)