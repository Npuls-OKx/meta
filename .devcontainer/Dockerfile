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
#                 met impress en draw voor de pdf-import (./deck <naam> bewerkbaar);
#                 writer om een gebouwd Word-sjabloon te kunnen bekijken (#554)
# - librsvg     : een vectorbeeld naar PNG, want het Word-formaat draagt geen
#                 SVG en pandoc roept rsvg-convert aan (#554)
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
      libreoffice-writer \
      librsvg2-bin \
      poppler-utils \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Archi (ArchiMate-modelleertool) headless, voor het exporteren van platen en
# stromen uit model.archimate zonder handmatige stap: de commandline-plugin
# rendert elke view als PNG via het HTML-rapport. Eigen JRE meegeleverd; geen
# display nodig. De download is vastgepind op versie en sha256, zodat de build
# reproduceerbaar is. Gebruik: scripts/exporteer-archimate-platen.py.
# Het releaselabel bij Archi is major_minor, dus 5.11.0 hangt onder 5_11. De eerdere
# opbouw maakte er 5.11_0 van en gaf een 404; die bouwstap faalde stil, waardoor
# /opt/Archi ontbrak en exporteer-archimate-platen.py niet kon draaien. Archi haalt
# oude releases bovendien weg: 5.10.0 was in november 2026 niet meer op te halen.
ARG ARCHI_VERSIE=5.11.0
ARG ARCHI_SHA256=a13f4f058c16d8653c1307a145b9dd6bddd4226abc952f58c586c46d61db219e
RUN LABEL="$(echo "${ARCHI_VERSIE%.*}" | tr . _)" \
 && curl -fsSL -o /tmp/archi.tgz \
      "https://github.com/archimatetool/archi.io/releases/download/${LABEL}/Archi-Linux64-${ARCHI_VERSIE}.tgz" \
 && echo "${ARCHI_SHA256}  /tmp/archi.tgz" | sha256sum -c - \
 && mkdir -p /opt \
 && tar -xzf /tmp/archi.tgz -C /opt \
 && rm /tmp/archi.tgz \
 && ln -s /opt/Archi/Archi /usr/local/bin/archi
ENV ARCHI_HOME=/opt/Archi

# Laat mermaid-cli/puppeteer de meegeleverde chromium gebruiken i.p.v. te downloaden.
ENV PUPPETEER_SKIP_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium

# Python-dependencies (geisoleerd in de container).
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
