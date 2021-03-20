import maya.cmds as cmds

#script_del_chico_malvavisco

sel = cmds.ls(sl=True)

for s in sel:
    padre = cmds.listRelatives(s, parent=True)
    objeto = cmds.xform(s, query=True, matrix=True,worldSpace=True)
    
    grp_root = cmds.group(empty=True, name=s + '_root')
    cmds.xform(grp_root, matrix=objeto, worldSpace=True)
    
    grp_auto = cmds.group(empty=True, name=s + '_auto')
    cmds.xform(grp_auto, matrix=objeto, worldSpace=True)
    
    cmds.parent(s, grp_auto)
    cmds.parent(grp_auto, grp_root)
    
    if padre:
    	cmds.parent(grp_root, padre)