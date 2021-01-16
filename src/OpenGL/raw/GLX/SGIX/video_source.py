'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_SGIX_video_source'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLX,'GLX_SGIX_video_source',error_checker=_errors._error_checker)

@_f
@_p.types(_cs.GLXVideoSourceSGIX,ctypes.POINTER(_cs.Display),_cs.c_int,_cs.VLServer,_cs.VLPath,_cs.c_int,_cs.VLNode)
def glXCreateGLXVideoSourceSGIX(display,screen,server,path,nodeClass,drainNode):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXVideoSourceSGIX)
def glXDestroyGLXVideoSourceSGIX(dpy,glxvideosource):pass
