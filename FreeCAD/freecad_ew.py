#!/usr/bin/env python3


# ez elméletileg felmegy githubra

def fcmacro(name, text):
    ''' Make macro for FreeCAD. '''
    file = open('/home/bucomar/.FreeCAD/Macro/' + name + '.FCMacro', 'w+')
    
    file.write(text)
    file.close()

# 1777_EW.FCMacro
code = """

#### Ideee kő írnijja FreeCAD koódott ééé!

FreeCAD.newDocument()
App.ActiveDocument.addObject("Part::Cylinder","Cylinder")

# Henger létrehozása
App.ActiveDocument.ActiveObject.Label = "Henger"
App.ActiveDocument.recompute()

"""



fcmacro('1556', code)



"""
FreeCAD.newDocument()\n'
App.ActiveDocument.addObject("Part::Cylinder","Cylinder")\n'

# Henger létrehozása
App.ActiveDocument.ActiveObject.Label = "Henger"\n'
App.ActiveDocument.recompute()\n'
Gui.SendMsgToActiveView("ViewFit")\n'


makeCylinder(radius,height,[pnt,dir,angle])\n'


import Part\n'
sr = Part.makeCylinder(400,1000)\n'
Part.show(sr)\n'
sr.Label = "Rev"\n'

su = App.ActiveDocument.addObject("Part::Cylinder","Henger")\n'
su.Label = "Schacht"\n'
su.Radius = 500\n'
su.Height = 1000\n'
su.Angle = 360\n'
doc.recompute()')

"""

