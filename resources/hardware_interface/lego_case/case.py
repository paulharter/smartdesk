import svgwrite

def case(width, height):

    drawing_width = 180
    drawing_height = 160

    dwg = svgwrite.Drawing('case.svg',
                           profile='tiny',
                           size=("%smm" % drawing_width, "%smm" % drawing_height),
                           viewBox=(0, 0, drawing_width, drawing_height))
    flu = 1.6
    lego_width = 5 * flu * width
    lego_height = 5 * flu * height
    corner_radius = 0.5
    left = (drawing_width - lego_width) / 2
    top = (drawing_height - lego_height) / 2
    dwg.add(dwg.rect((left, top),
                     (lego_width, lego_height),
                     rx = corner_radius,
                     ry = corner_radius,
                     stroke="blue",
                     stroke_width="0.01mm",
                     fill="none"))


    case_height = 100
    case_width = 140

    left = (drawing_width - case_width) / 2
    top = (drawing_height - case_height) / 2

    corner_radius = 5 * flu

    dwg.add(dwg.rect((left, top),
                     (case_width, case_height),
                     rx = corner_radius,
                     ry = corner_radius,
                     stroke="red",
                     stroke_width="0.01mm",
                     fill="none"))

    holes_height = 75
    holes_width = 75

    hole_radius = 2.25

    x = (drawing_width - holes_width) / 2
    y =  (drawing_height - holes_height) / 2

    dwg.add(dwg.circle((x, y),
                     r = hole_radius,
                     stroke="red",
                     stroke_width="0.01mm",
                     fill="none"))

    dwg.add(dwg.circle((x, y + holes_height),
                     r = hole_radius,
                     stroke="red",
                     stroke_width="0.01mm",
                     fill="none"))

    dwg.add(dwg.circle((x + holes_width, y + holes_height),
                     r = hole_radius,
                     stroke="red",
                     stroke_width="0.01mm",
                     fill="none"))

    dwg.add(dwg.circle((x + holes_width, y),
                     r = hole_radius,
                     stroke="red",
                     stroke_width="0.01mm",
                     fill="none"))
    dwg.save()


case(12, 8)
