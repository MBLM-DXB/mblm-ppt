#!/usr/bin/env python3
"""Generate MBLM R2 deck semantic SVGs — compact data-driven builder."""
from __future__ import annotations
from pathlib import Path

OUT = Path("/workspace/mblm-ppt-master/templates/decks/mblm-r2/templates")
FONT = "BentonSansCond, Arial Narrow, Arial, sans-serif"
LOGO_L = "../images/MBLM_LOGO_White background.svg"
LOGO_D = "../images/MBLM_LOGO_dark background.svg"
C = dict(bk="#000000", wh="#FFFFFF", gy="#E5E5E5", gl="#BFBFBF", gd="#9CA3AF",
         gt="#6B7280", gw="#F2F2F2", bl="#00AEFF", bm="#006AF1", nv="#002A60",
         ba="#0068EB", yl="#F2B75A", rd="#D65F6D")

def E(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"','&quot;')

def open_svg(lid, lname):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"\n'
            f'  width="1280" height="720" viewBox="0 0 1280 720"\n'
            f'  data-pptx-master="mblm_r2_master" data-pptx-master-name="MBLM R2 Consulting"\n'
            f'  data-pptx-layout="{lid}" data-pptx-layout-name="{E(lname)}">\n')

def bg(fill=None):
    fill = fill or C["wh"]
    return (f'  <rect id="master-bg" x="0" y="0" width="1280" height="720" fill="{fill}"\n'
            f'    data-pptx-layer="master" data-pptx-editable="false"/>\n')

def logo(dark=False):
    if dark:
        return (f'  <image id="layout-logo" x="40" y="40" width="138" height="69"\n'
                f'    href="{LOGO_D}" preserveAspectRatio="xMidYMid meet"\n'
                f'    data-pptx-layer="layout" data-pptx-editable="false" data-pptx-role="logo"/>\n')
    return (f'  <image id="layout-logo" x="1148.2" y="39.7" width="88.4" height="44.2"\n'
            f'    href="{LOGO_L}" preserveAspectRatio="xMidYMid meet"\n'
            f'    data-pptx-layer="layout" data-pptx-editable="false" data-pptx-role="logo"/>\n')

def title(tok="{{TITLE}}", x=40, y=40, w=1080, h=60, fill=None, size=47, weight="300", anchor="start"):
    fill = fill or C["bk"]
    ty = y + 42
    ta = f' text-anchor="{anchor}"' if anchor != "start" else ""
    tx = x if anchor == "start" else (x + w if anchor == "end" else x + w/2)
    return (f'  <g id="title-slot" data-pptx-placeholder="title" data-pptx-bounds="{x:g} {y:g} {w:g} {h:g}">\n'
            f'    <text id="title-carrier" data-pptx-carrier="true" x="{tx:g}" y="{ty:g}" fill="{fill}"{ta}\n'
            f'      font-family="{FONT}" font-size="{size}" font-weight="{weight}">{E(tok)}</text>\n'
            f'  </g>\n')

def slot(pid, tok, x, y, w, h, fill=None, size=16, weight="400", anchor="start", idx=None, ph="body"):
    fill = fill or C["bk"]
    ty = y + size + 4
    ta = f' text-anchor="{anchor}"' if anchor != "start" else ""
    tx = x if anchor == "start" else (x + w if anchor == "end" else x + w/2)
    ia = f' data-pptx-idx="{idx}"' if idx is not None else ""
    return (f'  <g id="{pid}" data-pptx-placeholder="{ph}"{ia} data-pptx-bounds="{x:g} {y:g} {w:g} {h:g}">\n'
            f'    <text id="{pid}-carrier" data-pptx-carrier="true" x="{tx:g}" y="{ty:g}" fill="{fill}"{ta}\n'
            f'      font-family="{FONT}" font-size="{size}" font-weight="{weight}">{E(tok)}</text>\n'
            f'  </g>\n')

def page():
    return (f'  <g id="page-number-slot" data-pptx-placeholder="slide-number" data-pptx-bounds="1200 680 40 24">\n'
            f'    <text id="page-number-carrier" data-pptx-carrier="true" x="1240" y="698" text-anchor="end" fill="{C["bk"]}"\n'
            f'      font-family="{FONT}" font-size="12">{{{{PAGE}}}}</text>\n'
            f'  </g>\n')

def source(tok="{{SOURCE}}"):
    return (f'  <g id="source-slot" data-pptx-placeholder="body" data-pptx-idx="90" data-pptx-bounds="40 680 400 20">\n'
            f'    <text id="source-carrier" data-pptx-carrier="true" x="40" y="694" fill="{C["gt"]}"\n'
            f'      font-family="{FONT}" font-size="11">{E(tok)}</text>\n'
            f'  </g>\n')

def rect(iid, x, y, w, h, fill, stroke=None, sw=1, rx=0):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    rxA = f' rx="{rx}"' if rx else ""
    return (f'  <rect id="{iid}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{fill}"{st}{rxA}\n'
            f'    data-pptx-layer="layout" data-pptx-editable="false"/>\n')

def circle(iid, cx, cy, r, fill):
    return (f'  <circle id="{iid}" cx="{cx:g}" cy="{cy:g}" r="{r:g}" fill="{fill}"\n'
            f'    data-pptx-layer="layout" data-pptx-editable="false"/>\n')

def line(iid, x1, y1, x2, y2, stroke, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'  <line id="{iid}" x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{stroke}" stroke-width="{sw}"{d}\n'
            f'    data-pptx-layer="layout" data-pptx-editable="false"/>\n')

def poly(iid, points, fill):
    return (f'  <polygon id="{iid}" points="{points}" fill="{fill}"\n'
            f'    data-pptx-layer="layout" data-pptx-editable="false"/>\n')

def static_text(iid, x, y, text, fill, size, weight="400", anchor="start"):
    ta = f' text-anchor="{anchor}"' if anchor != "start" else ""
    return (f'  <text id="{iid}" x="{x:g}" y="{y:g}" fill="{fill}"{ta}\n'
            f'    font-family="{FONT}" font-size="{size}" font-weight="{weight}"\n'
            f'    data-pptx-layer="layout" data-pptx-editable="false">{E(text)}</text>\n')

def chev(x, y, w, h, notch=18):
    return f"{x:g},{y:g} {x+w-notch:g},{y:g} {x+w:g},{y+h/2:g} {x+w-notch:g},{y+h:g} {x:g},{y+h:g} {x+notch:g},{y+h/2:g}"

def bullets(pid, n, x, y, w, tok_fmt, line_h=50, size=15, idx0=10):
    parts = []
    for i in range(n):
        by = y + i * line_h
        parts.append(circle(f"{pid}-b{i}", x+6, by+10, 3.5, C["bk"]))
        parts.append(slot(f"{pid}-t{i}", tok_fmt.format(i=i+1), x+18, by, w-18, line_h-4, size=size, idx=idx0+i))
    return "".join(parts)

def finish(parts):
    parts.append("</svg>\n")
    return "".join(parts)


# --- builders ---
def build_r2_02():
    p=[open_svg("objectives_two_column","Objectives Two Column"),bg(),logo(),title()]
    p.append(slot("intro","{{INTRO}}",40,120,1200,40,size=18,weight="700",idx=0))
    for col,bx in enumerate([40,660]):
        p.append(bullets(f"c{col}",4,bx,190,540,f"{{{{COL_{col+1}_ITEM_{{i}}}}}}",line_h=50,idx0=10+col*10))
    p.append(page()); return finish(p)

def build_r2_03():
    p=[open_svg("content_vs_structure","Content vs Structure"),bg(),logo(),title()]
    p.append(line("div",640,130,640,640,C["gd"],1.5,"4 6"))
    for i,x in enumerate([40,680]):
        p.append(rect(f"h{i}",x,130,520,48,C["bk"]))
        p.append(slot(f"ht{i}",f"{{{{COLUMN_{i+1}_TITLE}}}}",x,130,520,48,fill=C["wh"],size=20,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(circle(f"ic{i}",x+260,230,36,C["bk"]))
        p.append(rect(f"icg{i}",x+240,214,40,32,C["gy"]))
        p.append(bullets(f"c{i}",3,x+10,300,480,f"{{{{COLUMN_{i+1}_ITEM_{{i}}}}}}",line_h=50,idx0=20+i*10))
    p.append(page()); return finish(p)

def build_r2_04():
    p=[open_svg("from_to_compare","From-To Comparison"),bg(),logo(),title()]
    p.append(rect("fh",40,130,560,44,C["bk"]))
    p.append(slot("ft","{{FROM_TITLE}}",40,130,560,44,fill=C["wh"],size=18,weight="700",anchor="middle",idx=1,ph="subtitle"))
    p.append(rect("th",680,130,560,44,C["bl"]))
    p.append(slot("tt","{{TO_TITLE}}",680,130,560,44,fill=C["wh"],size=18,weight="700",anchor="middle",idx=2,ph="subtitle"))
    for r in range(4):
        y=200+r*100
        p.append(line(f"r{r}",40,y+80,1240,y+80,C["gd"],1,"4 4"))
        p.append(slot(f"fr{r}",f"{{{{FROM_ROW_{r+1}}}}}",40,y,520,70,size=15,idx=10+r))
        p.append(poly(f"tr{r}",f"640,{y+20} 660,{y+35} 640,{y+50}",C["bk"]))
        p.append(slot(f"tor{r}",f"{{{{TO_ROW_{r+1}}}}}",680,y,520,70,size=15,idx=20+r))
    p.append(page()); return finish(p)

def build_r2_05():
    p=[open_svg("three_column_cards","Three Column Cards"),bg(),logo(),title()]
    cw,gap=380,30
    for c in range(3):
        x=40+c*(cw+gap)
        p.append(rect(f"ch{c}",x,130,cw,48,C["bk"]))
        p.append(slot(f"cht{c}",f"{{{{COL_{c+1}_HEADER}}}}",x,130,cw,48,fill=C["wh"],size=20,weight="700",anchor="middle",idx=c+1,ph="subtitle"))
        p.append(rect(f"cb{c}",x,178,cw,280,C["wh"],stroke=C["bk"],sw=1.5))
        p.append(bullets(f"c{c}",3,x+12,200,cw-30,f"{{{{COL_{c+1}_ITEM_{{i}}}}}}",line_h=70,idx0=10+c*10))
        cx=x+cw/2
        p.append(poly(f"ar{c}",f"{cx-14},475 {cx+14},475 {cx},498",C["bl"]))
        p.append(rect(f"cf{c}",x,510,cw,120,C["gy"]))
        p.append(slot(f"cft{c}",f"{{{{COL_{c+1}_SUMMARY}}}}",x+16,530,cw-32,80,size=16,weight="700",idx=40+c))
    p.append(page()); return finish(p)

def build_r2_06():
    p=[open_svg("scr_bc_framework","SCR+bc Framework"),bg(),logo(),title()]
    for i in range(5):
        y=140+i*95
        p.append(rect(f"rl{i}",40,y,180,70,C["bk"]))
        p.append(slot(f"rlt{i}",f"{{{{ROW_{i+1}_LABEL}}}}",40,y,180,70,fill=C["wh"],size=16,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(poly(f"ra{i}",f"240,{y+20} 260,{y+35} 240,{y+50}",C["bl"]))
        p.append(rect(f"rb{i}",280,y,960,70,C["gw"]))
        p.append(slot(f"rbt{i}",f"{{{{ROW_{i+1}_BODY}}}}",300,y+10,920,50,size=16,idx=20+i))
    p.append(page()); return finish(p)

def build_r2_07():
    p=[open_svg("scr_proposal_flow","SCR Proposal Flow"),bg(),logo(),title()]
    p.append(line("flow",100,280,1180,280,C["bl"],3))
    w,gap=260,40
    for i in range(4):
        x=40+i*(w+gap)
        p.append(rect(f"sh{i}",x,140,w,44,C["bk"]))
        p.append(slot(f"sht{i}",f"{{{{STAGE_{i+1}_TITLE}}}}",x,140,w,44,fill=C["wh"],size=16,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(circle(f"sn{i}",x+w/2,280,10,C["bl"]))
        for j in range(2):
            by=320+j*120
            p.append(rect(f"sb{i}{j}",x,by,w,100,C["wh"],stroke=C["gl"],sw=1.5))
            p.append(slot(f"sbt{i}{j}",f"{{{{STAGE_{i+1}_BOX_{j+1}}}}}",x+12,by+20,w-24,60,size=14,idx=20+i*5+j))
    p.append(page()); return finish(p)

def build_r2_08():
    p=[open_svg("scr_tips_rail","SCR Tips Left Rail"),bg(),logo(),title()]
    p.append(rect("rail",40,140,160,48,C["bk"]))
    p.append(slot("railt","{{RAIL_LABEL}}",40,140,160,48,fill=C["wh"],size=16,weight="700",anchor="middle",idx=1,ph="subtitle"))
    p.append(line("vr",220,140,220,640,C["gl"],2))
    p.append(bullets("tips",4,236,160,960,"{{TIP_{i}}}",line_h=110,size=16,idx0=10))
    p.append(page()); return finish(p)

def build_r2_09():
    p=[open_svg("executive_summary","Executive Summary"),bg(),logo(),title()]
    p.append(line("d1",440,140,440,640,C["gd"],1.5,"4 6"))
    p.append(line("d2",840,140,840,640,C["gd"],1.5,"4 6"))
    for i,(x,w) in enumerate([(40,380),(460,360),(860,380)]):
        p.append(rect(f"ch{i}",x,140,w,80,C["gy"]))
        p.append(circle(f"ci{i}",x+40,180,22,C["bk"]))
        p.append(slot(f"cht{i}",f"{{{{COLUMN_{i+1}_TITLE}}}}",x+70,155,w-90,50,size=18,weight="700",idx=i+1,ph="subtitle"))
        p.append(bullets(f"c{i}",3,x+8,250,w-20,f"{{{{COLUMN_{i+1}_ITEM_{{i}}}}}}",line_h=80,idx0=10+i*10))
    p.append(page()); return finish(p)

def build_r2_10():
    p=[open_svg("summary_proposal","Summary of Proposal"),bg(),logo(),title()]
    colors=[C["bk"],C["bm"],C["nv"]]; cw,gap=360,40
    for c in range(3):
        x=40+c*(cw+gap)
        p.append(rect(f"ch{c}",x,130,cw,48,colors[c]))
        p.append(slot(f"cht{c}",f"{{{{COLUMN_{c+1}_TITLE}}}}",x,130,cw,48,fill=C["wh"],size=20,weight="700",anchor="middle",idx=c+1,ph="subtitle"))
        p.append(bullets(f"c{c}",4,x+8,210,cw-20,f"{{{{COLUMN_{c+1}_ITEM_{{i}}}}}}",line_h=90,idx0=10+c*10))
        if c<2:
            sx=x+cw+gap/2
            p.append(line(f"sep{c}",sx,200,sx,620,C["gl"],1))
            p.append(circle(f"nd{c}",sx,400,14,C["bk"]))
            p.append(poly(f"chv{c}",f"{sx-4},392 {sx+6},400 {sx-4},408",C["wh"]))
    p.append(page()); return finish(p)

def build_r2_11():
    p=[open_svg("client_purpose_circles","Client Purpose Circles"),bg(),logo(),title()]
    fills=["#D6E9FF","#7EB6F5",C["bm"],C["bk"]]; tfs=[C["bk"],C["bk"],C["wh"],C["wh"]]
    for i in range(4):
        cx=160+i*300
        p.append(circle(f"c{i}",cx,280,90,fills[i]))
        p.append(slot(f"cl{i}",f"{{{{CIRCLE_{i+1}_LABEL}}}}",cx-70,cy:=260,140,40,fill=tfs[i],size=16,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(slot(f"cd{i}",f"{{{{CIRCLE_{i+1}_DESC}}}}",cx-110,400,220,160,size=14,anchor="middle",idx=10+i))
    p.append(page()); return finish(p)

def build_r2_12():
    p=[open_svg("content_toc","Content TOC"),bg(),logo(),title()]
    p.append(line("spine",80,300,1200,300,C["gd"],1.5,"6 6"))
    for i in range(6):
        cx=140+i*200; num=f"{i+1:02d}"
        p.append(circle(f"tc{i}",cx,300,42,C["bk"]))
        p.append(static_text(f"tn{i}",cx,310,num,C["wh"],28,"700","middle"))
        p.append(slot(f"st{i}",f"{{{{SECTION_{i+1:02d}_TITLE}}}}",cx-90,370,180,36,size=16,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(slot(f"sd{i}",f"{{{{SECTION_{i+1:02d}_DESC}}}}",cx-90,420,180,80,size=13,anchor="middle",idx=20+i))
    p.append(page()); return finish(p)

def build_r2_13():
    p=[open_svg("list_photo_split","List Photo Split"),bg(),logo(),title()]
    p.append(rect("well",40,130,600,500,C["gw"]))
    p.append(bullets("items",5,56,160,540,"{{ITEM_{i}}}",line_h=80,idx0=10))
    p.append(rect("photo",680,130,560,500,C["gy"]))
    p.append(slot("img","{{IMAGE}}",680,350,560,40,fill=C["gt"],size=14,anchor="middle",idx=50,ph="object"))
    p.append(source()); p.append(page()); return finish(p)

def build_r2_14():
    p=[open_svg("background_timeline","Background Timeline"),bg(),logo(),title()]
    p.append(rect("well",40,130,560,500,C["gw"]))
    p.append(slot("prose","{{PROSE}}",60,160,520,440,size=16,idx=1))
    p.append(line("tl",760,160,760,620,C["gd"],1.5,"4 6"))
    for i in range(4):
        cy=200+i*120
        p.append(circle(f"tn{i}",760,cy,14,C["bk"]))
        p.append(slot(f"tt{i}",f"{{{{TIMELINE_{i+1}}}}}",800,cy-20,400,80,size=15,idx=10+i))
    p.append(page()); return finish(p)

def build_r2_15():
    p=[open_svg("four_pillars","Four Pillars"),bg(),logo(),title()]
    for i in range(4):
        cx=160+i*300
        p.append(rect(f"ic{i}",cx-40,160,80,80,C["gy"]))
        p.append(slot(f"icl{i}","{{IMAGE}}",cx-40,185,80,30,fill=C["gt"],size=11,anchor="middle",idx=50+i,ph="object"))
        p.append(slot(f"r{i}",f"{{{{REASON_{i+1:02d}}}}}",cx-120,280,240,80,size=18,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(slot(f"d{i}",f"{{{{DESC_{i+1:02d}}}}}",cx-120,380,240,160,size=14,anchor="middle",idx=20+i))
    p.append(source()); p.append(page()); return finish(p)

def build_r2_16():
    p=[open_svg("solution_pillars","Solution Pillars"),bg(),logo(),title()]
    fills=[C["bk"],C["nv"],C["bm"],C["bl"]]
    for i in range(4):
        cx=160+i*300
        p.append(circle(f"c{i}",cx,200,48,fills[i]))
        p.append(rect(f"ig{i}",cx-20,180,40,40,C["gy"]))
        p.append(slot(f"h{i}",f"{{{{PILLAR_{i+1}_TITLE}}}}",cx-120,280,240,60,size=18,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(slot(f"b{i}",f"{{{{PILLAR_{i+1}_BODY}}}}",cx-120,360,240,200,size=14,anchor="middle",idx=20+i))
    p.append(page()); return finish(p)


def build_r2_17():
    p=[open_svg("solution_gallery","Solution Gallery"),bg(),logo(),title()]
    tw,th,gx,gy=280,200,30,30
    for r in range(2):
        for c in range(4):
            i=r*4+c; x=40+c*(tw+gx); y=130+r*(th+gy)
            p.append(rect(f"th{i}",x,y,tw,th,C["gy"],stroke=C["gl"]))
            p.append(slot(f"tht{i}",f"{{{{THUMB_{i+1}}}}}",x,y+th/2-10,tw,30,fill=C["gt"],size=13,anchor="middle",idx=10+i,ph="object"))
    p.append(page()); return finish(p)

def build_r2_18():
    p=[open_svg("business_case_blocks","Business Case Blocks"),bg(),logo(),title()]
    for row in range(2):
        y=160+row*160
        for i in range(3):
            x=60+i*220; fill=C["bm"] if (row+i)%2==0 else C["bk"]
            p.append(rect(f"p{row}{i}",x,y,150,100,fill))
            p.append(slot(f"pt{row}{i}",f"{{{{PARAM_{row*3+i+1}}}}}",x,y+30,150,40,fill=C["wh"],size=14,weight="700",anchor="middle",idx=10+row*3+i))
            if i<2: p.append(static_text(f"x{row}{i}",x+180,y+60,"×",C["bk"],28,"700","middle"))
        p.append(static_text(f"eq{row}",760,y+60,"=",C["bk"],28,"700","middle"))
        p.append(rect(f"res{row}",800,y,150,100,C["nv"]))
        p.append(slot(f"rest{row}",f"{{{{RESULT_{row+1}}}}}",800,y+30,150,40,fill=C["wh"],size=14,weight="700",anchor="middle",idx=30+row))
    p.append(rect("call",40,500,1200,120,C["gw"]))
    p.append(circle("cb",70,560,3.5,C["bk"]))
    p.append(slot("ct","{{CALLOUT}}",86,540,1120,60,size=16,idx=40))
    p.append(page()); return finish(p)

def build_r2_19():
    p=[open_svg("strategy_five_pillars","Strategy Five Pillars"),bg(),logo(),title()]
    for i in range(5):
        cx=128+i*250
        p.append(circle(f"c{i}",cx,180,40,C["bk"]))
        p.append(rect(f"ig{i}",cx-16,164,32,32,C["gy"]))
        p.append(line(f"dl{i}",cx,220,cx,280,C["gl"],1.5))
        p.append(slot(f"h{i}",f"{{{{PILLAR_{i+1}_TITLE}}}}",cx-100,300,200,50,size=16,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(slot(f"b{i}",f"{{{{PILLAR_{i+1}_BODY}}}}",cx-100,370,200,220,size=13,anchor="middle",idx=20+i))
    p.append(page()); return finish(p)

def build_r2_20():
    p=[open_svg("design_criteria_cards","Design Criteria Cards"),bg(),logo(),title()]
    cw,gap=180,20
    for i in range(6):
        x=40+i*(cw+gap); cx=x+cw/2
        p.append(circle(f"c{i}",cx,160,28,C["bk"]))
        p.append(rect(f"ig{i}",cx-12,148,24,24,C["gy"]))
        p.append(slot(f"h{i}",f"{{{{CRITERIA_{i+1}_TITLE}}}}",x,210,cw,40,size=14,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(rect(f"card{i}",x,260,cw,340,C["gw"]))
        p.append(bullets(f"c{i}",3,x+8,280,cw-16,f"{{{{CRITERIA_{i+1}_ITEM_{{i}}}}}}",line_h=90,size=12,idx0=20+i*5))
    p.append(page()); return finish(p)

def build_r2_21():
    p=[open_svg("three_core_principles","Three Core Principles"),bg(),logo(),title()]
    p.append(rect("well",40,130,1200,500,C["gw"]))
    p.append(line("d1",440,160,440,600,C["gl"],1))
    p.append(line("d2",840,160,840,600,C["gl"],1))
    for i in range(3):
        x=80+i*400
        p.append(circle(f"n{i}",x+40,220,32,C["bl"]))
        p.append(static_text(f"nt{i}",x+40,230,str(i+1),C["wh"],22,"700","middle"))
        p.append(slot(f"h{i}",f"{{{{PRINCIPLE_{i+1}_TITLE}}}}",x,280,320,50,size=18,weight="700",idx=i+1,ph="subtitle"))
        p.append(slot(f"b{i}",f"{{{{PRINCIPLE_{i+1}_BODY}}}}",x,350,320,200,size=15,idx=10+i))
    p.append(page()); return finish(p)

def build_r2_22():
    p=[open_svg("four_step_guiding","Four Step Guiding Principles"),bg(),logo(),title()]
    sw,gap=210,10
    for i in range(4):
        x=40+i*(sw+gap)
        p.append(poly(f"ch{i}",chev(x,130,sw,48,18),C["bk"]))
        p.append(slot(f"cht{i}",f"{{{{STEP_{i+1}_TITLE}}}}",x+20,130,sw-40,48,fill=C["wh"],size=13,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(slot(f"wk{i}",f"{{{{STEP_{i+1}_WEEKS}}}}",x,185,sw,24,fill=C["gt"],size=11,anchor="middle",idx=50+i))
        p.append(line(f"tl{i}",x+10,215,x+sw-10,215,C["bk"],1))
        if i<3: p.append(line(f"vd{i}",x+sw+gap/2,240,x+sw+gap/2,600,C["gd"],1,"3 4"))
        p.append(bullets(f"a{i}",3,x+8,250,sw-16,f"{{{{STEP_{i+1}_ACTION_{{i}}}}}}",line_h=40,size=12,idx0=20+i*10))
        p.append(line(f"sep{i}",x+10,380,x+sw-10,380,C["gl"],1))
        p.append(bullets(f"d{i}",3,x+8,400,sw-16,f"{{{{STEP_{i+1}_DELIVERABLE_{{i}}}}}}",line_h=50,size=12,idx0=60+i*10))
    sx=980
    p.append(rect("gph",sx,130,260,44,C["bl"]))
    p.append(slot("gpht","{{GUIDING_HEADER}}",sx,130,260,44,fill=C["wh"],size=14,weight="700",anchor="middle",idx=5,ph="subtitle"))
    p.append(rect("gpb",sx,174,260,450,C["gw"]))
    for i in range(4):
        y=190+i*105
        if i>0: p.append(line(f"gpl{i}",sx+10,y-10,sx+250,y-10,C["gl"],1))
        p.append(rect(f"gpi{i}",sx+16,y,36,36,C["gy"]))
        p.append(slot(f"gpt{i}",f"{{{{PRINCIPLE_{i+1}}}}}",sx+60,y,180,70,size=12,idx=80+i))
    p.append(source()); p.append(page()); return finish(p)

def build_r2_23():
    p=[open_svg("four_step_timeline","Four Step Timeline"),bg(),logo(),title()]
    p.append(line("tl",80,180,1200,180,C["gl"],2))
    for i in range(4):
        cx=160+i*300
        p.append(circle(f"n{i}",cx,180,12,C["bl"]))
        p.append(slot(f"ph{i}",f"{{{{PHASE_{i+1}_TITLE}}}}",cx-120,210,240,36,size=16,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        if i<3: p.append(line(f"vd{i}",cx+140,250,cx+140,640,C["gd"],1,"3 4"))
        p.append(slot(f"al{i}","Key activities",cx-120,260,240,24,fill=C["gt"],size=12,weight="700",anchor="middle",idx=90+i))
        p.append(bullets(f"a{i}",3,cx-110,300,220,f"{{{{PHASE_{i+1}_ACTION_{{i}}}}}}",line_h=40,size=12,idx0=20+i*10))
        p.append(slot(f"dl{i}","Main deliverables",cx-120,440,240,24,fill=C["gt"],size=12,weight="700",anchor="middle",idx=95+i))
        p.append(bullets(f"d{i}",3,cx-110,480,220,f"{{{{PHASE_{i+1}_DELIVERABLE_{{i}}}}}}",line_h=40,size=12,idx0=60+i*10))
    p.append(page()); return finish(p)

def build_r2_24():
    p=[open_svg("three_deliverables","Three Deliverables"),bg(),logo(),title()]
    for i in range(3):
        cx=213+i*400
        p.append(circle(f"c{i}",cx,220,48,C["bk"]))
        p.append(rect(f"ig{i}",cx-18,202,36,36,C["gy"]))
        p.append(line(f"dl{i}",cx,268,cx,340,C["gl"],1.5))
        p.append(slot(f"h{i}",f"{{{{DELIVERABLE_{i+1}_TITLE}}}}",cx-150,360,300,50,size=18,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(slot(f"b{i}",f"{{{{DELIVERABLE_{i+1}_BODY}}}}",cx-150,430,300,160,size=14,anchor="middle",idx=10+i))
    p.append(page()); return finish(p)

def build_r2_25():
    p=[open_svg("milestones_roadmap","Milestones Roadmap"),bg(),logo(),title(w=1000)]
    p.append(slot("sub","{{SUBTITLE}}",40,100,600,30,size=16,weight="700",idx=1,ph="subtitle"))
    p.append(slot("note","{{NOTE}}",900,100,240,30,fill=C["gt"],size=11,anchor="end",idx=2))
    colors=[C["bl"],C["nv"],C["bm"],C["bk"]]; px=[280,520,760,1000]
    for i,(cx,col) in enumerate(zip(px,colors)):
        p.append(slot(f"pt{i}",f"{{{{PHASE_{i+1}_TIMEFRAME}}}}",cx-100,140,200,24,fill=C["gt"],size=11,anchor="middle",idx=10+i))
        p.append(slot(f"ph{i}",f"{{{{PHASE_{i+1}_TITLE}}}}",cx-100,165,200,36,fill=col,size=18,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        if i<3:
            p.append(poly(f"ar{i}",f"{cx+90},180 {cx+102},185 {cx+90},190",C["bk"]))
            p.append(line(f"al{i}",cx+80,185,px[i+1]-80,185,C["bk"],1.5))
    for a in range(3):
        y=230+a*140
        if a>0: p.append(line(f"rd{a}",40,y-10,1240,y-10,C["gd"],1,"3 4"))
        p.append(slot(f"area{a}",f"{{{{AREA_{a+1}_LABEL}}}}",40,y,180,100,size=13,weight="700",idx=20+a))
        for ph in range(4):
            p.append(slot(f"m{ph}{a}",f"{{{{MILESTONES_P{ph+1}_A{a+1}}}}}",px[ph]-100,y,200,110,size=13,idx=30+ph*5+a))
    p.append(source()); p.append(page()); return finish(p)

def build_r2_26():
    p=[open_svg("scope_tree","Scope Tree"),bg(),logo(),title()]
    p.append(rect("root",440,130,400,56,C["bl"],rx=4))
    p.append(slot("roott","{{ROOT}}",440,130,400,56,fill=C["wh"],size=18,weight="700",anchor="middle",idx=1,ph="subtitle"))
    p.append(line("v1",640,186,640,230,C["gl"],1.5))
    p.append(line("h1",200,230,1080,230,C["gl"],1.5))
    for i in range(3):
        x=80+i*220
        p.append(line(f"vi{i}",x+90,230,x+90,260,C["gl"],1.5))
        p.append(rect(f"in{i}",x,260,180,50,C["bk"]))
        p.append(slot(f"int{i}",f"{{{{IN_SCOPE_{i+1}}}}}",x,260,180,50,fill=C["wh"],size=13,weight="700",anchor="middle",idx=10+i))
        for j in range(2):
            p.append(rect(f"inc{i}{j}",x+10,340+j*70,160,50,C["gw"]))
            p.append(slot(f"inct{i}{j}",f"{{{{IN_SCOPE_{i+1}_CHILD_{j+1}}}}}",x+10,340+j*70,160,50,size=12,anchor="middle",idx=20+i*5+j))
    for i in range(2):
        x=780+i*220
        p.append(line(f"vo{i}",x+90,230,x+90,260,C["gl"],1.5))
        p.append(rect(f"out{i}",x,260,180,50,C["gd"]))
        p.append(slot(f"outt{i}",f"{{{{OUT_SCOPE_{i+1}}}}}",x,260,180,50,fill=C["wh"],size=13,weight="700",anchor="middle",idx=40+i))
    p.append(rect("l1",1000,620,20,14,C["bk"]))
    p.append(slot("lt1","{{LEGEND_IN}}",1028,615,100,24,size=11,idx=90))
    p.append(rect("l2",1140,620,20,14,C["gd"]))
    p.append(slot("lt2","{{LEGEND_OUT}}",1168,615,70,24,size=11,idx=91))
    p.append(page()); return finish(p)


def build_r2_27():
    p=[open_svg("project_chevrons","Project Chevrons"),bg(),logo(),title()]
    fills=[C["bl"],C["bm"],C["ba"],C["nv"],C["bk"]]; cw=220
    for i in range(5):
        x=40+i*(cw+8)
        p.append(poly(f"ch{i}",chev(x,130,cw,52,18),fills[i]))
        p.append(slot(f"cht{i}",f"{{{{PHASE_{i+1}_TITLE}}}}",x+18,130,cw-36,52,fill=C["wh"],size=13,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        for row,lab in enumerate(["PURPOSE","ACTIVITIES","MILESTONES"]):
            y=220+row*140
            if i==0: p.append(slot(f"rl{row}",lab,40,y-30,200,24,fill=C["gt"],size=11,weight="700",idx=90+row))
            p.append(bullets(f"p{i}r{row}",2,x+8,y,cw-20,f"{{{{PHASE_{i+1}_R{row+1}_ITEM_{{i}}}}}}",line_h=40,size=12,idx0=20+i*20+row*5))
    p.append(page()); return finish(p)

def build_r2_28():
    p=[open_svg("six_week_plan","Six Week Plan"),bg(),logo(),title()]
    for i in range(6):
        x=200+i*130
        p.append(rect(f"w{i}",x,130,120,36,C["nv"]))
        p.append(slot(f"wt{i}",f"{{{{WEEK_{i+1}}}}}",x,130,120,36,fill=C["wh"],size=12,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
    for r in range(4):
        y=190+r*90
        p.append(slot(f"al{r}",f"{{{{ACTIVITY_{r+1}_LABEL}}}}",40,y+10,150,50,size=12,weight="700",idx=10+r))
        x=200+(r%3)*130; w=min(240+(r%2)*130, 980-x)
        p.append(poly(f"ab{r}",chev(x,y+10,w,40,14),C["bm"]))
        p.append(slot(f"at{r}",f"{{{{ACTIVITY_{r+1}}}}}",x+10,y+10,min(w,200)-20,40,fill=C["wh"],size=12,idx=20+r))
        p.append(poly(f"ws{r}",f"{x+60},{y-2} {x+70},{y+10} {x+60},{y+22}",C["yl"]))
    p.append(rect("com",1000,130,240,500,C["gw"]))
    p.append(slot("comh","{{COMMENTS_HEADER}}",1000,140,240,30,size=13,weight="700",anchor="middle",idx=5))
    p.append(slot("comt","{{COMMENTS}}",1015,190,210,400,size=12,idx=50))
    p.append(page()); return finish(p)

def build_r2_29():
    p=[open_svg("gantt_chart","Gantt Chart"),bg(),logo(),title()]
    p.append(rect("wh",200,120,1040,40,C["bk"]))
    for i in range(8):
        x=200+i*130
        p.append(slot(f"w{i}",f"{{{{WEEK_{i+1}}}}}",x,120,130,40,fill=C["wh"],size=11,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(line(f"vg{i}",x,160,x,640,C["gl"],0.5))
    for r in range(5):
        y=180+r*90
        p.append(rect(f"ph{r}",40,y,150,70,C["bk"]))
        p.append(slot(f"pht{r}",f"{{{{PHASE_{r+1}}}}}",40,y,150,70,fill=C["wh"],size=12,weight="700",anchor="middle",idx=20+r))
        bx=200+(r%4)*130; bw=200+(r%3)*100
        p.append(rect(f"bar{r}",bx,y+15,bw,40,C["bm"]))
        p.append(slot(f"bart{r}",f"{{{{BAR_{r+1}}}}}",bx+8,y+15,min(bw-16,180),40,fill=C["wh"],size=11,idx=40+r))
        mx=bx+bw
        p.append(poly(f"ms{r}",f"{mx},{y+25} {mx+10},{y+35} {mx},{y+45} {mx-10},{y+35}",C["yl"]))
    p.append(page()); return finish(p)

def build_r2_30():
    p=[open_svg("three_major_phases","Three Major Phases"),bg(),logo(),title()]
    p.append(slot("sub","{{SUBTITLE}}",40,100,600,28,size=14,weight="700",idx=1,ph="subtitle"))
    fills=[C["bl"],C["bm"],C["bk"]]; cw=380
    for i in range(3):
        x=40+i*(cw+20)
        p.append(poly(f"ch{i}",chev(x,150,cw,52,20),fills[i]))
        p.append(slot(f"cht{i}",f"{{{{PHASE_{i+1}_TITLE}}}}",x+20,150,cw-40,52,fill=C["wh"],size=16,weight="700",anchor="middle",idx=i+2,ph="subtitle"))
        if i<2: p.append(line(f"vd{i}",x+cw+10,230,x+cw+10,620,C["gl"],1))
        p.append(slot(f"dl{i}","Deliverables",x+20,230,cw-40,24,fill=C["gt"],size=12,weight="700",idx=50+i))
        p.append(bullets(f"d{i}",3,x+16,270,cw-40,f"{{{{PHASE_{i+1}_DELIVERABLE_{{i}}}}}}",line_h=50,size=13,idx0=20+i*10))
        p.append(slot(f"pl{i}","People",x+20,440,cw-40,24,fill=C["gt"],size=12,weight="700",idx=60+i))
        p.append(bullets(f"p{i}",2,x+16,480,cw-40,f"{{{{PHASE_{i+1}_PEOPLE_{{i}}}}}}",line_h=50,size=13,idx0=70+i*5))
    p.append(page()); return finish(p)

def build_r2_31():
    p=[open_svg("high_level_timeline","High Level Timeline"),bg(),logo(),title()]
    p.append(rect("wh",200,120,1040,40,C["nv"]))
    for i in range(10):
        x=200+i*104
        p.append(slot(f"w{i}",f"{{{{WEEK_{i+1}}}}}",x,120,104,40,fill=C["wh"],size=10,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(line(f"vg{i}",x,160,x,640,C["gd"],0.75,"2 4"))
    for r in range(5):
        y=180+r*90
        p.append(slot(f"ws{r}",f"{{{{WORKSTREAM_{r+1}}}}}",40,y+15,150,50,size=12,weight="700",idx=20+r))
        bx=200+(r%5)*104; bw=min(250+(r%3)*80, 1240-bx)
        p.append(rect(f"bar{r}",bx,y+15,bw,40,C["bm"]))
        p.append(circle(f"ms{r}",bx+40,y+10,6,C["yl"]))
    p.append(page()); return finish(p)

def build_r2_32():
    p=[open_svg("phase_three_steps","Phase Three Steps"),bg(),logo(),title()]
    for i in range(3):
        x=80+i*400
        p.append(static_text(f"n{i}",x,220,f"{i+1:02d}",C["bl"],72,"300"))
        p.append(slot(f"s{i}",f"{{{{STEP_{i+1}_TITLE}}}}",x,250,340,50,size=20,weight="700",idx=i+1,ph="subtitle"))
        if i<2: p.append(line(f"vd{i}",x+360,160,x+360,340,C["gl"],1))
    p.append(rect("band",40,360,1200,280,C["gw"]))
    for i in range(3):
        x=80+i*400
        p.append(bullets(f"s{i}",3,x,400,320,f"{{{{STEP_{i+1}_ITEM_{{i}}}}}}",line_h=60,size=14,idx0=20+i*10))
    p.append(page()); return finish(p)

def build_r2_33():
    p=[open_svg("six_workstreams_org","Six Workstreams Org"),bg(),logo(),title()]
    p.append(rect("st",440,120,400,48,C["bk"]))
    p.append(slot("stt","{{STEERCO}}",440,120,400,48,fill=C["wh"],size=16,weight="700",anchor="middle",idx=1,ph="subtitle"))
    p.append(line("v1",640,168,640,200,C["gl"],1.5))
    p.append(rect("pm",480,200,320,40,C["bm"]))
    p.append(slot("pmt","{{PROJECT_MGMT}}",480,200,320,40,fill=C["wh"],size=14,weight="700",anchor="middle",idx=2,ph="subtitle"))
    p.append(line("v2",640,240,640,270,C["gl"],1.5))
    p.append(line("h1",120,270,1160,270,C["gl"],1.5))
    for i in range(6):
        x=40+i*205
        p.append(line(f"vt{i}",x+90,270,x+90,290,C["gl"],1.5))
        p.append(rect(f"tr{i}",x,290,190,40,C["nv"]))
        p.append(slot(f"trt{i}",f"{{{{TRACK_{i+1}_TITLE}}}}",x,290,190,40,fill=C["wh"],size=12,weight="700",anchor="middle",idx=10+i))
        p.append(rect(f"trb{i}",x,330,190,280,C["gw"]))
        p.append(bullets(f"t{i}",4,x+6,350,170,f"{{{{TRACK_{i+1}_ITEM_{{i}}}}}}",line_h=55,size=11,idx0=30+i*10))
    p.append(page()); return finish(p)

def build_r2_34():
    p=[open_svg("risks_table","Risks Table"),bg(),logo(),title()]
    p.append(slot("ctx","{{CONTEXT_LABEL}}",1050,95,190,24,fill=C["gt"],size=12,anchor="end",idx=1))
    p.append(rect("h1",40,140,480,40,C["bk"]))
    p.append(slot("h1t","{{COL_RISK}}",50,140,460,40,fill=C["wh"],size=16,weight="700",idx=2,ph="subtitle"))
    p.append(rect("h2",540,140,520,40,C["bk"]))
    p.append(slot("h2t","{{COL_MITIGATION}}",550,140,500,40,fill=C["wh"],size=16,weight="700",idx=3,ph="subtitle"))
    p.append(rect("h3",1080,140,160,40,C["bk"]))
    p.append(slot("h3t","{{COL_LEVEL}}",1080,140,160,40,fill=C["wh"],size=16,weight="700",anchor="middle",idx=4,ph="subtitle"))
    rcols=[C["yl"],C["rd"],C["yl"],C["yl"],C["rd"]]
    for r in range(5):
        y=200+r*85
        if r>0: p.append(line(f"rd{r}",40,y-10,1240,y-10,C["gd"],1,"4 4"))
        p.append(slot(f"risk{r}",f"{{{{RISK_{r+1:02d}}}}}",50,y,430,60,size=14,idx=10+r))
        p.append(poly(f"ar{r}",f"500,{y+10} 518,{y+22} 500,{y+34}",C["bl"]))
        p.append(slot(f"mit{r}",f"{{{{MITIGATION_{r+1:02d}}}}}",550,y,500,60,size=14,idx=30+r))
        p.append(line(f"vl{r}",1070,y-5,1070,y+65,C["gl"],1))
        p.append(circle(f"lv{r}",1160,y+22,14,rcols[r]))
    p.append(source("{{FOOTNOTE}}")); p.append(page()); return finish(p)

def build_r2_35():
    p=[open_svg("risks_matrix","Risks Matrix"),bg(),logo(),title()]
    for i in range(5):
        y=140+i*95
        p.append(rect(f"rn{i}",40,y,420,70,C["bk"]))
        p.append(slot(f"rnt{i}",f"{{{{RISK_{i+1}_NAME}}}}",55,y+10,340,50,fill=C["wh"],size=14,weight="700",idx=10+i))
        p.append(circle(f"lc{i}",490,y+35,18,C["bl"]))
        p.append(static_text(f"lt{i}",490,y+41,chr(ord("A")+i),C["wh"],14,"700","middle"))
        if i<4: p.append(line(f"rd{i}",40,y+80,540,y+80,C["gd"],1,"4 4"))
    p.append(rect("mx",600,140,640,500,C["wh"],stroke=C["gl"]))
    p.append(slot("axy","{{AXIS_Y}}",610,150,200,24,fill=C["gt"],size=11,idx=50))
    p.append(slot("axx","{{AXIS_X}}",1000,610,200,24,fill=C["gt"],size=11,anchor="end",idx=51))
    for g in range(1,4):
        p.append(line(f"vg{g}",600+g*160,140,600+g*160,640,C["gy"],1))
        p.append(line(f"hg{g}",600,140+g*125,1240,140+g*125,C["gy"],1))
    for i,(px,py) in enumerate([(720,500),(880,350),(1040,280),(760,220),(1100,450)]):
        p.append(circle(f"d{i}",px,py,16,C["bl"]))
        p.append(static_text(f"dt{i}",px,py+5,chr(ord("A")+i),C["wh"],12,"700","middle"))
    p.append(page()); return finish(p)

def build_r2_36():
    p=[open_svg("capability_matrix","Capability Matrix"),bg(),logo(),title()]
    p.append(rect("hdr",40,130,1200,44,C["nv"]))
    cw=200
    for i in range(6):
        p.append(slot(f"ch{i}",f"{{{{COL_{i+1}}}}}",40+i*cw,130,cw,44,fill=C["wh"],size=13,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
    for r in range(6):
        y=190+r*70; fill=C["gw"] if r%2==0 else C["wh"]
        p.append(rect(f"row{r}",40,y,1200,70,fill))
        p.append(slot(f"rl{r}",f"{{{{ROW_{r+1}_LABEL}}}}",50,y+15,180,40,size=13,weight="700",idx=20+r))
        for c in range(1,6):
            if (r+c)%3!=0:
                p.append(circle(f"d{r}{c}",40+c*cw+cw/2,y+35,8,C["bl"]))
    p.append(page()); return finish(p)

def build_r2_37():
    p=[open_svg("reference_cases","Reference Cases"),bg(),logo(),title()]
    for i in range(4):
        x=40+i*310
        p.append(rect(f"ph{i}",x,130,290,220,C["gy"]))
        p.append(slot(f"img{i}","{{IMAGE}}",x,220,290,30,fill=C["gt"],size=12,anchor="middle",idx=50+i,ph="object"))
        p.append(rect(f"ct{i}",x,350,290,48,C["bk"]))
        p.append(slot(f"ctt{i}",f"{{{{CASE_{i+1}_TITLE}}}}",x+10,350,270,48,fill=C["wh"],size=14,weight="700",idx=i+1,ph="subtitle"))
        p.append(rect(f"cd{i}",x,398,290,220,C["gw"]))
        p.append(slot(f"cdt{i}",f"{{{{CASE_{i+1}_DESC}}}}",x+12,420,266,180,size=13,idx=20+i))
    p.append(page()); return finish(p)

def build_r2_38():
    p=[open_svg("marketplace_cards","Marketplace Cards"),bg(),logo(),title()]
    p.append(line("nl",100,280,1180,280,C["bl"],2))
    for i in range(6):
        x=40+i*205; cx=x+90
        p.append(circle(f"nd{i}",cx,280,10,C["bl"]))
        p.append(rect(f"card{i}",x,140,190,110,C["bk"],rx=8))
        p.append(rect(f"ig{i}",cx-16,155,32,32,C["gy"]))
        p.append(slot(f"ct{i}",f"{{{{CARD_{i+1}_TITLE}}}}",x+8,200,174,40,fill=C["wh"],size=13,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
        p.append(slot(f"cd{i}",f"{{{{CARD_{i+1}_DESC}}}}",x,320,190,280,size=13,anchor="middle",idx=20+i))
    p.append(page()); return finish(p)

def build_r2_39():
    p=[open_svg("program_overview","Program Overview"),bg(),logo(),title()]
    fills=[C["bl"],C["bm"],C["ba"],C["nv"],"#003D8F",C["bk"]]; cw=190
    for i in range(6):
        x=40+i*(cw+12)
        p.append(poly(f"ch{i}",chev(x,130,cw,48,16),fills[i]))
        p.append(slot(f"cht{i}",f"{{{{PHASE_{i+1}_TITLE}}}}",x+16,130,cw-32,48,fill=C["wh"],size=12,weight="700",anchor="middle",idx=i+1,ph="subtitle"))
    p.append(slot("ceh","{{CORE_ELEMENTS_HEADER}}",40,220,400,30,size=16,weight="700",idx=10,ph="subtitle"))
    for i in range(4):
        x=40+i*310
        p.append(circle(f"n{i}",x+24,290,20,C["bk"]))
        p.append(static_text(f"nt{i}",x+24,296,str(i+1),C["wh"],14,"700","middle"))
        p.append(slot(f"cet{i}",f"{{{{CORE_{i+1}_TITLE}}}}",x+55,270,230,40,size=14,weight="700",idx=20+i))
        p.append(bullets(f"ce{i}",3,x+8,340,280,f"{{{{CORE_{i+1}_ITEM_{{i}}}}}}",line_h=70,size=13,idx0=40+i*10))
    p.append(page()); return finish(p)

def build_r2_40():
    grad=(
      '  <defs>\n'
      f'    <linearGradient id="section-grad" x1="0%" y1="0%" x2="100%" y2="100%">\n'
      f'      <stop offset="0%" stop-color="{C["bl"]}"/>\n'
      f'      <stop offset="45%" stop-color="{C["bm"]}"/>\n'
      f'      <stop offset="100%" stop-color="{C["nv"]}"/>\n'
      '    </linearGradient>\n'
      '  </defs>\n'
      '  <rect id="master-bg" x="0" y="0" width="1280" height="720" fill="url(#section-grad)"\n'
      '    data-pptx-layer="master" data-pptx-editable="false"/>\n'
      '  <path id="ribbon-1" d="M-40,520 C200,400 400,600 640,480 C880,360 1100,520 1320,400"\n'
      '    fill="none" stroke="#003D8F" stroke-width="48" opacity="0.35"\n'
      '    data-pptx-layer="layout" data-pptx-editable="false"/>\n'
      '  <path id="ribbon-2" d="M-40,580 C240,460 480,640 720,520 C960,400 1160,560 1320,480"\n'
      '    fill="none" stroke="#001A40" stroke-width="64" opacity="0.4"\n'
      '    data-pptx-layer="layout" data-pptx-editable="false"/>\n'
    )
    p=[open_svg("section_agenda","Section Agenda"),grad,logo(dark=True)]
    items=[("{{SECTION_01}}",C["wh"],"700"),("{{SECTION_02}}","#B0B8C4","300"),
           ("{{SECTION_03}}","#B0B8C4","300"),("{{SECTION_04}}","#B0B8C4","300")]
    for i,(tok,fill,weight) in enumerate(items):
        y=220+i*80
        p.append(slot(f"sec{i}",tok,480,y,760,60,fill=fill,size=47,weight=weight,anchor="end",idx=i+1,ph="title" if i==0 else "body"))
    return finish(p)

def build_r2_41():
    p=[open_svg("overview_prose","Overview Prose"),bg(),logo(),title()]
    for i in range(4):
        p.append(slot(f"p{i}",f"{{{{PARAGRAPH_{i+1}}}}}",40,140+i*110,1200,90,size=18,idx=10+i))
    p.append(page()); return finish(p)


ROSTER = [
    (1,"r2_02","objectives_two_column",build_r2_02),
    (2,"r2_03","content_vs_structure",build_r2_03),
    (3,"r2_04","from_to_compare",build_r2_04),
    (4,"r2_05","short_relevant_actionable",build_r2_05),
    (5,"r2_06","scr_bc_framework",build_r2_06),
    (6,"r2_07","scr_proposal_flow",build_r2_07),
    (7,"r2_08","scr_tips_situation",build_r2_08),
    (8,"r2_09","executive_summary",build_r2_09),
    (9,"r2_10","summary_proposal",build_r2_10),
    (10,"r2_11","client_purpose_circles",build_r2_11),
    (11,"r2_12","content_toc",build_r2_12),
    (12,"r2_13","industry_inflection_photo",build_r2_13),
    (13,"r2_14","background_purpose_timeline",build_r2_14),
    (14,"r2_15","time_to_act_pillars",build_r2_15),
    (15,"r2_16","solution_pillars",build_r2_16),
    (16,"r2_17","solution_gallery",build_r2_17),
    (17,"r2_18","business_case_blocks",build_r2_18),
    (18,"r2_19","strategy_process_pillars",build_r2_19),
    (19,"r2_20","design_criteria_cards",build_r2_20),
    (20,"r2_21","three_core_principles",build_r2_21),
    (21,"r2_22","four_step_guiding",build_r2_22),
    (22,"r2_23","four_step_timeline",build_r2_23),
    (23,"r2_24","three_deliverables",build_r2_24),
    (24,"r2_25","milestones_roadmap",build_r2_25),
    (25,"r2_26","scope_tree",build_r2_26),
    (26,"r2_27","project_chevrons",build_r2_27),
    (27,"r2_28","six_week_plan",build_r2_28),
    (28,"r2_29","sixteen_week_gantt",build_r2_29),
    (29,"r2_30","three_major_phases",build_r2_30),
    (30,"r2_31","high_level_timeline",build_r2_31),
    (31,"r2_32","phase_three_steps",build_r2_32),
    (32,"r2_33","six_workstreams_org",build_r2_33),
    (33,"r2_34","risks_table",build_r2_34),
    (34,"r2_35","risks_matrix",build_r2_35),
    (35,"r2_36","capability_matrix",build_r2_36),
    (36,"r2_37","reference_cases",build_r2_37),
    (37,"r2_38","marketplace_cards",build_r2_38),
    (38,"r2_39","program_overview",build_r2_39),
    (39,"r2_40","section_agenda",build_r2_40),
    (40,"r2_41","overview_prose",build_r2_41),
]

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for num, rid, slug, builder in ROSTER:
        name = f"{num:02d}_{rid}_{slug}.svg"
        path = OUT / name
        svg = builder()
        path.write_text(svg, encoding="utf-8")
        print(f"wrote {name} ({len(svg.encode())} bytes)")
    print(f"TOTAL {len(ROSTER)} SVGs")

if __name__ == "__main__":
    main()
