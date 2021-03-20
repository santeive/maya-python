from maya import cmds

SUFFIXES = {
    "mesh": "geo",
    "joint": "jnt",
    "camera": None,
    "ambientLight": "lgt"
}

def rename(sel=False):
    sel = cmds.ls(sl=True)

    if len(sel) == 0:
        #Si no se selecciona nada, (dag) toma el outliner
        sel = cmds.ls(dag=True, long=True)

    sel.sort(key=len, reverse=True)
    print sel    

    for obj in sel:
        shortName = obj.split('|')[-1]
        
        children = cmds.listRelatives(obj, children=True, fullPath=True) or []
        
        if len(children) == 1:
            child = children[0]
            objType = cmds.objectType(child)
        else:
            objType = cmds.objectType(obj)

        suffix = SUFFIXES.get(objType, DEFAULT_SUFFIX)

        if not suffix:
            continue

        if obj.endswith(suffix):
            continue
        
        newName = shortName + "_" + suffix
        print(newName)
        
        cmds.rename(obj, newName)
        