#!/usr/bin/env python3
# Generate the Agentic Football knockout bracket SVG with uniform boxes and
# exact connector geometry (vector math, so it never drifts like ASCII spacing).
# Output: competitions/2026/agentic-football/Virtual-APJ/bracket.svg
# Run from the repo root: python scripts/render_bracket.py
BOX_W, BOX_H = 190, 44
COL_GAP = 70          # horizontal gap between rounds
V_UNIT = 60           # vertical spacing unit for round-of-16 slots
PAD_X, PAD_Y = 20, 20
LINE = "#5b6b7a"
BOX_FILL = "#ffffff"
BOX_STROKE = "#2f3b47"
WIN_FILL = "#eaf4ea"      # winner box tint
TXT = "#1a2530"
FONT = "font-family='Segoe UI, Helvetica, Arial, sans-serif'"

# Matches per round as (topTeam, topScore, botTeam, botScore, winner='top'|'bot')
R16 = [
  ("Snow Halation FC",3,"Ember Bolts",0,"top"),
  ("Ember Keels",4,"Daangipay",5,"bot"),
  ("Ember Ironsides",0,"sana",2,"bot"),
  ("Ember Panthers",2,"Ember Mephis",1,"top"),
  ("LAFAEK FC",4,"Ember Nomads",5,"bot"),
  ("Yadavs' Team",1,"Ember Cairns",2,"bot"),
  ("Ember Badgers",3,"Ember Ibises",2,"top"),
  ("Ember Prongs",2,"Ember Blades",1,"top"),
]
QF = [
  ("Snow Halation FC",12,"Daangipay",2,"top"),
  ("sana",3,"Ember Panthers",4,"bot"),
  ("Ember Cairns",3,"Ember Nomads",2,"top"),
  ("Ember Badgers",5,"Ember Prongs",1,"top"),
]
SF = [
  ("Snow Halation FC",8,"Ember Panthers",2,"top"),
  ("Ember Badgers",6,"Ember Cairns",2,"top"),
]
FN = [
  ("Snow Halation FC",5,"Ember Badgers",4,"top"),
]
rounds=[R16,QF,SF,FN]
titles=["ROUND OF 16","QUARTER-FINALS","SEMI-FINALS","FINAL"]

# vertical center of each match slot per round
# R16: 8 matches evenly spaced. Each subsequent round centers between its two feeders.
centers=[]
base=[PAD_Y + 40 + i*V_UNIT*2 + V_UNIT for i in range(8)]  # 8 R16 centers
centers.append(base)
for r in range(1,4):
    prev=centers[-1]
    cur=[(prev[2*i]+prev[2*i+1])/2 for i in range(len(prev)//2)]
    centers.append(cur)

def col_x(r): return PAD_X + r*(BOX_W+COL_GAP)
W = col_x(4) + PAD_X
H = base[-1] + V_UNIT + 60

svg=[]
svg.append(f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}' {FONT}>")
svg.append(f"<rect width='{W}' height='{H}' fill='#fbfcfd'/>")
# round titles
for r,t in enumerate(titles):
    x=col_x(r)+BOX_W/2
    svg.append(f"<text x='{x:.0f}' y='24' text-anchor='middle' font-size='13' font-weight='700' fill='{TXT}'>{t}</text>")

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def box(x, cy, top, ts, bot, bs, winner):
    y=cy-BOX_H/2
    top_win = winner=="top"
    parts=[]
    parts.append(f"<rect x='{x}' y='{y:.0f}' width='{BOX_W}' height='{BOX_H}' rx='5' fill='{BOX_FILL}' stroke='{BOX_STROKE}' stroke-width='1.2'/>")
    # divider
    parts.append(f"<line x1='{x}' y1='{y+BOX_H/2:.0f}' x2='{x+BOX_W}' y2='{y+BOX_H/2:.0f}' stroke='#dde3e8' stroke-width='1'/>")
    for k,(name,score,win) in enumerate([(top,ts,top_win),(bot,bs,not top_win)]):
        ry=y+k*(BOX_H/2)
        if win:
            parts.append(f"<rect x='{x}' y='{ry:.0f}' width='{BOX_W}' height='{BOX_H/2:.0f}' rx='0' fill='{WIN_FILL}'/>")
        fw="700" if win else "400"
        parts.append(f"<text x='{x+10}' y='{ry+BOX_H/4+4:.0f}' font-size='12' font-weight='{fw}' fill='{TXT}'>{esc(name)}</text>")
        parts.append(f"<text x='{x+BOX_W-12}' y='{ry+BOX_H/4+4:.0f}' font-size='12' font-weight='{fw}' fill='{TXT}' text-anchor='end'>{score}</text>")
    # re-stroke border on top of winner fill
    parts.append(f"<rect x='{x}' y='{y:.0f}' width='{BOX_W}' height='{BOX_H}' rx='5' fill='none' stroke='{BOX_STROKE}' stroke-width='1.2'/>")
    return "".join(parts)

# connectors: from each pair of boxes in round r to the box in round r+1
for r in range(3):
    for i in range(len(centers[r])//2):
        y1=centers[r][2*i]; y2=centers[r][2*i+1]
        xr=col_x(r)+BOX_W
        xn=col_x(r+1)
        ymid=centers[r+1][i]
        midx=(xr+xn)/2
        svg.append(f"<path d='M {xr} {y1:.0f} H {midx:.0f} V {y2:.0f} H {xr}' fill='none' stroke='{LINE}' stroke-width='1.3'/>")
        svg.append(f"<path d='M {midx:.0f} {ymid:.0f} H {xn}' fill='none' stroke='{LINE}' stroke-width='1.3'/>")

# boxes
for r,matches in enumerate(rounds):
    for i,m in enumerate(matches):
        svg.append(box(col_x(r), centers[r][i], m[0],m[1],m[2],m[3],m[4]))

# champion label + trophy
champ_cy=centers[3][0]
cx=col_x(3)+BOX_W+16
svg.append(f"<text x='{cx}' y='{champ_cy+5:.0f}' font-size='16'>🏆</text>")

svg.append("</svg>")
open("competitions/2026/agentic-football/Virtual-APJ/bracket.svg","w").write("\n".join(svg))
print("wrote bracket.svg  (%dx%d)"%(W,H))
