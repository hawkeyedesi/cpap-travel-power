#!/usr/bin/env python3
"""Optional helper: regenerates the static HTML pages from the content below.
The committed .html files are the site; no build step is needed to host it."""

NAV = [("index.html","Home"),("setup.html","Outage-proof setup"),("batteries.html","Batteries compared"),
       ("flying.html","Flying"),("india.html","India power"),("test.html","Test your setup")]

S = {
 "resmed": ('ResMed AirSense 11 user guide (technical specifications, 65W power supply)','https://document.resmed.com/documents/products/machine/airsense-11/user-guide/airsense11_user-guide_amer_mul.pdf'),
 "zopec": ('Zopec – Explore Mini Battery System product page','https://www.zopec.com/products/zopec-explore-mini-battery-system'),
 "zopecsite": ('Zopec Explore Mini official site','https://www.zopecexploremini.com/'),
 "zopecups": ('Zopec – how the Explore UPS batteries work','https://www.zopec.com/pages/zopec-medical-universal-cpap-battery-line'),
 "zopecman": ('Zopec Explore Mini user manual (PDF, hosted by a retailer)','https://www.respshop.com/cdn/shop/files/ENG_Explore_Mini_User_Manual_03.03.24_1.pdf'),
 "medi": ('Medistrom – Pilot-24 Lite product page','https://www.medistrom.com/products-pilot24-lite.html'),
 "medikit": ('Medistrom – AirSense 11 kit for Pilot-24 Lite','https://www.medistrom.com/products-pilot24-lite-resmed-airsense-11-kit.html'),
 "medirt": ('Choice One Medical (retailer) – Pilot-24 Lite page with tested runtime table','https://choiceonemedical.com/products/pilot-24-lite'),
 "eco": ('EcoFlow – RAPID Pro Power Bank (27,650mAh, 300W)','https://us.ecoflow.com/products/ecoflow-rapid-pro-power-bank-27650mah-300w-140w-built-in-cable'),
 "anker": ('Anker – Prime Charger (100W, 3 ports) specifications (example of a 100W charger)','https://www.anker.com/products/a2688-anker-prime-charger-100w-3-ports-gan'),
 "faa": ('FAA PackSafe – Lithium batteries','https://www.faa.gov/hazmat/packsafe/lithium-batteries'),
 "faa2": ('FAA – Airline passengers and batteries','https://www.faa.gov/hazmat/packsafe/airline-passengers-and-batteries'),
 "iata": ('IATA – Safe travel with lithium batteries','https://www.iata.org/en/youandiata/travelers/batteries/'),
 "dgca": ('The Hindu BusinessLine – DGCA bars use of power banks on board aircraft','https://www.thehindubusinessline.com/economy/logistics/power-banks-barred-from-use-on-board-aircraft-dgca/article70470708.ece'),
 "bis": ('Bureau of Indian Standards – Plugs and Sockets lesson plan (PDF)','https://www.bis.gov.in/wp-content/uploads/2023/08/Plugs-and-Sockets-20.pdf'),
 "iec": ('IEC – World Plugs (look up India)','https://www.iec.ch/world-plugs'),
}

DISCLAIMER = ('<div class="card note"><strong>Not medical advice.</strong> This is a traveller\'s guide, not guidance from a clinician. '
  'Check your therapy settings and any battery use with your doctor or DME (equipment supplier), and check battery rules with your airline before you fly.</div>')

def page(fname, title, desc, body, sources):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h==fname else ""}>{t}</a>' for h,t in NAV)
    src = "".join(f'<li><a href="{S[k][1]}" rel="noopener">{S[k][0]}</a></li>' for k in sources)
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · CPAP travel power</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230f766e'/%3E%3Cpath d='M18 4 9 18h6l-2 10 10-15h-6z' fill='%23fff'/%3E%3C/svg%3E">
</head>
<body>
<header class="site"><div class="wrap"><a class="brand" href="index.html">CPAP <span>travel power</span></a><nav>{nav}</nav></div></header>
<main><div class="wrap">
{body}
{DISCLAIMER}
<section class="sources"><h2>Sources</h2><ol>{src}</ol><p>Checked October 2026. Specs change; trust the label on your own gear and the manufacturer's current page.</p></section>
</div></main>
<footer><div class="wrap">An independent guide. No ads, no affiliate links, no sponsors. Product names are mentioned only because it's the gear we actually use or considered.</div></footer>
</body>
</html>
'''
    open(fname,"w").write(html)

# ---------------- HOME
page("index.html","Run your CPAP on battery while travelling",
 "An honest guide to running a ResMed AirSense 11 on battery while travelling, with India's power cuts as the main example.",
'''<h1>Keep your CPAP running when the power doesn't</h1>
<p class="lede">A plain-English guide to running a ResMed AirSense 11 on battery while travelling. We use India as the main example: 230&nbsp;V power, different plugs, and power cuts that can hit in the middle of the night.</p>

<div class="card quick">
<h2 style="margin-top:4px">The quick answer</h2>
<ul>
<li><b>Use a CPAP battery that works as a UPS.</b> Wall power runs straight through it, and it switches to battery on its own if the power cuts. We use a Zopec Explore Mini (99.5&nbsp;Wh).</li>
<li><b>Chain it like this:</b> wall &rarr; 100–240&nbsp;V USB-C charger &rarr; UPS battery &rarr; AirSense&nbsp;11. <a href="setup.html">See the diagram.</a></li>
<li><b>Turn the humidifier and heated tube off</b> when you might be running on battery. With them off, we plan on <b>about one night</b> (roughly 10–12&nbsp;h) from one ~100&nbsp;Wh battery. That's our planning estimate, not a measured result yet.</li>
<li><b>Keep spare power banks off the night path.</b> Use them during the day to top up the CPAP battery.</li>
<li><b>Flying:</b> batteries of 100&nbsp;Wh or less generally go in carry-on and never in checked bags. <a href="flying.html">Details.</a></li>
<li><b>India:</b> 230&nbsp;V, 50&nbsp;Hz. The AirSense 11 power supply takes 100–240&nbsp;V, so you need a plug adapter, not a voltage converter. <a href="india.html">Details.</a></li>
<li><b>Test it all at home first.</b> <a href="test.html">Here's how.</a></li>
</ul>
</div>

<h2>Why this matters</h2>
<p>A CPAP running from the wall simply stops when the power goes out, and you wake up to a mask that isn't blowing. In places where power cuts are common, a battery that takes over without a hiccup can be the difference between a full night of therapy and a broken one.</p>
<p>The AirSense 11's own power supply is rated 100–240&nbsp;V, 50–60&nbsp;Hz, and ResMed lists typical power use of 56.1&nbsp;W and a peak of 73.2&nbsp;W. On battery, the humidifier and heated tube are the biggest thing you control: published runtimes drop from a full night to a few hours with them on (see <a href="batteries.html">Batteries compared</a>).</p>

<h2>Guides</h2>
<div class="grid">
<a href="setup.html"><b>The outage-proof setup</b><small>The UPS chain we use, with a diagram</small></a>
<a href="batteries.html"><b>Batteries compared</b><small>UPS-style CPAP batteries vs. power banks</small></a>
<a href="flying.html"><b>Flying with CPAP batteries</b><small>Carry-on rules, Wh limits, India's in-flight rule</small></a>
<a href="india.html"><b>India power basics</b><small>Voltage, plugs, outages</small></a>
<a href="test.html"><b>Test before you fly</b><small>A simple home test plan</small></a>
</div>

<h2>Who we are</h2>
<p>We're a CPAP user (AirSense 11) getting ready for a trip to India, writing down what we learned while setting up. We haven't been paid by anyone and we don't sell anything. Our own test results will be added after the trip.</p>
''', ["resmed","zopec","medirt","faa","iata","bis"])

# ---------------- SETUP
DIAGRAM = '''<div class="diagram" role="img" aria-label="Night setup: wall outlet, plug adapter, 100 watt USB-C charger, Zopec Explore Mini acting as UPS, AirSense 11. Daytime only: EcoFlow power bank recharges the Zopec.">
<svg class="horiz" viewBox="0 0 720 300" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif">
<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#0f766e"/></marker>
<marker id="ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#9aa5b1"/></marker></defs>
<text x="10" y="22" font-size="14" font-weight="700" fill="#0f766e">AT NIGHT</text>
<g font-size="13" text-anchor="middle">
<rect x="10" y="40" width="120" height="70" rx="10" fill="#f4f2ec" stroke="#d9d4c8"/><text x="70" y="70" font-weight="600">Wall outlet</text><text x="70" y="90" fill="#5b6670">230 V + adapter</text>
<rect x="155" y="40" width="130" height="70" rx="10" fill="#f4f2ec" stroke="#d9d4c8"/><text x="220" y="70" font-weight="600">USB-C charger</text><text x="220" y="90" fill="#5b6670">100 W, 100–240 V</text>
<rect x="310" y="32" width="160" height="86" rx="12" fill="#e6f4f1" stroke="#0f766e" stroke-width="2"/><text x="390" y="64" font-weight="700" fill="#0f766e">CPAP battery (UPS)</text><text x="390" y="84" fill="#1f2933">Zopec Explore Mini</text><text x="390" y="102" fill="#5b6670">takes over in an outage</text>
<rect x="495" y="40" width="130" height="70" rx="10" fill="#f4f2ec" stroke="#d9d4c8"/><text x="560" y="70" font-weight="600">AirSense 11</text><text x="560" y="90" fill="#5b6670">humidifier off</text>
</g>
<g stroke="#0f766e" stroke-width="2.5" fill="none" marker-end="url(#ar)"><path d="M130 75H151"/><path d="M285 75H306"/><path d="M470 75H491"/></g>
<g font-size="11" fill="#5b6670" text-anchor="middle"><text x="296" y="132">USB-C</text><text x="482" y="132">DC cable</text></g>
<line x1="10" y1="165" x2="710" y2="165" stroke="#e6e2da"/>
<text x="10" y="195" font-size="14" font-weight="700" fill="#5b6670">DAYTIME ONLY</text>
<g font-size="13" text-anchor="middle">
<rect x="155" y="212" width="130" height="70" rx="10" fill="#fff" stroke="#c3cad1" stroke-dasharray="5 4"/><text x="220" y="242" font-weight="600">Power bank</text><text x="220" y="262" fill="#5b6670">EcoFlow RAPID Pro</text>
<rect x="310" y="212" width="160" height="70" rx="12" fill="#fff" stroke="#c3cad1" stroke-dasharray="5 4"/><text x="390" y="242" font-weight="600">CPAP battery</text><text x="390" y="262" fill="#5b6670">recharging</text>
</g>
<path d="M285 247H306" stroke="#9aa5b1" stroke-width="2.5" marker-end="url(#ag)"/>
<text x="490" y="242" font-size="12" fill="#5b6670">Not connected to the CPAP.</text><text x="490" y="260" font-size="12" fill="#5b6670">Top-up only, while you're awake.</text>
</svg>
<svg class="vert" viewBox="0 0 340 560" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" text-anchor="middle">
<defs><marker id="av" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#0f766e"/></marker>
<marker id="avg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#9aa5b1"/></marker></defs>
<text x="20" y="20" font-size="14" font-weight="700" fill="#0f766e" text-anchor="start">AT NIGHT</text>
<g font-size="14">
<rect x="40" y="32" width="260" height="56" rx="10" fill="#f4f2ec" stroke="#d9d4c8"/><text x="170" y="56" font-weight="600">Wall outlet</text><text x="170" y="76" fill="#5b6670" font-size="12">230 V + plug adapter</text>
<rect x="40" y="118" width="260" height="56" rx="10" fill="#f4f2ec" stroke="#d9d4c8"/><text x="170" y="142" font-weight="600">USB-C charger</text><text x="170" y="162" fill="#5b6670" font-size="12">100 W, 100–240 V</text>
<rect x="30" y="204" width="280" height="72" rx="12" fill="#e6f4f1" stroke="#0f766e" stroke-width="2"/><text x="170" y="230" font-weight="700" fill="#0f766e">CPAP battery (UPS)</text><text x="170" y="249" font-size="13">Zopec Explore Mini</text><text x="170" y="266" fill="#5b6670" font-size="12">takes over in an outage</text>
<rect x="40" y="306" width="260" height="56" rx="10" fill="#f4f2ec" stroke="#d9d4c8"/><text x="170" y="330" font-weight="600">AirSense 11</text><text x="170" y="350" fill="#5b6670" font-size="12">humidifier + heated tube off</text>
</g>
<g stroke="#0f766e" stroke-width="2.5" marker-end="url(#av)"><path d="M170 88V114"/><path d="M170 174V200"/><path d="M170 276V302"/></g>
<g font-size="11" fill="#5b6670" text-anchor="start"><text x="180" y="193">USB-C</text><text x="180" y="295">DC cable</text></g>
<line x1="10" y1="390" x2="330" y2="390" stroke="#e6e2da"/>
<text x="20" y="416" font-size="14" font-weight="700" fill="#5b6670" text-anchor="start">DAYTIME ONLY</text>
<g font-size="14"><rect x="40" y="428" width="260" height="50" rx="10" fill="#fff" stroke="#c3cad1" stroke-dasharray="5 4"/><text x="170" y="458" font-weight="600">Power bank (EcoFlow RAPID Pro)</text>
<rect x="40" y="504" width="260" height="50" rx="10" fill="#fff" stroke="#c3cad1" stroke-dasharray="5 4"/><text x="170" y="534" font-weight="600">CPAP battery, recharging</text></g>
<path d="M170 478V500" stroke="#9aa5b1" stroke-width="2.5" marker-end="url(#avg)"/>
</svg></div>'''

page("setup.html","The outage-proof setup",
 "How to chain a USB-C charger, a UPS-style CPAP battery and a ResMed AirSense 11 so a power cut doesn't stop your therapy.",
f'''<h1>The outage-proof setup</h1>
<p class="lede">The idea is simple: put a battery <em>between</em> the wall and your CPAP. If the power cuts at 3&nbsp;a.m., the battery takes over and you keep sleeping.</p>
{DIAGRAM}
<h2>The night chain</h2>
<ol>
<li><b>Wall outlet + plug adapter.</b> In India that means a Type D adapter for most sockets (we carry a Ceptics India adapter). See <a href="india.html">India power basics</a>.</li>
<li><b>A dual-voltage USB-C charger.</b> We use an Anker 100&nbsp;W charger. Check the label says <code>100–240V</code> input. Zopec's manual asks for a 65&nbsp;W (or equivalent) USB-C charger for this setup, so 100&nbsp;W leaves some headroom.</li>
<li><b>A UPS-style CPAP battery.</b> We use the Zopec Explore Mini. Zopec says that while wall power is present it passes straight through (sparing the cells), and if it senses the power has dropped it switches to battery instantly.</li>
<li><b>AirSense 11</b>, connected with the AirSense 11 DC cable that comes with the Explore Mini.</li>
</ol>
<p>Zopec's manual also describes a second way to charge it in UPS mode: your AirSense 11's own power cord plus ResMed's AirSense 11 charging adapter. Either way, follow the manual for your exact cables.</p>

<div class="card quick"><b>Heated tube off.</b> Zopec's manual says that in the USB-C UPS setup the heated tube <em>must</em> be off, or the CPAP will start pulling from the battery even with the wall connected. If you see the battery draining, turn the humidifier and heated tube off too.</div>

<h2>Why not just use a power bank?</h2>
<p>It's tempting to plug a big laptop power bank into the CPAP and charge the bank from the wall. We don't recommend it for the night:</p>
<ul>
<li>Consumer power banks with "pass-through charging" aren't designed as medical UPS units. When wall power cuts, some briefly drop their output while they switch over, and that blip can be enough to reboot the CPAP mid-night.</li>
<li>Every extra adapter and cable in a daisy-chain is one more thing that can wiggle loose or negotiate the wrong voltage.</li>
<li>A generic power bank usually needs an extra USB-C-to-CPAP cable, which is another link to trust.</li>
</ul>
<p>So we keep our EcoFlow RAPID Pro (99.54&nbsp;Wh) <b>off the night path</b>. During the day, if the CPAP battery ran down overnight, we use the EcoFlow to recharge it over USB-C. That's useful on days when the power is out for a long stretch.</p>

<h2>How long will it last?</h2>
<p>With the humidifier and heated tube <b>off</b>, we're planning on roughly <b>10–12 hours, so about one night</b>, from one fully charged ~100&nbsp;Wh battery. Zopec's own pages say "1–2 nights" or "1.5–2.0 nights" in the same conditions. We use the lower number because runtime depends heavily on your pressure, mask leak and the room.</p>
<p>With the humidifier on, runtime drops a lot. For its similar 95&nbsp;Wh Pilot-24 Lite, the runtime table a Medistrom retailer publishes says using the humidifier or heated tubing cuts runtime to about 2–4 hours.</p>
<p>We'll replace the planning estimate with our own measured numbers after <a href="test.html">our tests</a>.</p>
''', ["zopecman","zopecups","zopec","zopecsite","anker","eco","medirt","resmed"])

# ---------------- BATTERIES
page("batteries.html","Batteries compared",
 "UPS-style CPAP batteries vs generic USB-C power banks for a ResMed AirSense 11: capacity, outage switchover and charging.",
'''<h1>Batteries compared</h1>
<p class="lede">There are two kinds of battery people use with a CPAP: ones built to sit in the power path like a UPS, and general power banks. Both can be useful, just for different jobs.</p>

<div class="table-wrap"><table>
<thead><tr><th></th><th>Zopec Explore Mini</th><th>Medistrom Pilot-24 Lite</th><th>EcoFlow RAPID Pro power bank</th></tr></thead>
<tbody>
<tr><td><b>Type</b></td><td>CPAP battery with UPS</td><td>CPAP battery / backup power supply</td><td>General USB-C power bank</td></tr>
<tr><td><b>Capacity (maker)</b></td><td>99.5&nbsp;Wh</td><td>95&nbsp;Wh</td><td>99.54&nbsp;Wh (27,650&nbsp;mAh)</td></tr>
<tr><td><b>AirSense 11</b></td><td>Cables included</td><td>Needs AirSense 11 kit (sold separately)</td><td>Not designed for CPAP; would need a third-party cable</td></tr>
<tr><td><b>Takes over in an outage</b></td><td>Yes, wall power passes through and it auto-switches (maker's claim)</td><td>Yes, sold as a backup power supply (maker's claim)</td><td>Has pass-through charging, but it isn't a UPS. Not recommended on the night path</td></tr>
<tr><td><b>Charges from</b></td><td>USB-C (65&nbsp;W) or ResMed cord + adapter</td><td>24&nbsp;V DC input (ResMed or Medistrom adapter). No USB-C input listed, so it can't top up from a USB-C power bank</td><td>USB-C (up to 140&nbsp;W per port)</td></tr>
<tr><td><b>Recharge time (maker)</b></td><td>Under 1.5&nbsp;h</td><td>2–3&nbsp;h (7–9&nbsp;h with the AirMini adapter)</td><td>0–80% in 20&nbsp;min with EcoFlow's own 320&nbsp;W station</td></tr>
<tr><td><b>Our role for it</b></td><td>Night path (we own one)</td><td>Good alternative</td><td>Daytime top-ups only (we own one)</td></tr>
</tbody></table></div>
<p style="font-size:.9rem;color:var(--muted)">All specs are from the manufacturers' own pages (see Sources). We haven't measured any of them yet.</p>

<h2>What "UPS-style" means</h2>
<p>A UPS (uninterruptible power supply) sits between the wall and your device. When wall power is there, it powers the device and stays charged. When wall power disappears, it switches to battery fast enough that the device doesn't notice. Zopec describes three parts: wall power pass-through, outage detection with automatic switching, and the reserve battery.</p>

<h2>A note on runtime numbers</h2>
<p>Runtime depends mostly on your pressure setting. Here are tested AirSense 11 runtimes for the Pilot-24 Lite with the humidifier and heated tube off, from a table published by retailer Choice One Medical (Medistrom's own page just says "1–2 nights" at an average pressure):</p>
<div class="table-wrap"><table style="min-width:320px">
<thead><tr><th>Pressure</th><th>Runtime (published test)</th></tr></thead>
<tbody><tr><td>5 cm H₂O</td><td>20 h 11 m</td></tr><tr><td>10 cm H₂O</td><td>12 h 33 m</td></tr><tr><td>15 cm H₂O</td><td>8 h 55 m</td></tr><tr><td>20 cm H₂O</td><td>6 h 58 m</td></tr></tbody></table></div>
<p>These are published figures for one battery, not ours, but they show the pattern: higher pressure means a shorter night. Our own planning number for the Zopec is about one night (10–12&nbsp;h) with the humidifier and heated tube off.</p>

<h2>Why all three are just under 100 Wh</h2>
<p>That's not a coincidence. 100&nbsp;Wh is the line under which spare lithium batteries are generally allowed in carry-on without airline approval. See <a href="flying.html">Flying with CPAP batteries</a>.</p>
''', ["zopec","zopecups","zopecman","medi","medikit","medirt","eco"])

# ---------------- FLYING
page("flying.html","Flying with CPAP batteries",
 "Airline rules for CPAP batteries and power banks: the 100 Wh carry-on limit, never in checked bags, and India's in-flight power bank rule.",
'''<h1>Flying with CPAP batteries</h1>
<p class="lede">The short version: <b>spare lithium batteries go in your carry-on, never in checked bags</b>, and anything at or under 100&nbsp;Wh is generally fine without asking the airline.</p>

<div class="card quick">
<ul style="margin:0">
<li><b>Up to 100&nbsp;Wh:</b> generally allowed in carry-on (FAA, IATA).</li>
<li><b>Over 100 up to 160&nbsp;Wh:</b> only with airline approval, and no more than two spares per person (FAA).</li>
<li><b>Over 160&nbsp;Wh:</b> usually not allowed on passenger aircraft (IATA).</li>
<li><b>Never in checked baggage.</b> If your carry-on gets gate-checked, take the batteries out first and keep them with you.</li>
</ul></div>

<h2>Where our kit lands</h2>
<p>Going by the manufacturers' stated capacities, the Zopec Explore Mini (99.5&nbsp;Wh), Medistrom Pilot-24 Lite (95&nbsp;Wh) and EcoFlow RAPID Pro (99.54&nbsp;Wh) are each just under 100&nbsp;Wh, so they fall in the "generally allowed in carry-on" group.</p>
<p>The FAA sets no quantity limit for most batteries under 100&nbsp;Wh, but it says many airlines have stricter limits on how many power banks each passenger can carry. <b>Check your airline's page before you pack two or three.</b></p>

<h2>Packing tips</h2>
<ul>
<li>Protect the terminals from short circuits: original packaging, a battery case or pouch, or tape over exposed contacts (FAA, IATA).</li>
<li>Make sure the Wh rating is printed on each battery. If it isn't, the FAA says Wh = volts &times; amp-hours. Carrying a printout of the spec page can help at security.</li>
<li>Don't fly with a swollen, damaged or recalled battery (FAA, IATA).</li>
<li>Empty the humidifier tub before packing the CPAP.</li>
</ul>

<h2>Flights to, from or within India</h2>
<p>In November 2025, India's aviation regulator (DGCA) issued an advisory that power banks and spare batteries must stay in hand baggage, and that <b>using or charging power banks on board is prohibited</b>, including from the seat's power outlet. It also says not to put them in overhead bins. Expect cabin crew on these flights to enforce this.</p>
<p>If you plan to use your CPAP <em>on the plane</em> on a long flight, ask the airline ahead of time. ResMed's user guide says the AirSense 11 meets FAA requirements for all phases of air travel, but whether you can run it on board, and from what power source, is the airline's call.</p>

<h2>What we couldn't confirm</h2>
<p>Rules about CPAP <em>machines</em> as medical devices (for example whether they count toward your cabin bag allowance) vary by airline and country. We haven't listed them here because we couldn't confirm one rule that applies everywhere. Ask your airline.</p>
''', ["faa","faa2","iata","dgca","resmed","zopec","medi","eco"])

# ---------------- INDIA
page("india.html","India power basics",
 "India's 230 V 50 Hz power, plug types C, D and M, and what that means for an AirSense 11 and a USB-C charger.",
'''<h1>India power basics</h1>
<p class="lede">India runs at <b>230&nbsp;V, 50&nbsp;Hz</b>, about twice the US voltage. The good news: modern CPAP and USB-C chargers are built for it. You mostly need the right plug shape and a plan for power cuts.</p>

<h2>Voltage: adapter yes, converter no</h2>
<ul>
<li>The AirSense 11's 65&nbsp;W power supply is rated <b>100–240&nbsp;V, 50–60&nbsp;Hz</b> (ResMed user guide). It works on Indian power with just a plug adapter.</li>
<li>Your USB-C charger needs to say <b>100–240&nbsp;V</b> on the label. For example, Anker lists its 100&nbsp;W chargers at 100–240&nbsp;V input. Check yours, because not every charger is dual-voltage.</li>
<li>A plug adapter only changes the plug shape. It does <b>not</b> change the voltage, so anything you plug in through it must itself be rated for 230&nbsp;V.</li>
</ul>

<h2>Plugs: C, D and M</h2>
<div class="table-wrap"><table style="min-width:420px">
<thead><tr><th>Type</th><th>What it looks like</th><th>Where you'll see it</th></tr></thead>
<tbody>
<tr><td><b>D</b></td><td>Three round pins in a triangle</td><td>The most common domestic plug in India (BIS)</td></tr>
<tr><td><b>C</b></td><td>Two thin round pins ("Europlug")</td><td>Low-power, two-pin devices</td></tr>
<tr><td><b>M</b></td><td>Three larger round pins</td><td>Higher-current appliances</td></tr>
</tbody></table></div>
<p>A US flat-pin plug won't fit. A travel adapter that offers a Type D plug covers most rooms. We carry a Ceptics India adapter.</p>

<h2>Power cuts</h2>
<p>Power cuts can come without warning and at any hour, sometimes briefly, sometimes for longer. If the home has backup power, check whether it actually covers the outlet by your bed. That's why we put a <a href="setup.html">UPS-style CPAP battery</a> in the chain every night, not just when an outage seems likely.</p>
<ul>
<li>Recharge the CPAP battery whenever power is available during the day.</li>
<li>Keep a charged power bank to top it up if the outage runs long.</li>
<li>Keep the humidifier and heated tube off on battery to stretch runtime.</li>
</ul>
<p>We don't give outage frequency numbers here because they vary a lot by city and neighbourhood, and we didn't find one reliable official figure to quote.</p>
''', ["resmed","anker","bis","iec"])

# ---------------- TEST
page("test.html","Test your setup before you fly",
 "A simple home test plan for a CPAP UPS battery setup: wall-yank tests, a dry overnight run and recharge timing.",
'''<h1>How to test your setup before you fly</h1>
<p class="lede">Find out at home, not on night one in a new place, whether your chain really survives a power cut. Here's the plan we're following.</p>

<h2>1. Start full</h2>
<p>Charge the CPAP battery to 100% and note how it's connected (charger, cables, adapter). Test the exact chain you'll travel with.</p>

<h2>2. Awake "wall-yank" tests (2–3 times)</h2>
<ol>
<li>Set up the full night chain: wall &rarr; charger &rarr; CPAP battery &rarr; AirSense 11.</li>
<li>Start therapy with the mask on, sitting up and awake.</li>
<li>Pull the charger out of the wall (or switch off the socket).</li>
<li>Watch and feel: does the CPAP <b>reboot</b>, show an error, or <b>pause airflow</b> even for a moment? Does the battery show it's now discharging?</li>
<li>Plug it back in and check it returns to pass-through and charging.</li>
</ol>
<p>Do it two or three times. A setup that passes once and fails once isn't good enough.</p>

<h2>3. A dry overnight on battery alone</h2>
<p>With the humidifier and heated tube <b>off</b>, sleep a whole night on the CPAP battery with the wall unplugged. In the morning, note how many hours you got and how much charge is left. That's your real number for your pressure and mask.</p>

<h2>4. Time the recharge</h2>
<ul>
<li>Time a full recharge from the wall charger.</li>
<li>Time a recharge from your power bank too (for us, the EcoFlow over USB-C) and note how much of the power bank it used. That tells you how many "rescue" top-ups you really have.</li>
</ul>

<h2>What to write down</h2>
<ul><li>Pressure setting and mask type</li><li>Did the CPAP blip or reboot on any wall-yank?</li><li>Hours on battery overnight, and % left</li><li>Recharge time: wall, and from power bank</li></ul>

<div class="card pending"><h2 style="margin-top:4px">Our test results: coming after our trip</h2><p>We haven't finished testing yet, so there are no numbers here on purpose. We'll post what actually happened, including anything that went wrong.</p></div>
''', ["zopecman","resmed","eco"])
print("built")
