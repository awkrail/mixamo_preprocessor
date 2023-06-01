"""
Use blender to convert FBX (T-pose) to BVH file
"""
import os
import bpy
import numpy as np

def get_bvh_name(filename):
    filename = filename.split(".")[-2]
    return filename + ".bvh"

def main():
    fbx_dir = "./mixamo/fbx/"
    bvh_dir = "./mixamo/bvh/"

    for filename in os.listdir(fbx_dir):
        fbx_path = os.path.join(fbx_dir, filename)
        bvh_path = os.path.join(bvh_dir, get_bvh_name(filename))

        bpy.ops.import_scene.fbx(filepath=fbx_path)
        action = bpy.data.actions[-1]

        frame_start = action.frame_range[0]
        frame_end = max(60, action.frame_range[1])

        bpy.ops.export_anim.bvh(filepath=bvh_path,
                                frame_start=int(frame_start),
                                frame_end=int(frame_end),
                                root_transform_only=True)

        bpy.data.actions.remove(bpy.data.actions[-1])

if __name__ == "__main__":
    main()
