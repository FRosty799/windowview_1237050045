# Window-to-Viewport Transformation

Simple Python OpenGL example demonstrating viewport rendering using GLFW.

## Files

- `glviewport.py` - Main script that creates a GLFW window and draws a triangle with OpenGL.

## Requirements

- Python 3
- `glfw`
- `PyOpenGL`

## Install

```powershell
python -m pip install glfw PyOpenGL
```

## Usage

```powershell
python glviewport.py
```

## Description

This project initializes a GLFW window, sets the OpenGL viewport to the window size, and renders a triangle in normalized device coordinates (NDC).

The `glViewport` call controls the area of the window where OpenGL draws, illustrating how viewport transformation maps NDC coordinates to screen space.

## Notes

- Resize the window to see the viewport automatically adjust.
- Close the window to exit the application.
