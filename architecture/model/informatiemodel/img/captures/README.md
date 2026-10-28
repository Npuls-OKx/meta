# Vastgelegde beelden bij een issue

De beelden in [`../regels/`](../regels/) volgen de regeltabel: zij worden opnieuw getekend zodra een regel wijzigt. Dat is precies wat je wilt in het document, en precies wat je niet wilt onder een issue. Een issue beschrijft een vraag op een moment; een beeld dat daarna meebeweegt laat de vraag niet meer zien.

Deze map draagt daarom vastgelegde afbeeldingen, per datum. Een issue verwijst ernaar met de commit erin, zodat het beeld blijft zoals het was toen de vraag werd gesteld.

```
https://raw.githubusercontent.com/Npuls-OKx/meta/<commit>/architecture/model/informatiemodel/img/captures/<datum>/<beeld>.png
```

| | |
|---|---|
| Vorm | PNG, twee keer de SVG-maat, teruggebracht tot 64 kleuren |
| Maken | `chromium --headless --screenshot` op de SVG, daarna `convert -strip -colors 64 PNG8:` |
| Wanneer | Bij het aanmaken van een issue dat over een beeld gaat |
| Levende versie | [`../regels/`](../regels/), met het document als ingang |

De map `20261028` hoort bij de zeven issues uit de sparsessie van 28 oktober 2026: #433 tot en met #439.
