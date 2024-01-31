#!/usr/bin/python3

import playsound

a1='Free_Test_Data_100KB_MP3.mp3'
a2='Free_Test_Data_100KB_OGG.ogg' # The specified device is not open or is not recognized by MCI
a3='Free_Test_Data_500KB_WAV.wav' # virker

playsound.playsound(a1)


# what about pyaudio?
# pygame also works.

"""
  DEPRECATION: 
  playsound is being installed using the legacy 'setup.py install' method, 
  because it does not have a 'pyproject.toml' 
  and the 'wheel' package is not installed. 
  pip 23.1 will enforce this behaviour change. 
  A possible replacement is to enable the '--use-pep517' option. 
  Discussion can be found at https://github.com/pypa/pip/issues/8559
"""