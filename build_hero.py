#!/usr/bin/env python3
"""
build_hero.py — builds hero.svg for the profile README.

Left  : ASCII portrait cropped out of the gh-ascii card (your face, untouched)
Right : your own details, typed in one line at a time (CSS animation)
Look  : pure black, grey/white text

Usage (from repo root):
    curl -fL "https://gh.crafter.run/vinnu112p?theme=dark&cols=140" -o dark_mode.svg
    python build_hero.py
    -> writes hero.svg
"""
import base64, html, os, re, sys, urllib.request

USER = "vinnu112p"
SRC_URL = f"https://gh.crafter.run/{USER}?theme=dark&cols=140"
SRC_FILE = "dark_mode.svg"
OUT_FILE = "hero.svg"

CROP = 0.46        # fraction of original card width kept = portrait only (stats start at ~0.468).
                   # face cut off on the right -> raise. stats text leaking in -> lower.
LEFT_SKIP = 0.0    # fraction to trim from the left edge, if any
WIDTH = 1000       # final card width
PAD = 26
CW = 8.4           # approx monospace char width at 14px
LH = 25            # line height

# ─────────────── EDIT YOUR DETAILS HERE ───────────────
# ("title", text) · ("sec", text) · ("kv", label, value) · ("gap",)
ROWS = [
    ("title", "vinayak@vinnu112p"),
    ("kv", "Name", "Vinayak Patel"),
    ("kv", "Role", "Student · Full Stack Developer"),
    ("kv", "College", "Parul University, Vadodara"),
    ("kv", "Degree", "B.Tech CSE · Batch 2027"),
    ("kv", "Focus", "Premium UI · Web animation"),
    ("gap",),
    ("sec", "Stack"),
    ("kv", "Languages", "Java, Python, JavaScript, C"),
    ("kv", "Web", "React, Tailwind, Node, MongoDB"),
    ("gap",),
    ("sec", "Hobbies"),
    ("kv", "Play", "Gaming · Music"),
    ("kv", "Practice", "DSA · Competitive programming"),
    ("gap",),
    ("sec", "Contact"),
    ("kv", "Email", "patelvinnu.112@gmail.com"),
    ("kv", "GitHub", "github.com/vinnu112p"),
    ("kv", "LinkedIn", "in/vinayakpatell"),
    ("kv", "X", "@Patelvinnu112"),
    ("gap",),
    ("kv", "Open to", "Internships · Collaboration"),
]
# ───────────────────────────────────────────────────────


def load_source():
    if os.path.exists(SRC_FILE):
        return open(SRC_FILE, encoding="utf-8").read()
    print(f"{SRC_FILE} not found, downloading...")
    req = urllib.request.Request(SRC_URL, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=60).read().decode("utf-8")


def svg_size(raw):
    tag = re.search(r"<svg\b[^>]*>", raw).group(0)
    vb = re.search(r'viewBox="\s*([-\d.]+)[\s,]+([-\d.]+)[\s,]+([\d.]+)[\s,]+([\d.]+)', tag)
    if vb:
        return float(vb.group(3)), float(vb.group(4))
    w = re.search(r'\bwidth="([\d.]+)', tag)
    h = re.search(r'\bheight="([\d.]+)', tag)
    if w and h:
        return float(w.group(1)), float(h.group(1))
    sys.exit("Could not read SVG size from " + SRC_FILE)


def blacken(raw):
    """Turn the card's navy background pure black."""
    m = re.search(r'<rect\b[^>]*\bfill="(#[0-9a-fA-F]{3,8})"', raw)
    if not m:
        m = re.search(r"fill:\s*(#[0-9a-fA-F]{3,8})", raw)
    if m:
        bg = m.group(1)
        print("background colour found:", bg, "-> #000000")
        raw = re.sub(re.escape(bg), "#000000", raw, flags=re.I)
    else:
        print("no background colour found, left as is")
    return raw


def main():
    raw = blacken(load_source())
    W0, H0 = svg_size(raw)
    print(f"source card size: {W0} x {H0}")

    b64 = base64.b64encode(raw.encode("utf-8")).decode()

    crop_x = W0 * LEFT_SKIP
    crop_w = W0 * (CROP - LEFT_SKIP)
    p_h = 500
    p_w = p_h * crop_w / H0
    px, py = PAD, PAD

    rx0 = px + p_w + 34           # right panel start
    rx1 = WIDTH - PAD - 10        # right panel end

    # layout right panel
    y = 0
    laid = []
    for r in ROWS:
        laid.append((r, y))
        y += LH if r[0] != "gap" else LH * 0.55
    content_h = y
    total_h = max(p_h, content_h) + PAD * 2
    top = py + (total_h - PAD * 2 - content_h) / 2 + 16

    out = []
    a = out.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {total_h:.0f}" width="{WIDTH}" height="{total_h:.0f}">')
    a("""<style>
      text{font-family:'JetBrains Mono','Fira Code',Consolas,'SF Mono',Menlo,monospace;font-size:14px}
      .t{fill:#ffffff;font-weight:700}
      .s{fill:#ffffff;font-weight:600}
      .l{fill:#8b949e}
      .v{fill:#e6edf3}
      .r{opacity:0;animation:in .55s ease-out forwards}
      .p{opacity:0;animation:pf 1.4s ease-out .1s forwards}
      .scan{animation:sweep 5s linear 1.6s infinite}
      .cur{animation:blink 1s steps(2,start) infinite}
      @keyframes in{from{opacity:0;transform:translateX(-10px)}to{opacity:1;transform:translateX(0)}}
      @keyframes pf{from{opacity:0}to{opacity:1}}
      @keyframes sweep{0%{transform:translateY(-60px)}100%{transform:translateY(%dpx)}}
      @keyframes blink{to{visibility:hidden}}
    </style>""".replace("%d", str(int(p_h + 60))))
    a("<defs>")
    a(f'<clipPath id="pc"><rect x="{px}" y="{py}" width="{p_w:.1f}" height="{p_h}" rx="6"/></clipPath>')
    a('<linearGradient id="sg" x1="0" y1="0" x2="0" y2="1">'
      '<stop offset="0" stop-color="#fff" stop-opacity="0"/>'
      '<stop offset=".5" stop-color="#fff" stop-opacity=".10"/>'
      '<stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>')
    a("</defs>")

    # card
    a(f'<rect x=".5" y=".5" width="{WIDTH-1}" height="{total_h-1:.0f}" rx="14" fill="#000" stroke="#262626"/>')

    # portrait (cropped via nested svg viewBox)
    a('<g class="p">')
    a(f'<svg x="{px}" y="{py}" width="{p_w:.1f}" height="{p_h}" viewBox="{crop_x:.1f} 0 {crop_w:.1f} {H0}" preserveAspectRatio="xMidYMid slice">'
      f'<image href="data:image/svg+xml;base64,{b64}" x="0" y="0" width="{W0}" height="{H0}"/></svg>')
    a('<g clip-path="url(#pc)">'
      f'<rect class="scan" x="{px}" y="{py}" width="{p_w:.1f}" height="60" fill="url(#sg)"/></g>')
    a("</g>")

    # right panel
    delay = 0.5
    for r, ry in laid:
        kind = r[0]
        if kind == "gap":
            continue
        yy = top + ry
        a(f'<g class="r" style="animation-delay:{delay:.2f}s">')
        if kind == "title":
            a(f'<text class="t" x="{rx0:.1f}" y="{yy:.1f}">{html.escape(r[1])}</text>')
            x_line = rx0 + (len(r[1]) + 1) * CW
            a(f'<line x1="{x_line:.1f}" y1="{yy-5:.1f}" x2="{rx1:.1f}" y2="{yy-5:.1f}" stroke="#30363d"/>')
        elif kind == "sec":
            a(f'<text class="s" x="{rx0:.1f}" y="{yy:.1f}">{html.escape(r[1])}</text>')
            x_line = rx0 + (len(r[1]) + 1) * CW
            a(f'<line x1="{x_line:.1f}" y1="{yy-5:.1f}" x2="{rx1:.1f}" y2="{yy-5:.1f}" stroke="#30363d"/>')
        else:
            label, val = r[1], r[2]
            a(f'<text class="l" x="{rx0:.1f}" y="{yy:.1f}">. {html.escape(label)}:</text>')
            a(f'<text class="v" x="{rx1:.1f}" y="{yy:.1f}" text-anchor="end">{html.escape(val)}</text>')
            x_a = rx0 + (len(label) + 4) * CW
            x_b = rx1 - (len(val) + 1) * CW
            if x_b > x_a:
                a(f'<line x1="{x_a:.1f}" y1="{yy-4:.1f}" x2="{x_b:.1f}" y2="{yy-4:.1f}" '
                  f'stroke="#3d444d" stroke-width="1.5" stroke-dasharray="1 5" stroke-linecap="round"/>')
        a("</g>")
        delay += 0.12

    # blinking cursor after last row
    last_y = top + laid[-1][1]
    a(f'<rect class="cur" x="{rx0:.1f}" y="{last_y+LH-11:.1f}" width="9" height="16" fill="#e6edf3"/>')
    a("</svg>")

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"wrote {OUT_FILE} ({WIDTH} x {total_h:.0f}). Open it in a browser to check.")


if __name__ == "__main__":
    main()
