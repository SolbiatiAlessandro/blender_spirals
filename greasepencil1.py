"""
filename = "/Users/lessandro/Hacking/BLENDER/greasepencil1.py"
exec(compile(open(filename).read(), filename, 'exec'))
"""

from typing import Tuple

from bpy.types import GreasePencil, GPencilLayer, GPencilFrame, GPencilStroke
import bpy

import sys
import os
import bpy
blender_scripts_dir = "/Users/lessandro/Hacking/BLENDER/blender_spirals"
if blender_scripts_dir not in sys.path:
   sys.path.append(blender_scripts_dir)

import alexgeometry
import importlib
importlib.reload(alexgeometry)


def create_gp(gp_data: GreasePencil, name) -> GreasePencil:
    if name not in bpy.context.scene.objects:
        gp_obj = bpy.data.objects.new(name, gp_data)
        bpy.context.scene.objects[-1].name = name
        bpy.context.scene.collection.objects.link(gp_obj)

    return bpy.context.scene.objects.get(name)


def create_gp_layer(gp_obj, layer_name, clear_layer) -> GPencilLayer:
    # Get grease pencil layer or create one if none exists
    if layer_name in gp_obj.data.layers:
        gp_layer = gp_obj.data.layers.get(layer_name)
    else:
        gp_layer = gp_obj.data.layers.new(layer_name, set_active=True)

    if clear_layer:
        gp_layer.clear()

    return gp_layer


def init_gp(name) -> Tuple[GreasePencil, GreasePencil]:
    gp_data = bpy.data.grease_pencils.new(name)
    gp_obj = create_gp(gp_data, name)

    return gp_data, gp_obj


def stroke_polyline(gp_frame: GPencilFrame, vertices, line_width) -> GPencilStroke:
    gp_stroke = gp_frame.strokes.new()
    gp_stroke.points.add(len(vertices))

    for ix, vertex in enumerate(vertices):
        gp_stroke.points[ix].co = vertex

    gp_stroke.line_width = line_width
    return gp_stroke


def create_gp_material(name: str, color) -> bpy.types.Material:
    gp_mat = bpy.data.materials.new(name)
    bpy.data.materials.create_gpencil_data(gp_mat)
    gp_mat.grease_pencil.color = color

    return gp_mat


gp_dat, gp_obj = init_gp("TestPencil")

# a circle of 1 meter radius with 10 segments
x, y, r, n = 0, 1, 1, 30
gp_layer = create_gp_layer(gp_obj, "TestLayer" , True)
for segment in range(n):
    gp_frame = gp_layer.frames.new(segment * 3)
    gp_mat = create_gp_material("BlackLine", [0., 0., 0., 1.])
    gp_dat.materials.append(gp_mat)

    z, w = alexgeometry.next_point_on_a_circle(x, y, n, r)
    gp_stroke = stroke_polyline(gp_frame, [[x, y, 0], [z, w, 0]], 10)
    print(x, y, z, w)
    x, y = z, w



print("Success!")
