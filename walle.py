from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from math import *
def choosecolor(c):
    alist=[]
    if c==1 :#darkyellow
        alist.append(1)
        alist.append(.9)
        alist.append(.1)
    elif c==2: #wideyellow
        alist.append(.9)
        alist.append(1)
        alist.append(.5)
    elif c==3:# burrble
        alist.append(.5)
        alist.append(0)
        alist.append(.8)
    elif c==4 :#dark blue
        alist.append(.6)
        alist.append(.6)
        alist.append(.7)
    elif c==5 :#wideblue
        alist.append(.6)
        alist.append(.6)
        alist.append(.5)
    elif c==6: #red
        alist.append(.9)
        alist.append(0)
        alist.append(0)
    elif c==7 :#blue
        alist.append(.4)
        alist.append(.1)
        alist.append(.9)
    elif c==8 :#white
        alist.append(1)
        alist.append(1)
        alist.append(1)
    elif c==9 : #black
        alist.append(0)
        alist.append(0)
        alist.append(0)
    elif c==10 :#widered
        alist.append(1)
        alist.append(.2)
        alist.append(.2)
    elif c==11:#brown
        alist.append(.8)
        alist.append(.4)
        alist.append(.2)
    elif c==12:# blue
        alist.append(.4)
        alist.append(1)
        alist.append(1)



    return alist






def drawpolygon(x1,y1,x2,y2,x3,y3,x4,y4,c):
    listcolor =choosecolor(c)
    glBegin(GL_POLYGON)
    glColor3f(listcolor[0],listcolor[1],listcolor[2])
    glVertex(x1, y1)
    glVertex(x2,y2)
    glVertex(x3,y3)
    glVertex(x4,y4)
    glEnd()
    glFlush()

def drawpolygon5add(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,c):
    listcolor =choosecolor(c)
    glBegin(GL_POLYGON)
    glColor3f(listcolor[0],listcolor[1],listcolor[2])
    glVertex(x1, y1)
    glVertex(x2,y2)
    glVertex(x3,y3)
    glVertex(x4,y4)
    glVertex(x5,y5)
    glEnd()
    glFlush()
def drawpolygon6add(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,c):
    listcolor =choosecolor(c)
    glBegin(GL_POLYGON)
    glColor3f(listcolor[0],listcolor[1],listcolor[2])
    glVertex(x1, y1)
    glVertex(x2,y2)
    glVertex(x3,y3)
    glVertex(x4,y4)
    glVertex(x5,y5)
    glVertex(x6,y6)
    glEnd()
    glFlush()
def drawcircle (r=.1,cx=0,cy=0,c=1):
    color=choosecolor(c)
    glBegin(GL_POLYGON)
    glColor3f(color[0],color[1],color[2])
    for theta in np.arange(0,2*pi,.01):
        x=r*cos(theta)+cx
        y=r*sin(theta)+cy
        glVertex(x,y)
    glEnd()
    glFlush()
def drawcirclecolor (r=.1,cx=0,cy=0):

    glBegin(GL_POLYGON)
    for theta in np.arange(0,2*pi,.01):
        glColor3f(.4,theta,.6)
        x=r*cos(theta)+cx
        y=r*sin(theta)+cy
        glVertex(x,y)
    glEnd()
    glFlush()
def halfdrawcircle (r=.1,cx=0,cy=0,c=1):
    color=choosecolor(c)
    glBegin(GL_POLYGON)
    glColor3f(color[0],color[1],color[2])
    for theta in np.arange(0,pi,.01):
        x=r*cos(theta)+cx
        y=r*sin(theta)+cy
        glVertex(x,y)
    glEnd()
    glFlush()
def drawlineloop(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,c):
    colorlist=choosecolor(c)
    glBegin(GL_LINE_LOOP)
    glColor3f(colorlist[0],colorlist[1],colorlist[2])
    glVertex(x1, y1)
    glVertex(x2,y2)
    glVertex(x3,y3)
    glVertex(x4,y4)
    glEnd()
    glFlush()
def drawline(x1,y1,x2,y2,c):
    colorlist=choosecolor(c)
    glBegin(GL_LINES)
    glColor3f(colorlist[0],colorlist[1],colorlist[2])
    glVertex(x1,y1)
    glVertex(x2,y2)
    glEnd()
    glFlush()

def draw ():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    drawline(1,0,-1,0,9)
    drawline(0,1,0,-1,9)

    drawpolygon6add(.32, -.42, .43, -.42, .45, -.33, .45, -.27, .4, -.27, .37, -.3, 10)
    drawpolygon6add(-.32, -.42, -.43, -.42, -.45, -.33, -.45, -.27, -.4, -.27, -.37, -.3, 10)
    drawpolygon(.32,-.48,.43,-.48,.43,-.42,.32,-.42,11)
    drawpolygon(-.32, -.48, -.43, -.48, -.43, -.42, -.32, -.42, 11)
    drawpolygon(.46,-.46,.4,-.46,.4,-.44,.46,-.44,4)
    drawpolygon(-.46, -.46, -.4, -.46, -.4, -.44, -.46, -.44, 4)
    drawline(.4,.25,.5,.3,9)
    drawline(.4,.2,.5,.25,9)
    drawline(.5,.3,.6,.3,9)
    drawline(.5,.25,.6,.25,9)
    drawline(.6,.3,.8,.15,9)
    drawline(.6,.25,.75,.14,9)
    drawline(.8,.15,.82,.17,9)
    drawline(.75,.14,.72,.12,9)
    drawline(.82,.17,.85,.11,9)
    drawline(.72,.12,.73,.06,9)
    drawline(.73,.06,.85,.11,9)
    drawcircle(.03,.81,.06,11)
    drawcircle(.03,-.81,.06,11)

    drawpolygon(-.1,.3,.1,.3,.1,.6,-.1,.6,3)
    ############triangle
    glBegin(GL_POLYGON)
    glColor3f(.4,.7,.1)
    glVertex(-.1,.8)
    glVertex(.1,.8)
    glVertex(0,.6)
    glEnd()
    glFlush()

    drawcirclecolor(.06, .15, .82)
    drawcirclecolor(.06, -.15, .82)
    drawcircle(.03,.13,.8,6)
    drawcircle(.01,-.13/2,.8/2,9)
    drawcircle(.01, .13 / 2, .8 / 2, 9)
    drawcircle(.03,-.13,.8,6)
    drawcircle(.01,.12,.79,7)
    drawcircle(.01, -.12, .79, 7)

    drawline(.08,.9,.23,.9,9)
    drawline(-.08, .9, -.23, .9, 9)

    drawline(-.4, .25,- .5, .3, 9)
    drawline(-.4, .2, -.5, .25, 9)
    drawline(-.5, .3, -.6, .3, 9)
    drawline(-.5, .25, -.6, .25, 9)
    drawline(-.6, .3,- .8, .15, 9)
    drawline(-.6, .25, -.75, .14, 9)
    drawline(-.8, .15, -.82, .17, 9)
    drawline(-.75, .14, -.72, .12, 9)
    drawline(-.82, .17,- .85, .11, 9)
    drawline(-.72, .12, -.73, .06, 9)
    drawline(-.73, .06,- .85, .11, 9)


    drawpolygon(-.4,-.3,.4,-.3,.4,.3,-.4,.3,1)
    drawpolygon(-.05, -.2, .05, -.2, .05, .2, -.05, .2, 12)
    for x in np.arange(-.2,.2,.02):
        glBegin(GL_POINTS)
        glColor3f(1,0,.2)
        glVertex(0,x)
        glEnd()
        glFlush()

    for i in np.arange(-.3,.3,.01):
        drawline(.4,i,-.4,-i,2)
    drawpolygon(.45,-.6,.65,-.6,.65,-.2,.45,-.2,11)
    drawpolygon(-.65,-.6,-.45,-.6,-.45,-.2,-.65,-.2,11)
    drawlineloop(-.4,-.3,.4,-.3,.4,.3,-.4,.3,-.4,-.3,9)
    for i in np.arange(-.2,-.6,-.05):
        drawline(.45,i,.65,i,8)
    for i in np.arange(-.2,-.6,-.05):
        drawline(-.45,i,-.65,i,8)




















































glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"walle")
glutDisplayFunc(draw)
glutMainLoop()