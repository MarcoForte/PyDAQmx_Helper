===========
PyDAQmx_Helper
===========

PyDAQmx-Helper provides a set of specialised classes that replace using a 'Task' in PyDAQmx. It is usefull for simple applications of the PyDAQmx library.
Typical usage
often looks like this::

    #!/usr/bin/env python

    from pydaqmx_helper.atod import AtoD
    myAtoD = AtoD()
    myAtoD.addChannels([0])
    val = myAtoD.readVoltage()
    print(val)




Installation
=========

Download zip and move to  python folder and use pip with my setup.py
