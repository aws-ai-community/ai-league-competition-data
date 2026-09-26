#!/usr/bin/env python3
# Generate Agentic Football knockout bracket SVGs with uniform boxes and exact
# connector geometry (vector math, so it never drifts like ASCII spacing).
#
# Run from the repo root:  python scripts/render_bracket.py
# Renders every event defined in EVENTS below to its bracket.svg.

BOX_W, BOX_H = 190, 44
COL_GAP = 70          # horizontal gap between rounds
V_UNIT = 60           # vertical spacing unit for the first (widest) round
PAD_X, PAD_Y = 20, 20
LINE = "#5b6b7a"
BOX_FILL = "#ffffff"
BOX_STROKE = "#2f3b47"
WIN_FILL = "#eaf4ea"      # winner box tint
TXT = "#1a2530"
FONT = "font-family='Segoe UI, Helvetica, Arial, sans-serif'"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(rounds, titles, out_path):
    """rounds: list of rounds; each round is a list of matches
    (topTeam, topScore, botTeam, botScore, winner='top'|'bot').
    Round 0 is the widest; each later round has half as many matches."""
    n_rounds = len(rounds)
    n_first = len(rounds[0])

    # vertical centre of each match slot per round; each next-round box sits
    # exactly midway between its two feeders.
    centers = [[PAD_Y + 40 + i * V_UNIT * 2 + V_UNIT for i in range(n_first)]]
    for _ in range(1, n_rounds):
        prev = centers[-1]
        centers.append([(prev[2 * i] + prev[2 * i + 1]) / 2 for i in range(len(prev) // 2)])

    def col_x(r):
        return PAD_X + r * (BOX_W + COL_GAP)

    W = col_x(n_rounds - 1) + BOX_W + PAD_X + 40  # room for trophy on the right
    H = centers[0][-1] + V_UNIT + 60

    svg = [
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}' {FONT}>",
        f"<rect width='{W}' height='{H}' fill='#fbfcfd'/>",
    ]
    for r, t in enumerate(titles):
        x = col_x(r) + BOX_W / 2
        svg.append(f"<text x='{x:.0f}' y='24' text-anchor='middle' font-size='13' font-weight='700' fill='{TXT}'>{t}</text>")

    def box(x, cy, top, ts, bot, bs, winner):
        y = cy - BOX_H / 2
        top_win = winner == "top"
        parts = [f"<rect x='{x}' y='{y:.0f}' width='{BOX_W}' height='{BOX_H}' rx='5' fill='{BOX_FILL}' stroke='{BOX_STROKE}' stroke-width='1.2'/>"]
        parts.append(f"<line x1='{x}' y1='{y+BOX_H/2:.0f}' x2='{x+BOX_W}' y2='{y+BOX_H/2:.0f}' stroke='#dde3e8' stroke-width='1'/>")
        for k, (name, score, win) in enumerate([(top, ts, top_win), (bot, bs, not top_win)]):
            ry = y + k * (BOX_H / 2)
            if win:
                parts.append(f"<rect x='{x}' y='{ry:.0f}' width='{BOX_W}' height='{BOX_H/2:.0f}' fill='{WIN_FILL}'/>")
            fw = "700" if win else "400"
            parts.append(f"<text x='{x+10}' y='{ry+BOX_H/4+4:.0f}' font-size='12' font-weight='{fw}' fill='{TXT}'>{esc(name)}</text>")
            parts.append(f"<text x='{x+BOX_W-12}' y='{ry+BOX_H/4+4:.0f}' font-size='12' font-weight='{fw}' fill='{TXT}' text-anchor='end'>{score}</text>")
        parts.append(f"<rect x='{x}' y='{y:.0f}' width='{BOX_W}' height='{BOX_H}' rx='5' fill='none' stroke='{BOX_STROKE}' stroke-width='1.2'/>")
        return "".join(parts)

    # connectors
    for r in range(n_rounds - 1):
        for i in range(len(centers[r]) // 2):
            y1, y2 = centers[r][2 * i], centers[r][2 * i + 1]
            xr = col_x(r) + BOX_W
            xn = col_x(r + 1)
            ymid = centers[r + 1][i]
            midx = (xr + xn) / 2
            svg.append(f"<path d='M {xr} {y1:.0f} H {midx:.0f} V {y2:.0f} H {xr}' fill='none' stroke='{LINE}' stroke-width='1.3'/>")
            svg.append(f"<path d='M {midx:.0f} {ymid:.0f} H {xn}' fill='none' stroke='{LINE}' stroke-width='1.3'/>")

    # boxes
    for r, matches in enumerate(rounds):
        for i, m in enumerate(matches):
            svg.append(box(col_x(r), centers[r][i], m[0], m[1], m[2], m[3], m[4]))

    # trophy on the champion (final round, single match)
    champ_cy = centers[-1][0]
    cx = col_x(n_rounds - 1) + BOX_W + 16
    svg.append(f"<text x='{cx}' y='{champ_cy+5:.0f}' font-size='16'>🏆</text>")

    svg.append("</svg>")
    with open(out_path, "w") as f:
        f.write("\n".join(svg))
    print(f"wrote {out_path}  ({W}x{H})")


TITLES_16 = ["ROUND OF 16", "QUARTER-FINALS", "SEMI-FINALS", "FINAL"]

# --- Virtual APJ -----------------------------------------------------------
APJ = [
    [  # Round of 16
        ("Snow Halation FC", 3, "Ember Bolts", 0, "top"),
        ("Ember Keels", 4, "Daangipay", 5, "bot"),
        ("Ember Ironsides", 0, "sana", 2, "bot"),
        ("Ember Panthers", 2, "Ember Mephis", 1, "top"),
        ("LAFAEK FC", 4, "Ember Nomads", 5, "bot"),
        ("Yadavs' Team", 1, "Ember Cairns", 2, "bot"),
        ("Ember Badgers", 3, "Ember Ibises", 2, "top"),
        ("Ember Prongs", 2, "Ember Blades", 1, "top"),
    ],
    [  # Quarter-finals
        ("Snow Halation FC", 12, "Daangipay", 2, "top"),
        ("sana", 3, "Ember Panthers", 4, "bot"),
        ("Ember Cairns", 3, "Ember Nomads", 2, "top"),
        ("Ember Badgers", 5, "Ember Prongs", 1, "top"),
    ],
    [  # Semi-finals
        ("Snow Halation FC", 8, "Ember Panthers", 2, "top"),
        ("Ember Badgers", 6, "Ember Cairns", 2, "top"),
    ],
    [  # Final
        ("Snow Halation FC", 5, "Ember Badgers", 4, "top"),
    ],
]

# --- Virtual EMEA ----------------------------------------------------------
EMEA = [
    [  # Round of 16
        ("Real Ernesto", 5, "Lama Saint-Germain", 4, "top"),
        ("Blitz Cougars", 5, "Kiro-Five", 2, "top"),
        ("Blitz Crocodiles", 2, "FC Bayern Kerry", 4, "bot"),
        ("S3 Sirens FC", 1, "Spectral Shades", 3, "bot"),
        ("Divided United", 3, "Blitz Barbs", 4, "bot"),
        ("Beast Balls", 4, "Blitz Caldera", 2, "top"),
        ("Blitz Egrets", 2, "Helm Claws", 3, "bot"),
        ("MarkRoss", 14, "Blitz Cairns", 1, "top"),
    ],
    [  # Quarter-finals
        ("Real Ernesto", 0, "Blitz Cougars", 8, "bot"),
        ("FC Bayern Kerry", 4, "Spectral Shades", 1, "top"),
        ("Blitz Barbs", 4, "Beast Balls", 3, "top"),
        ("MarkRoss", 6, "Helm Claws", 4, "top"),
    ],
    [  # Semi-finals
        ("Blitz Cougars", 11, "FC Bayern Kerry", 0, "top"),
        ("MarkRoss", 5, "Blitz Barbs", 4, "top"),
    ],
    [  # Final
        ("Blitz Cougars", 8, "MarkRoss", 4, "top"),
    ],
]

EVENTS = [
    (APJ, TITLES_16, "competitions/2026/agentic-football/Virtual-APJ/bracket.svg"),
    (EMEA, TITLES_16, "competitions/2026/agentic-football/Virtual-EMEA/bracket.svg"),
]

if __name__ == "__main__":
    for rounds, titles, out in EVENTS:
        render(rounds, titles, out)
