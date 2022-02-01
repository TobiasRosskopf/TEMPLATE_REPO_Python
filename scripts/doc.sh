#!/usr/bin/env bash
# https://pdoc.dev/docs/pdoc.html

echo "Generiere Code Dokumentation ..."
pdoc \
    --docformat=google \
    --show-source \
    --search \
    --math \
    --footer-text="Generated on `date`" \
    --output-directory=docs/html \
    package_name

if [ $1 == '--no-open' ]
then
    echo "FERTIG!"
else
    echo "Öffne Dokumentation ..."
    python -c "import webbrowser; webbrowser.open('http://localhost:8000/docs/html/package_name.html')"
    python -m http.server
fi
