import svgwrite

def cover_plate(size, corner_radius):
    dwg = svgwrite.Drawing('cover.svg', profile='tiny', size=("150mm", "150mm"), viewBox=(0, 0, 150, 150))
    border = (150 - size)/2
    dwg.add(dwg.rect((border, border),
                     (size, size),
                     rx = corner_radius,
                     ry = corner_radius,
                     stroke="red",
                     stroke_width="0.01mm",
                     fill="none"))
    dwg.save()

cover_plate(112, 5 * 1.6)
