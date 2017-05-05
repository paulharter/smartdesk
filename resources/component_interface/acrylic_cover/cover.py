from dxfwrite import DXFEngine as dxf



def cover_plate(size, corner_radius):

    drawing = dxf.drawing('output/cover.dxf')

    line = dxf.line((corner_radius, 0), (size - corner_radius, 0), color=1, thickness=0.01)
    line["thickness"] = 0.001
    drawing.add(line)

    drawing.add(dxf.line((size, 0 + corner_radius), (size, size - corner_radius), color=1, thickness=0.01))

    drawing.add(dxf.line((size - corner_radius, size), (0 + corner_radius, size), color=1, thickness=0.01))

    drawing.add(dxf.line((0, size - corner_radius), (0, 0 + corner_radius), color=1, thickness=0.01))

    drawing.save()


cover_plate(10, 0.5)
