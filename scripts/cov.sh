#!/usr/bin/env bash

echo "Öffne Testabdeckung ..."
python -c "import webbrowser; webbrowser.open('http://localhost:8000/htmlcov/index.html')"
python -m http.server
