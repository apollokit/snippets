#!/usr/bin/env python
# from: https://stackoverflow.com/q/52910944/4292910

import vtk

ColorBackground = [0.0, 0.0, 0.0]

in_file = "airboat.obj"

reader = vtk.vtkOBJReader()
reader.SetFileName(in_file)
reader.Update()

mapper = vtk.vtkPolyDataMapper()

if vtk.VTK_MAJOR_VERSION <= 5:
     mapper.SetInput(reader.GetOutput())
else:
     mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a rendering window and renderer
ren = vtk.vtkRenderer()
ren.SetBackground(ColorBackground)
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# Create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Assign actor to the renderer
ren.AddActor(actor)

# Enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()