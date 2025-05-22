# This script needed to points, really studid way; there is much better i guess, but if it works, it works

import traceback
import adsk.core
import adsk.fusion

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct

        # Replace with your points
        points = [
            # POINTS HERE format: (x_1,y_1), (x_2,y_2), (x_3,y_3)... (x_n, y_n) 
        ]

        rootComp = design.rootComponent
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)

        sketchPoints = []
        for pt in points:
            sketchPoints.append(adsk.core.Point3D.create(pt[0], pt[1], 0))

        for i in range(len(sketchPoints) - 1):
            sketch.sketchCurves.sketchLines.addByTwoPoints(sketchPoints[i], sketchPoints[i + 1])

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))