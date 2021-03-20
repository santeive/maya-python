import maya.cmds as cmds

#script_del_chico_malvavisco

#Creamos un cubo standard
#maya.cmds.polyCube()

#Creamos una instancia de cubo con nombre
cmds.polyCube(name="cubo_mio", height=5, width=10)


''' Transformación de objects '''

#Creamos una esfera
cmds.polySphere(name="esfera")

cmds.move(10, 1, 1, 'cubo_mio')
cmds.move(1, 10, 1, 'esfera') 


''' Leer y escribir atributos '''
sel = cmds.ls(sel=True)

#Leemos atributos
obj = cmds.polyCube(name='cubo_mio2')

#Traer informcion de transformacion del objeto
cmds.getAttr('cubo_mio2.translateX')
cmds.getAttr('cubo_mio2.translate')
cmds.getAttr('cubo_mio2.rotate')
cmds.getAttr('cubo_mio2.scale')

# Modificaciones de atributos 
objeto = cmds.polySphere(name="esfera")

# En el atributo objeto[1] nos referimos nodo de shape de transformacion
# Se puede visualizar seleccionando el objeto y visualizando el node editor

cmds.setAttr(objeto[1] + '.subdivisionsAxis',3)

#Visto hasta Leccion de Loops