FREECADPATH = '/lib/freecad/lib'
import sys
sys.path.append(FREECADPATH)

import FreeCAD
print FreeCAD.listDocuments()
mydoc = FreeCAD.activeDocument()


# ez elméletileg felmegy githubra


# Henger létrehozása

# App.ActiveDocument.addObject("Part::Cylinder","Cylinder")
# App.ActiveDocument.ActiveObject.Label = "Henger"
# App.ActiveDocument.recompute()
# Gui.SendMsgToActiveView("ViewFit")
# 
# 
# makeCylinder(radius,height,[pnt,dir,angle])
# 
# 
# import Part
# sr = Part.makeCylinder(400,1000)
# Part.show(sr)
# 
# 
# 
# sr.Label = "Rev"
# 
# su = App.ActiveDocument.addObject("Part::Cylinder","Henger")
# su.Label = "Schacht"
# su.Radius = 500
# su.Height = 1000
# su.Angle = 360
# 
# 

