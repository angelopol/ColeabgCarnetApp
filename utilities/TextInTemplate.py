from PIL import Image, ImageDraw, ImageFont

base = Image.open(r'C:\Users\Angel\OneDrive\Escritorio\Notes\Proyecto Solvencia\CarnetApp\TemplateImages\CarnetTemplateX102.jpg').convert('RGBA')

txt = Image.new('RGBA', base.size, (255,255,255,0))

fnt = ImageFont.truetype('ariblk.ttf', 40)
fnt2 = ImageFont.truetype('arialbd.ttf', 25)
fnt3 = ImageFont.truetype('arialbd.ttf', 20)

d = ImageDraw.Draw(txt)

d.text((384,10), "COLEGIO DE ABOGADOS", font=fnt, fill=(0,0,0,255))
d.text((377,60), "DEL ESTADO CARABOBO", font=fnt, fill=(0,0,0,255))

d.text((684,150), "Emisión:", font=fnt2, fill=(0,0,0,255))

d.text((707,180), "Vence:", font=fnt2, fill=(0,0,0,255))
#d.text((801,180), "14-08-2023", font=fnt2, fill=(0,0,0,255))

d.text((140,250), "Apellidos:", font=fnt2, fill=(0,0,0,255))
d.text((140,310), "Nombres:", font=fnt2, fill=(0,0,0,255))
d.text((140,370), "C.I.:", font=fnt2, fill=(0,0,0,255))
d.text((140,430), "INPRE:", font=fnt2, fill=(0,0,0,255))
d.text((140,490), "F. de inscripción:", font=fnt2, fill=(0,0,0,255))
d.text((140,550), "N° de inscripción:", font=fnt2, fill=(0,0,0,255))

out = Image.alpha_composite(base, txt)

out.save(r"TemplateImages\AbgTemplate.png")