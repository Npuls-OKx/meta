# OKx-meta dev container
# Doel: een reproduceerbare, geisoleerde omgeving waarin (AI-)agents tooling
# mogen installeren en scripts mogen draaien zonder de host te vervuilen.
#
# Tooling wordt zoveel mogelijk "gebakken" in dit image, zodat het team
# (na een clone + "Reopen in Container") exact dezelfde omgeving krijgt.

FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

# Systeem-tooling die in deze docs/architectuur-repo nuttig is:
# - imagemagick : grote afbeeldingen (bijv. ArchiMate-platen) verkleinen/tegelen
# - graphviz    : diagram-rendering
# - pandoc      : markdown -> pdf/docx conversies
# - chromium    : headless browser voor mermaid-cli (geen losse download nodig)
# - libreoffice : een presentatie-pdf omzetten naar een bewerkbare PowerPoint,
#                 met impress en draw voor de pdf-import (./deck <naam> bewerkbaar)
# - poppler     : pdftoppm, om een omzetting terug naar beeld te controleren
RUN apt-get update \
 && export DEBIAN_FRONTEND=noninteractive \
 && apt-get install -y --no-install-recommends \
      imagemagick \
      graphviz \
      pandoc \
      chromium \
      libreoffice-impress \
      libreoffice-draw \
      poppler-utils \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Laat mermaid-cli/puppeteer de meegeleverde chromium gebruiken i.p.v. te downloaden.
ENV PUPPETEER_SKIP_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium

# Python-dependencies (geisoleerd in de container).
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
