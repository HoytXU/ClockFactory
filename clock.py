import bpy
import numpy as np
from numpy.random import randint as RI
from numpy.random import uniform
from numpy.random import uniform as U

from infinigen.assets.material_assignments import AssetList
from infinigen.assets.materials import (
    glass_shader_list,
)
from infinigen.assets.utils.autobevel import BevelSharp
from infinigen.assets.utils.object import get_joint_name
from infinigen.core import surface
from infinigen.core.nodes import node_utils
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.placement.factory import AssetFactory
from infinigen.core.util import blender as butil
from infinigen.core.util.blender import deep_clone_obj
from infinigen.core.util.math import FixedSeed, clip_gaussian

from infinigen.core.nodes.node_utils import save_geometry_new, save_geometry
import copy

from infinigen.core.placement.factory import AssetFactory
from infinigen.core.util.math import FixedSeed


class ClockFactory(AssetFactory):
    def __init__(self, factory_seed=0):
        super().__init__(factory_seed)

        with FixedSeed(factory_seed):
            self.params = self.sample_parameters()

    @staticmethod
    def sample_parameters():
        return {
        }

    def create_asset(self, **params):
        obj_params = self.sample_parameters()
        self.params.update(obj_params)
        params = self.params

        obj = butil.spawn_cube()
        butil.modify_mesh(
            obj,
            "NODES",
            node_group=node_clock_pan(),
            ng_inputs=self.params,
            apply=True,
        )


        names = ["clock_pan", "hour_hand", "minute_hand", "clock_ring"]
        first = True
        parent_id = "world"
        joint_info = {
            "name": get_joint_name("revolute"),
            "type": "revolute",
            "axis": [0, 0, 1],
            "limit":{
                "lower": -np.pi / 2,
                "upper": np.pi / 2,
            },   
        }

        save_geometry_new(obj, 'whole', 0, params.get("i", None), params.get("path", None), parent_obj_id="world", first=True, use_bpy=True)
        
        return obj

def shader_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Emission Strength': 0.0000},
        attrs={'distribution': 'MULTI_GGX', 'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})


@node_utils.to_nodegroup(
    "node_clock_pan", singleton=True, type="GeometryNodeTree"
)
def node_clock_pan(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketGeometry', 'Geometry', None)])
    
    transform_geometry_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Translation': (0.7000, 0.0000, 0.0300), 'Scale': (0.0600, 0.0100, 0.0100)})
    
    transform_geometry_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_geometry_1, 'Rotation': (0.0000, 0.0000, 0.5236)})
    
    transform_geometry_3 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_geometry_1, 'Rotation': (0.0000, 0.0000, 1.0472)})
    
    transform_geometry_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_geometry_1, 'Rotation': (0.0000, 0.0000, 2.0944)})
    
    transform_geometry_12 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_geometry_1, 'Rotation': (0.0000, 0.0000, 1.5708)})
    
    transform_geometry_11 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_geometry_1, 'Rotation': (0.0000, 0.0000, 2.6180)})
    
    transform_geometry_10 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_geometry_1, 'Rotation': (0.0000, 0.0000, 3.1416)})
    
    transform_geometry_9 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_geometry_1, 'Rotation': (0.0000, 0.0000, 3.6652)})
    
    transform_geometry_8 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_geometry_1, 'Rotation': (0.0000, 0.0000, 4.1888)})
    
    transform_geometry_7 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_geometry_1, 'Rotation': (0.0000, 0.0000, 4.7124)})
    
    transform_geometry_6 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_geometry_1, 'Rotation': (0.0000, 0.0000, 5.2360)})
    
    transform_geometry_5 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_geometry_1, 'Rotation': (0.0000, 0.0000, 5.7596)})
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder', input_kwargs={'Radius': 0.8000, 'Depth': 0.0300})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [transform_geometry_2, transform_geometry_3, transform_geometry_4, transform_geometry_12, transform_geometry_11, transform_geometry_10, transform_geometry_9, transform_geometry_8, transform_geometry_7, transform_geometry_6, transform_geometry_5, transform_geometry_1, cylinder.outputs["Mesh"]]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})

@node_utils.to_nodegroup(
    "node_hour_hand", singleton=True, type="GeometryNodeTree"
)
def node_hour_hand(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    mesh_line = nw.new_node(Nodes.MeshLine, input_kwargs={'Count': 1, 'Offset': (0.0000, 0.0000, 0.0000)})
    
    cylinder_1 = nw.new_node('GeometryNodeMeshCylinder')
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': mesh_line, 'Instance': cylinder_1.outputs["Mesh"]})
    
    transform_geometry = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': instance_on_points, 'Translation': (0.0000, 2.0000, 0.0000), 'Rotation': (1.5708, 0.0000, 0.0000), 'Scale': (0.5000, 0.5000, 2.0000)})
    
    cone = nw.new_node('GeometryNodeMeshCone')
    
    transform_geometry_13 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': cone.outputs["Mesh"], 'Rotation': (1.5708, 0.0000, 0.0000)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform_geometry, transform_geometry_13]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ)
    
    transform_geometry_14 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': join_geometry_1, 'Translation': (0.0000, -0.4000, 0.0500), 'Rotation': combine_xyz, 'Scale': (0.0500, 0.1000, 0.0500)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': transform_geometry_14})
    
    group_output_2 = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})

@node_utils.to_nodegroup(
    "node_minute_hand", singleton=True, type="GeometryNodeTree"
)
def node_minute_hand(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    mesh_line = nw.new_node(Nodes.MeshLine, input_kwargs={'Count': 1, 'Offset': (0.0000, 0.0000, 0.0000)})
    
    cylinder_1 = nw.new_node('GeometryNodeMeshCylinder')
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': mesh_line, 'Instance': cylinder_1.outputs["Mesh"]})
    
    transform_geometry = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': instance_on_points, 'Translation': (0.0000, 2.0000, 0.0000), 'Rotation': (1.5708, 0.0000, 0.0000), 'Scale': (0.5000, 0.5000, 2.0000)})
    
    cone = nw.new_node('GeometryNodeMeshCone')
    
    transform_geometry_13 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': cone.outputs["Mesh"], 'Rotation': (1.5708, 0.0000, 0.0000)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform_geometry, transform_geometry_13]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ)
    
    transform_geometry_14 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': join_geometry_1, 'Translation': (0.0000, -0.4000, 0.0500), 'Rotation': combine_xyz, 'Scale': (0.0500, 0.1000, 0.0500)})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': -4.1000})
    
    transform_geometry_15 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': transform_geometry_14, 'Rotation': combine_xyz_1, 'Scale': (1.0000, 1.3000, 1.0000)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': transform_geometry_15})
    
    group_output_1 = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})


