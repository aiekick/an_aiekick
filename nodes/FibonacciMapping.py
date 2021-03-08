import bpy
from bpy.props import *
from animation_nodes.events import propertyChanged
from animation_nodes.base_types import AnimationNode

class FibonacciMappingNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_FibonacciMappingNode"
    bl_label = "Fibonacci Mapping"

    useX = BoolProperty(name = "Use X", default = False, update = propertyChanged)
    useY = BoolProperty(name = "Use Y", default = False, update = propertyChanged)
    useZ = BoolProperty(name = "Use Z", default = False, update = propertyChanged)

    def create(self):
        self.newInput("Object", "Source", "source")
        self.newInput("Object", "Target", "target")
        self.newInput("Vector", "Offset", "offset")

    def draw(self, layout):
        layout.prop(self, "useX")
        layout.prop(self, "useY")
        layout.prop(self, "useZ")

    def execute(self, source, target, offset):
        if source is None or target is None:
            return

        if self.useX: target.location.x = source.location.x + offset.x
        if self.useY: target.location.y = source.location.y + offset.y
        if self.useZ: target.location.z = source.location.z + offset.z