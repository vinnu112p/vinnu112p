#!/usr/bin/env python3
"""
build_portfolio_window.py — creates a classy, minimal monochrome (black & grey)
browser mockup window for Vinayak's live portfolio.
"""

def generate_portfolio_svg(out_path="portfolio_window.svg"):
    w, h = 960, 420
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <linearGradient id="windowBg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#080808"/>
      <stop offset="100%" stop-color="#020202"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#121212"/>
      <stop offset="100%" stop-color="#080808"/>
    </linearGradient>
    <clipPath id="windowClip">
      <rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="12"/>
    </clipPath>
  </defs>

  <style>
    text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif; }}
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', Consolas, 'SF Mono', Menlo, monospace; }}
    .title {{ font-size: 34px; font-weight: 800; fill: #ffffff; letter-spacing: -0.5px; }}
    .sub {{ font-size: 13px; font-weight: 600; fill: #8b949e; letter-spacing: 2px; text-transform: uppercase; }}
    .desc {{ font-size: 14.5px; fill: #a0a6b0; }}
    .btn {{ transition: all 0.2s ease; cursor: pointer; }}
  </style>

  <!-- Outer Window Frame -->
  <g clip-path="url(#windowClip)">
    <!-- Canvas Background: Pure classy dark -->
    <rect x="0" y="0" width="{w}" height="{h}" fill="url(#windowBg)"/>

    <!-- Subtle Minimalist Grid lines in deep charcoal -->
    <g stroke="#1a1a1a" stroke-width="0.8" opacity="0.6">
      <line x1="80" y1="46" x2="80" y2="{h}"/>
      <line x1="280" y1="46" x2="280" y2="{h}"/>
      <line x1="480" y1="46" x2="480" y2="{h}"/>
      <line x1="680" y1="46" x2="680" y2="{h}"/>
      <line x1="880" y1="46" x2="880" y2="{h}"/>
      <line x1="0" y1="140" x2="{w}" y2="140"/>
      <line x1="0" y1="240" x2="{w}" y2="240"/>
      <line x1="0" y1="340" x2="{w}" y2="340"/>
    </g>

    <!-- Browser Header / Titlebar in matte charcoal -->
    <rect x="0" y="0" width="{w}" height="46" fill="#0f0f0f" stroke="#222222" stroke-width="1"/>
    
    <!-- Minimalist Monochrome Window Controls -->
    <circle cx="28" cy="23" r="5.5" fill="#262626" stroke="#333333" stroke-width="0.8"/>
    <circle cx="48" cy="23" r="5.5" fill="#262626" stroke="#333333" stroke-width="0.8"/>
    <circle cx="68" cy="23" r="5.5" fill="#262626" stroke="#333333" stroke-width="0.8"/>

    <!-- URL Bar -->
    <rect x="180" y="9" width="600" height="28" rx="6" fill="#050505" stroke="#262626" stroke-width="1"/>
    <!-- Padlock icon in grey -->
    <path d="M 204 25 v -4 a 4 4 0 0 1 8 0 v 4 m -6 0 h 12 a 2 2 0 0 1 2 2 v 5 a 2 2 0 0 1 -2 2 h -12 a 2 2 0 0 1 -2 -2 v -5 a 2 2 0 0 1 2 -2" fill="none" stroke="#8b949e" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    <text class="mono" x="228" y="27" fill="#d0d7de" font-size="12.5" font-weight="500">https://vinayak-studio.vercel.app</text>
    
    <!-- Status Badge in URL bar (monochrome) -->
    <g transform="translate(712, 15)">
      <circle cx="6" cy="8" r="3.5" fill="#ffffff"/>
      <text class="mono" x="15" y="11.5" fill="#ffffff" font-size="10.5" font-weight="600" letter-spacing="0.5px">ONLINE</text>
    </g>

    <!-- Subtle divider line under header -->
    <line x1="0" y1="46" x2="{w}" y2="46" stroke="#222222" stroke-width="1"/>

    <!-- Inside Content Showcase -->
    <!-- Pill tag -->
    <g transform="translate(60, 78)">
      <rect width="168" height="24" rx="12" fill="#141414" stroke="#2a2a2a" stroke-width="1"/>
      <circle cx="12" cy="12" r="3" fill="#ffffff"/>
      <text class="mono" x="24" y="15.5" fill="#c9d1d9" font-size="11" font-weight="600" letter-spacing="0.5px">CREATIVE STUDIO</text>
    </g>

    <!-- Main Title: Authentic Portfolio Typography -->
    <text class="title" x="60" y="146">VINAYAK PATEL</text>

    <!-- Subtitle -->
    <text class="sub" x="60" y="180">Full Stack Developer &amp; Motion Engineer</text>

    <!-- Description Paragraphs -->
    <text class="desc" x="60" y="218">A cinematic two-act web experience crafted with scroll-driven GSAP choreography,</text>
    <text class="desc" x="60" y="242">layered depth, and tactile micro-interactions built for feeling first.</text>

    <!-- Tech Stack Pill Badges (Monochrome Black & Grey) -->
    <g transform="translate(60, 276)">
      <!-- React -->
      <g transform="translate(0, 0)">
        <rect width="78" height="26" rx="5" fill="#121212" stroke="#262626"/>
        <text class="mono" x="14" y="17" fill="#c9d1d9" font-size="11.5" font-weight="500">React</text>
      </g>
      <!-- GSAP -->
      <g transform="translate(86, 0)">
        <rect width="74" height="26" rx="5" fill="#121212" stroke="#262626"/>
        <text class="mono" x="14" y="17" fill="#c9d1d9" font-size="11.5" font-weight="500">GSAP</text>
      </g>
      <!-- Tailwind -->
      <g transform="translate(168, 0)">
        <rect width="112" height="26" rx="5" fill="#121212" stroke="#262626"/>
        <text class="mono" x="14" y="17" fill="#c9d1d9" font-size="11.5" font-weight="500">Tailwind CSS</text>
      </g>
      <!-- JavaScript -->
      <g transform="translate(288, 0)">
        <rect width="102" height="26" rx="5" fill="#121212" stroke="#262626"/>
        <text class="mono" x="14" y="17" fill="#c9d1d9" font-size="11.5" font-weight="500">JavaScript</text>
      </g>
      <!-- Cinematic Motion -->
      <g transform="translate(398, 0)">
        <rect width="134" height="26" rx="5" fill="#121212" stroke="#262626"/>
        <text class="mono" x="14" y="17" fill="#c9d1d9" font-size="11.5" font-weight="500">Cinematic Motion</text>
      </g>
    </g>

    <!-- Action Buttons (Classy Monochrome) -->
    <g transform="translate(60, 330)">
      <!-- Primary Live Button -->
      <g class="btn">
        <rect width="210" height="42" rx="8" fill="#ffffff" stroke="#ffffff" stroke-width="1"/>
        <!-- External link icon in black -->
        <path d="M 27 21 h 8 M 35 21 l -4 -4 M 35 21 l -4 4" fill="none" stroke="#000000" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        <text class="mono" x="46" y="26" fill="#000000" font-size="13" font-weight="700">Open Live Studio ↗</text>
      </g>

      <!-- View Repo Button -->
      <g transform="translate(226, 0)" class="btn">
        <rect width="170" height="42" rx="8" fill="#141414" stroke="#2c2c2c" stroke-width="1.2"/>
        <!-- Code brackets in grey -->
        <path d="M 24 25 l -4 -4 l 4 -4 M 32 17 l 4 4 l -4 4" fill="none" stroke="#c9d1d9" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        <text class="mono" x="44" y="26" fill="#c9d1d9" font-size="13" font-weight="600">View Repo ↗</text>
      </g>
    </g>
  </g>

  <!-- Clean outer border in classy dark grey -->
  <rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="12" fill="none" stroke="#262626" stroke-width="1"/>
</svg>"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {out_path} ({w}x{h}) in classy black & grey successfully!")

if __name__ == "__main__":
    generate_portfolio_svg()
