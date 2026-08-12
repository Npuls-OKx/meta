# Streamlit — Npuls huisstijl

## Quickstart

1. Kopieer `assets/streamlit/streamlit-config.toml` naar `.streamlit/config.toml`
2. Kopieer `assets/streamlit/streamlit-custom.css` naar je projectmap
3. Injecteer de CSS bovenin je Streamlit app:

```python
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Npuls Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

css = Path("streamlit-custom.css").read_text()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
```

## Kleuren in Plotly / Altair / Matplotlib

```python
NPULS = {
    "orange": "#DD784B",
    "black":  "#000000",
    "pink":   "#F4D9DC",
    "blue":   "#3D68EC",
    "yellow": "#F4D74B",
    "green":  "#00AF81",
}
PALETTE = [NPULS["blue"], NPULS["orange"], NPULS["green"],
           NPULS["yellow"], NPULS["pink"], NPULS["black"]]
```

### Plotly

```python
import plotly.express as px
fig = px.bar(df, x="x", y="y", color="cat",
             color_discrete_sequence=PALETTE)
fig.update_layout(
    font_family="Inter, 'General Sans', sans-serif",
    font_color=NPULS["black"],
    plot_bgcolor="white",
    paper_bgcolor="white",
    colorway=PALETTE,
)
```

### Altair

```python
import altair as alt
chart = alt.Chart(df).mark_bar().encode(
    x="x", y="y",
    color=alt.Color("cat:N", scale=alt.Scale(range=PALETTE)),
).configure(font="Inter")
```

### Matplotlib

```python
import matplotlib as mpl
mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=PALETTE)
mpl.rcParams["font.family"] = "Inter"
mpl.rcParams["axes.edgecolor"] = NPULS["black"]
```

## Status-kleuren

| Status  | Kleur  | Use |
|---------|--------|-----|
| Succes  | Groen  | `st.success` |
| Waarschuwing | Geel | `st.warning` |
| Fout    | Oranje | `st.error` (we vermijden rood) |
| Info    | Blauw  | `st.info` |

## Sidebar

De sidebar gebruikt roze achtergrond met blauwe tekst (goedgekeurde combinatie):

```css
[data-testid="stSidebar"] {
  background-color: #F4D9DC;
  color: #3D68EC;
}
```

Dit zit al in `streamlit-custom.css`.

## Layout-tips

- Titel altijd in Oranje (`#DD784B`), body zwart
- KPI metrics: cijfer in Blauw, label in zwart
- Tabs: actieve tab onderstreping in Oranje
- Knop primary: Blauw bg, witte tekst
