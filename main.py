from render import Render, V2, V3

from obj import Obj

from texture import Texture

from shaders import gourad, toon

from utils import color

r = Render()
r.glCreateWindow(1000,1000)
r.glClear()

r.active_texture = Texture('./models/model.bmp')
r.active_shader = toon

#r.light = V3(1,0,0)

r.loadModel('./models/model.obj', V3(500,500,0), V3(300,300,300))


r.glFinish('output.bmp')
