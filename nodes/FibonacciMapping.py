import bpy
from bpy.props import *
from animation_nodes.events import propertyChanged
from animation_nodes.base_types import AnimationNode

class FibonacciMappingNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_FibonacciMappingNode"
    bl_label = "Fibonacci Mapping"

    count = FloatProperty(name = "Count", default = False, update = propertyChanged)
    radius = FloatProperty(name = "Radius", default = False, update = propertyChanged)
    
    def create(self):
        self.newInput("Float", "count", "count")
        self.newInput("Float", "radius", "radius")
        
    def draw(self, layout):
        layout.prop(self, "count")
        layout.prop(self, "radius")

    def execute(self, count, radius,):
        rnd = 1.;
        offset = 2. / count;
        increment = PI * (3. - sqrt(5.));
        y = ((i * offset) - 1.) + (offset / 2.);
        r = sqrt(1. - pow(y ,2.));
        phi = mod(i + rnd, count) * increment;
        x = cos(phi) * r;
        z = sin(phi) * r;
        return vec3(x, y, z);