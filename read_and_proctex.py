__author__ = 'yicong'

import csv

import bpy
import bmesh

D = bpy.data
C = bpy.context
O = bpy.ops

def delete_all():
    for obj in D.objects:
        obj.select = True
    if O.object.delete() == {'FINISHED'}:
        return 0
    else:
        return -1

def set_unit_metric():
    '''METRIC, DEGREE
    display as (cm)
    actually, it doesn't matter. sty file will always be inputed as arbitrary unit'''
    C.scene.unit_settings.system = 'METRIC'
    C.scene.unit_settings.system_rotation = 'DEGREES'
    C.scene.unit_settings.scale_length = 1
    return

'''
bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=1.0, depth=2.0,
end_fill_type='NGON', view_align=False, enter_editmode=False,
location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0),
layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
'''
def add_coinbody():
    O.mesh.primitive_cylinder_add(radius=1.5, depth=0.1, location=(0.0,0.0,-0.05))
    ob = C.object
    ob.name = 'Coin_body'
    ob.data.name = 'Coin_body_mesh'
    return ob

def save_model():
    O.wm.save_as_mainfile(filepath='mycoin.blend')

if __name__ == '__main__':
    delete_all()
    # set_unit_metric()

    O.mesh.primitive_plane_add(radius=1, location=(0.0,0.0,0.0))
    O.object.mode_set(mode='EDIT')
    O.mesh.subdivide(number_cuts=300)
    # O.object.mode_set(mode='OBJECT')

    O.object.modifier_add(type='DISPLACE')
    O.texture.new()
    D.textures['Texture'].type = 'IMAGE'

    O.image.open(filepath="/home/yicong/Documents/Blender_OpenCV/imgdiffbw.png")
    D.textures['Texture'].image=D.images[0]
    D.textures['Texture'].extension = 'CLIP'
    D.objects['Plane'].modifiers['Displace'].texture = D.textures['Texture']

    D.objects['Plane'].modifiers['Displace'].strength=-0.1
    D.objects['Plane'].modifiers['Displace'].mid_level=0.1

    O.object.mode_set(mode='OBJECT')
    O.object.modifier_apply(apply_as='DATA', modifier='Displace')

    add_coinbody()

    for obj in D.objects:
        obj.select = True
        C.scene.objects.active = obj
    O.object.join()

    save_model()


