import maya.cmds as cmds 

#script_del_chico_malvavisco

#Creamos un cilindro
#cmds.polyCylinder(n="cilinder_xy")

#Mostramos los elementos dqe la seleccion
sel = cmds.ls(sl=True)
print(sel, len(sel))

if len(sel) == 1:
    cont = cmds.circle(name=sel[0] + "_control", nr=[0,1,0])
    parent_constraint = cmds.parentConstraint(sel, cont)
    scale_constraint = cmds.scaleConstraint(sel, cont)
    #Para eliminar el constraint
    cmds.delete(parent_constraint, scale_constraint)
    
elif len(sel) == 2:
    constPoint = cmds.parentConstraint(sel[0], sel[1])
    constScale = cmds.scaleConstraint(sel[0], sel[1])
    #Para eliminar el constraint y solo alinear
    cmds.delete(constPoint, constScale)
    
elif len(sel) > 2:
    for i in range(len(sel)):
        cont = cmds.circle(name=sel[i] + "_control_" + str(i), nr=[0,1,0])
        constraintParent = cmds.parentConstraint(sel[i], cont)
        constScale = cmds.scaleConstraint(sel[i], cont)
        #cmds.delete(constraintParent, constScale)
    
else:
    cmds.warning('Selecciona un objeto')

# MAYA -DOC
# https://help.autodesk.com/view/MAYAUL/2020/ENU/

# MAYA - PYTHON COMMANDS
# https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=__CommandsPython_index_html