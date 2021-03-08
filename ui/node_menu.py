import bpy
from animation_nodes.ui.node_menu import insertNode

class AiekickNodesMenu(bpy.types.Menu):
    bl_idname = "AN_MT_AiekickNodes_menu"
    bl_label = "Aiekick Nodes"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_FibonacciMappingNode", "Fibonacci Mapping")

def drawMenu(self, context):
    if context.space_data.tree_type != "an_AnimationNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    layout.separator()
    layout.menu("AN_MT_AiekickNodes_menu", text = "Aiekick Nodes", icon = "SCRIPTPLUGINS")

def register():
    bpy.types.NODE_MT_add.append(drawMenu)

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)