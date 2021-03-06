from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    #glOrtho( -10 , 10 , -10 , 10 , -10 , 10 )
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
x=0
angle=0
dx=0.004
dangle=0.4



def draw():

    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global angle
    global dx
    global dangle

    glMatrixMode(GL_MODELVIEW)
# The Road



    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(-(0.25)*x-6, 0, -1 * 34)
    glScale(0.2, 10, -0.5)
    glutSolidCube(4.5)

    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(-(0.25)*x-26, 0, -1 * 22)
    glScale(0.2, 10, -0.5)
    glutSolidCube(4.5)

    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(-x, 0, -1 * 6)
    glScale(100, 0.25, -0.5)
    glutWireCube(4.5)

    glLoadIdentity()
    glTranslate(-x, 0,( -1 * 5)-0.1)
    glScale(100, 0.25, 0.002)
    glutSolidCube(4.5)

    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(-x, 0, 0.1)
    glScale(1.5, 0, -0.25)
    glutSolidCube(4.5)

    glLoadIdentity()
    glTranslate(-x-10, 0, 0.1)
    glScale(1.5, 0, -0.25)
    glutSolidCube(4.5)

    glLoadIdentity()
    glTranslate(-x+10, 0, 0.1)
    glScale(1.5, 0, -0.25)
    glutSolidCube(4.5)

    glLoadIdentity()
    glTranslate(-x-20, 0, 0.1)
    glScale(1.5, 0, -0.25)
    glutSolidCube(4.5)

    glLoadIdentity()
    glTranslate(-x - 30, 0, 0.1)
    glScale(1.5, 0, -0.25)
    glutSolidCube(4.5)

    glLoadIdentity()
    glTranslate(-x - 40, 0, 0.1)
    glScale(1.5, 0, -0.25)
    glutSolidCube(4.5)



#Car_Body


    glMatrixMode(GL_MODELVIEW)

    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(x - 2.5, - 2.5 * .25, (-2.5 * 0.5) - 0.5)
    glRotatef(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)

    glLoadIdentity()
    glColor3f(1, 0, 0)
    glTranslate(x, 0, -0.5)
    glScale(1.0, 0.25, 0.5)
    glutSolidCube(4.5)

    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(x,0,-0.5)
    glScale(1.0,0.25,0.5)
    glutWireCube(5)

    glLoadIdentity()
    glColor3f(1, 0, 0)
    glTranslate(x, 0.25 * 5, -0.5)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(x, 0.25 * 5, -0.5)
    glScale(0.5, 0.25, 0.5)
    glutWireCube(4.5)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(x+0.5, 0.25 * 3.3, 0.7)
    glScale(0.15, 0.35, 0)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(x - 0.5, 0.25 * 3.3, 0.7)
    glScale(0.15, 0.35, 0)
    glutSolidCube(5)

    glColor3f(0,0,0)

    glLoadIdentity()
    glTranslate(x+2.5,-2.5*.25,(2.5*.5)-0.5)
    glRotatef(angle,0,0,1)
    glutWireTorus(0.125,0.5,12,8)

    glColor3f(0,0,0)
    glLoadIdentity()
    glTranslate(x+2.5, -2.5 * .25, (-2.5*.5)-0.5)
    glRotatef(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)

    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(x-2.5, -2.5 * .25, (2.5*.5)-0.5)
    glRotatef(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)



    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(0, 0, 2*2.5)
    glScale(100, 0.25, 0.5)
    glutWireCube(4.5)

    glLoadIdentity()
    glTranslate(0, 0, (2*2.5)-1.5)
    glScale(100, 0.25, 0.000000005)
    glutSolidCube(4)

    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(-x, 0, -1 * 6)
    glScale(0.2, 10, -0.5)
    glutSolidCube(4.5)

    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(-x-29, 0, -1 * 6)
    glScale(0.2, 10, -0.5)
    glutSolidCube(4.5)

    if x > 7:
        dx = -0.004
        dangle = -0.4
    elif x < -17:
        dx= 0.004
        dangle = 0.4

    x += dx
    angle -= dangle
    glFlush()



glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)   # Set the window's initial width & height
glutCreateWindow(b"Moving Car")
glutDisplayFunc(draw)
glutIdleFunc(draw)

myinit()
glutMainLoop()

