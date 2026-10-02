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

# Archi (ArchiMate-modelleertool) headless, voor het exporteren van platen en
# stromen uit model.archimate zonder handmatige stap: de commandline-plugin
# rendert elke view als PNG via het HTML-rapport. Eigen JRE meegeleverd; geen
# display nodig. De download is vastgepind op versie en sha256, zodat de build
# reproduceerbaar is. Gebruik: scripts/exporteer-archimate-platen.py.
ARG ARCHI_VERSIE=5.10.0
ARG ARCHI_SHA256=f9422455a00a22f5340dc28692ceafe0ad720c8cde839eaafb0fab1cea57287f
RUN curl -fsSL -o /tmp/archi.tgz \
      "https://github.com/archimatetool/archi.io/releases/download/${ARCHI_VERSIE%.*}_${ARCHI_VERSIE##*.}/Archi-Linux64-${ARCHI_VERSIE}.tgz" \
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
