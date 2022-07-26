"""
filename = "/Users/lessandro/Hacking/BLENDER/blender_spirals/script.py"
exec(compile(open(filename).read(), filename, 'exec'))
"""

from typing import Tuple

from bpy.types import GreasePencil, GPencilLayer, GPencilFrame, GPencilStroke
import bpy

import sys
import os
import bpy
blender_scripts_dir = "/Users/lessandro/Hacking/BLENDER/blender_spirals/geometry"
if blender_scripts_dir not in sys.path:
   sys.path.append(blender_scripts_dir)
blender_scripts_dir = "/Users/lessandro/Hacking/BLENDER/blender_spirals/music"
if blender_scripts_dir not in sys.path:
   sys.path.append(blender_scripts_dir)

import spiral
import importlib
importlib.reload(spiral)

import random
import math

# BLENDER

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


# AUDIO

import music.audio as Audio
audioSplits = Audio.rmsSplits("/Users/lessandro/Hacking/BLENDER/blender_spirals/music/24jul-listzforblender.wav", 25) # 25 fps

maxRMS = max(audioSplits)
minRMS = (sum(audioSplits) / len(audioSplits))


# CREATE SPIRAL

gp_dat, gp_obj = init_gp("TestPencil")

x, y, frames, frame_length = 1, 0, len(audioSplits), 1
gp_layer = create_gp_layer(gp_obj, "TestLayer" , True)
gp_frame = gp_layer.frames.new(0)
for frame_number in range(frames):
    gp_layer.frames.copy(gp_frame)
    gp_mat = create_gp_material("BlackLine", [0., 0., 0., 1.])
    gp_dat.materials.append(gp_mat)
    if frame_number % 100 == 0:
        bpy.context.scene.world.color = (random.random(), random.random(), random.random())
        bpy.ops.anim.keyframe_insert_button(all=True)



    rms = audioSplits[frame_number]
    rstep_base = 5
    tstep_base = 0.05
    music_multiplier = (rms / (maxRMS - minRMS)) 
    z, w = spiral.next_point(
            x, 
            y, 
            music_multiplier * (2 * rstep_base), 
            music_multiplier * (2 * tstep_base), 
    )
    gp_stroke = stroke_polyline(gp_frame, [[x, y, 0], [z, w, 0]], 10 * math.sqrt(frame_number))
    #print(x, y, z, w)
    x, y = z, w



print("Success!")
print("number of frames" + str(frames * frame_length))

