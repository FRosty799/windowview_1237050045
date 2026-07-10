import glfw
from OpenGL.GL import *

def main():
    # 1. Inisialisasi GLFW
    if not glfw.init():
        return

    # 2. Buat Jendela (Window)
    window = glfw.create_window(800, 600, "Window-to-Viewport Transformation", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # 3. Loop Render
    while not glfw.window_should_close(window):
        # Membersihkan layar
        glClear(GL_COLOR_BUFFER_BIT)

        # 4. Implementasi Viewport
        # glViewport(x, y, width, height)
        # Ini menentukan area di dalam jendela tempat gambar akan dirender.
        # Jika kita ingin gambar memenuhi seluruh jendela:
        width, height = glfw.get_framebuffer_size(window)
        glViewport(0, 0, width, height)

        # Menggambar objek (Segitiga)
        # Koordinat di bawah adalah koordinat NDC (Normalized Device Coordinates)
        # yang secara otomatis ditransformasikan ke Viewport oleh pipeline OpenGL.
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(-0.5, -0.5)
        glVertex2f(0.5, -0.5)
        glVertex2f(0.0, 0.5)
        glEnd()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()