===========
PyDAQmx_Helper
===========

PyDAQmx-Helper provides a set of simplified classes for communicating with the National Instruments USB 6008 module, via the PyDAQmx module (which must be installed). They should also work with the USB 6009 although some features might be missing. They have been tested and work with Python 3.5. (PyDAQmx? DAQmx?)

The classes provide interfaces for the Analogue-to-Digital Convertors, Digital-to-Analogue Convertors, DigitalIO and Counters.  They were developed for Physics undergraduate laboratories at University College Dublin based on in-house C++ classes. These python classes were originally developed by Marco Forte as part of a summer internship.

Typical usage often looks like this::

    #!/usr/bin/env python

    from pydaqmx_helper.atod import AtoD
    myAtoD = AtoD()
    myAtoD.addChannels([0])
    val = myAtoD.readVoltage()
    print(val)


Installation
=========

Download zip and move to python folder and use pip with my setup.py
