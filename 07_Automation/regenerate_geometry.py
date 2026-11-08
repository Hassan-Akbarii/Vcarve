#!/usr/bin/env python3
"""Original River practice geometry. Python 3 standard library only.

Creates editable DXF/SVG and a dimensional manifest, not VCarve CAM or G-code.
Default output is a NEW Generated_Variant folder beside this script's folder.
"""
import argparse
import csv
import json
import math
from pathlib import Path
from xml.sax.saxutils import escape

COLORS = ['#e8cc9a', '#69452f', '#edd5a8', '#69452f', '#e8cc9a']

def bounds(poly):
    return [min(p[0] for p in poly), min(p[1] for p in poly),
            max(p[0] for p in poly), max(p[1] for p in poly)]

def area(poly):
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1] -
                   poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly)))/2)

def bezier(c, t):
    return (1-t)**3*c[0] + 3*(1-t)**2*t*c[1] + 3*(1-t)*t*t*c[2] + t**3*c[3]

def make_boundary_fn(p):
    w, h = p['finished_width_mm'], p['finished_height_mm']
    def f(i, y):
        if i == 0: return 0.0
        if i == 5: return w
        base = p['boundary_x_fractions'][i-1]*w
        a = [x*w/508.0 for x in p['bezier_x_offsets_at_508_mm'][i-1]]
        if y < 0: return base + a[0] + (a[1]-a[0])*6/h*y
        if y > h: return base + a[6] + (a[6]-a[5])*6/h*(y-h)
        if y <= h/2: return base + bezier(a[:4], 2*y/h)
        return base + bezier(a[3:], 2*y/h-1)
    return f

def make_parts(p, pretrim=False):
    w,h=p['finished_width_mm'],p['finished_height_mm']
    t=p['perimeter_trim_mm'] if pretrim else 0.0
    f=make_boundary_fn(p)
    n=math.ceil(h/p['curve_sample_step_mm'])
    ys=[i*h/n for i in range(n+1)]
    if t: ys=[-t]+ys+[h+t]
    polys=[]
    for i in range(5):
        left=[(-t if i==0 else f(i,y),y) for y in ys]
        right=[(w+t if i==4 else f(i+1,y),y) for y in reversed(ys)]
        polys.append(left+right)
    return polys

def dxf(path, entries):
    """Write simple R2000 DXF in mm with individually editable closed polylines."""
    layers=sorted(set(x[0] for x in entries))
    lines=[]
    def add(*xs): lines.extend(str(x) for x in xs)
    add(0,'SECTION',2,'HEADER',9,'$ACADVER',1,'AC1015',9,'$INSUNITS',70,4,
        9,'$MEASUREMENT',70,1,0,'ENDSEC',0,'SECTION',2,'TABLES',0,'TABLE',2,'LAYER',5,'2',100,'AcDbSymbolTable',70,len(layers))
    for l in layers:
        color=8 if l.startswith('REF_') else 3
        add(0,'LAYER',100,'AcDbSymbolTableRecord',100,'AcDbLayerTableRecord',2,l,70,0,62,color,6,'CONTINUOUS')
    add(0,'ENDTAB',0,'ENDSEC',0,'SECTION',2,'ENTITIES')
    for layer, poly, closed in entries:
        add(0,'LWPOLYLINE',100,'AcDbEntity',8,layer,100,'AcDbPolyline',90,len(poly),70,1 if closed else 0)
        for x,y in poly: add(10,f'{x:.6f}',20,f'{y:.6f}')
    add(0,'ENDSEC',0,'EOF')
    Path(path).write_text('\n'.join(lines)+'\n',encoding='ascii')

def svg(path, entries, width, height, title):
    a=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.6f}mm" height="{height:.6f}mm" viewBox="0 0 {width:.6f} {height:.6f}">',
       '<title>'+escape(title)+'</title>',f'<g transform="translate(0 {height:.6f}) scale(1 -1)">']
    for j,(layer,poly,closed) in enumerate(entries):
        points=' '.join(f'{x:.6f},{y:.6f}' for x,y in poly)
        tag='polygon' if closed else 'polyline'
        fill='none' if layer.startswith('REF_') else COLORS[j%len(COLORS)]
        if layer.startswith('CUT_') and 'WALNUT' in layer: fill='#69452f'
        if layer.startswith('CUT_') and 'MAPLE' in layer: fill='#e8cc9a'
        dash=' stroke-dasharray="3 2"' if layer.startswith('REF_') else ''
        a.append(f'<{tag} id="{layer}" points="{points}" fill="{fill}" stroke="#333333" stroke-width="0.25"{dash}/>')
    a.extend(['</g>','</svg>'])
    Path(path).write_text('\n'.join(a),encoding='utf-8')

def stock_layout(poly, margin):
    b=bounds(poly)
    width=math.ceil((b[2]-b[0]+2*margin)/5)*5
    height=math.ceil((b[3]-b[1]+2*margin)/5)*5
    dx,dy=margin-b[0],margin-b[1]
    local=[(x+dx,y+dy) for x,y in poly]
    rect=[(0,0),(width,0),(width,height),(0,height)]
    return width,height,local,rect,[dx,dy]

def editable_bezier_svg(p,path):
    """An exact low-node master for easier curve edits; assembly reference only."""
    w,h=p['finished_width_mm'],p['finished_height_mm']
    controls=[]
    for frac,offsets in zip(p['boundary_x_fractions'],p['bezier_x_offsets_at_508_mm']):
        controls.append([(frac*w+dx*w/508,j*h/6) for j,dx in enumerate(offsets)])
    def pt(a):return f'{a[0]:.6f} {a[1]:.6f}'
    parts=[]
    for i in range(5):
        if i==0: start=(0,0);s='M '+pt(start)+' L '+pt((0,h))
        else:
            cc=controls[i-1];s='M '+pt(cc[0])+' C '+' '.join(pt(z) for z in cc[1:4])+' C '+' '.join(pt(z) for z in cc[4:7])
        if i==4:s+=' L '+pt((w,h))+' L '+pt((w,0))
        else:
            cc=controls[i];s+=' L '+pt(cc[6])+' C '+' '.join(pt(z) for z in [cc[5],cc[4],cc[3]])+' C '+' '.join(pt(z) for z in [cc[2],cc[1],cc[0]])
        s+=' Z'
        parts.append(f'<path id="P{i+1:02d}" d="{s}" fill="{COLORS[i]}" stroke="#333" stroke-width="0.25"/>')
    body=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}"><title>Editable exact Bezier master - nominal assembly reference</title><g transform="translate(0 {h}) scale(1 -1)">'+''.join(parts)+'</g></svg>\n'
    Path(path).write_text(body,encoding='utf-8')

def generate(p,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    if p['units']!='mm': raise ValueError('This generator requires millimetres.')
    if p.get('nominal_joint_gap_mm',0)!=0: raise ValueError('Keep nominal CAD gap zero; fit allowance belongs in CAM.')
    if len(p['materials'])!=5: raise ValueError('Exactly five pieces required.')
    w,h=p['finished_width_mm'],p['finished_height_mm']
    if min(w,h)<=0 or p['curve_sample_step_mm']<=0: raise ValueError('Positive dimensions required.')
    if not 0<=p['perimeter_trim_mm']<=10: raise ValueError('Practice trim must be 0 to 10 mm.')
    if p['planed_stock_thickness_mm']<p['finished_thickness_mm']: raise ValueError('Stock thinner than finish.')
    nominal,pre=make_parts(p),make_parts(p,True)
    bfn=make_boundary_fn(p)
    gaps=[min(bfn(i+1,j*h/2000)-bfn(i,j*h/2000) for j in range(2001)) for i in range(5)]
    if min(gaps)<10: raise ValueError('Parts intersect or are too narrow for this exercise.')
    entries=[(f'P{i+1:02d}_'+('MAPLE' if i%2==0 else 'WALNUT'),poly,True) for i,poly in enumerate(nominal)]
    dxf(out/'Master_Finished_Assembly_mm.dxf',entries)
    svg(out/'Master_Finished_Assembly_mm.svg',entries,w,h,'Finished nominal assembly - reference only')
    editable_bezier_svg(p,out/'Master_Editable_Bezier_Assembly_mm.svg')
    # Pretrim assembly is translated by +trim in XY to keep all coordinates positive.
    t=p['perimeter_trim_mm']
    preent=[(f'P{i+1:02d}',[(x+t,y+t) for x,y in po],True) for i,po in enumerate(pre)]
    dxf(out/'Master_Pretrim_Assembly_mm.dxf',preent)
    svg(out/'Master_Pretrim_Assembly_mm.svg',preent,w+2*t,h+2*t,'Pretrim assembly - reference only')
    rows=[]
    for i,po in enumerate(pre):
        name=f'P{i+1:02d}_'+('Maple' if i%2==0 else 'Walnut')
        sw,sh,local,rect,shift=stock_layout(po,p['stock_margin_mm'])
        ent=[('CUT_'+name.upper(),local,True),('REF_STOCK',rect,True),
             ('REF_GRAIN',[(sw-8,12),(sw-8,sh-12)],False)]
        dxf(out/(name+'_Stock_Layout_mm.dxf'),ent)
        svg(out/(name+'_Stock_Layout_mm.svg'),ent,sw,sh,name+' stock and part - select CUT layer only')
        b=bounds(po)
        rows.append({'part_id':f'P{i+1:02d}','material':p['materials'][i],
                     'stock_x_mm':sw,'stock_y_mm':sh,'stock_z_mm':p['planed_stock_thickness_mm'],
                     'part_bbox_x_mm':round(b[2]-b[0],4),'part_bbox_y_mm':round(b[3]-b[1],4),
                     'assembly_to_stock_shift_x_mm':round(shift[0],6),'assembly_to_stock_shift_y_mm':round(shift[1],6),
                     'min_piece_width_in_x_mm':round(gaps[i],4),'grain':'Positive Y',
                     'cut_layer':'CUT_'+name.upper()})
    with (out/'Stock_and_Parts.csv').open('w',newline='',encoding='utf-8') as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
    # Short pair uses an exact 120 mm segment of board interface J12, at full scale.
    cy0=h/2-60
    ys=[j*0.5 for j in range(241)]
    cv=[(80+bfn(1,cy0+y)-bfn(1,h/2),y) for y in ys]
    a=[(0,0),(0,120)]+list(reversed(cv))
    b=cv+[(160,120),(160,0)]
    coupon_rows=[]
    for name,po,mat in [('Coupon_A_Maple',a,'Hard maple'),('Coupon_B_Walnut',b,'Walnut')]:
        sw,sh,local,rect,shift=stock_layout(po,p['stock_margin_mm'])
        ent=[('CUT_'+name.upper(),local,True),('REF_STOCK',rect,True)]
        dxf(out/(name+'_Stock_mm.dxf'),ent)
        svg(out/(name+'_Stock_mm.svg'),ent,sw,sh,name+' - nominal joint')
        coupon_rows.append({'part':name,'material':mat,'stock_x_mm':sw,'stock_y_mm':sh,
                            'stock_z_mm':p['planed_stock_thickness_mm'],'assembly_to_stock_shift_xy':shift})
    svg(out/'Coupon_Assembly_mm.svg',[('MAPLE',a,True),('WALNUT',b,True)],160,120,'Coupon pair - reference only')
    dxf(out/'Coupon_Assembly_mm.dxf',[('COUPON_A',a,True),('COUPON_B',b,True)])
    # Easy warm-up: 100 x 60 plate with two 10 mm holes in a 140 x 100 stock.
    rect=[(20,20),(120,20),(120,80),(20,80)]
    holes=[[(cx+5*math.cos(2*math.pi*j/96),50+5*math.sin(2*math.pi*j/96)) for j in range(96)] for cx in [40,100]]
    plate=[('CUT_OUTER',rect,True)]+[('CUT_HOLE_'+str(i+1),po,True) for i,po in enumerate(holes)]
    plate+=[('REF_STOCK',[(0,0),(140,0),(140,100),(0,100)],True)]
    dxf(out/'Warmup_Plate_Stock_mm.dxf',plate)
    svg(out/'Warmup_Plate_Stock_mm.svg',plate,140,100,'Warmup plate - 12 mm simulation stock')
    target=w*h
    actual=sum(area(po) for po in nominal)
    pretarget=(w+2*t)*(h+2*t)
    manifest={'status':'GEOMETRY CHECKED; CAM NOT CREATED OR VALIDATED',
              'revision':p['revision'],'units':'mm','parameters':p,'stock_parts':rows,'coupons':coupon_rows,
              'checks':{'finished_bbox_mm':[w,h],'finished_area_sum_mm2':actual,
                        'finished_area_expected_mm2':target,'finished_area_error_mm2':actual-target,
                        'pretrim_area_sum_mm2':sum(area(po) for po in pre),'pretrim_area_expected_mm2':pretarget,
                        'minimum_piece_widths_in_x_mm':gaps,
                        'shared_edges':'Same sampled curve reused in both adjoining pieces',
                        'sample_interval_y_mm':h/math.ceil(h/p['curve_sample_step_mm']),
                        'chord_error_estimate_mm':0.002,'cam_validation':'Requires import and simulation in VCarve'}}
    (out/'geometry_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    return manifest

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--params',type=Path,default=Path(__file__).with_name('parameters.json'))
    parser.add_argument('--out',type=Path,default=Path(__file__).resolve().parent.parent/'Generated_Variant')
    args=parser.parse_args()
    p=json.loads(args.params.read_text(encoding='utf-8'))
    m=generate(p,args.out)
    print('Created geometry in',args.out.resolve())
    print('Area error mm2:',round(m['checks']['finished_area_error_mm2'],7))
    print('No CRV, toolpaths or machine code generated. Complete CAM in VCarve.')

if __name__=='__main__': main()
