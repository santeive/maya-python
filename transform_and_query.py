import maya.cmds as cmds 

# cube[transform, object]
cube = cmds.polyCube()
print(cube)

# Query the width
cube_width = cmds.polyCube(cube[1], query=True, width=True)

# Create a sph based in the width's cube
sph = cmds.polySphere(radius = cube_width/2)

# Transforming objets

# Move, Rotate, Scale
cmds.move(1,0,0, cube[0], localSpace=True)
cmds.rotate(0,45,0, cube[0], relative=True)
cmds.scale(2,2,3, cube[0])

# xform - Obtenemos atributos de transformación
cube_t = cmds.xform(cube[0], query=True, translation=True)
cmds.xform(sph[0], translation=cube_t)

cube_bb = cmds.xform(cube[0], query=True, bb=True)
print cube_bb


