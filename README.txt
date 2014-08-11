===========
PyDAQmx-Helper
===========

PyDAQmx-Helper provides a set of specialised classes that replace using a 'Task' in PyDAQmx. It is usefull for simple applications of the PyDAQmx library.
Typical usage
often looks like this::

    #!/usr/bin/env python

    from PyDAQmx-Helper import atod

    from atod import AtoD
    myAtoD = AtoD()
    myAtoD.addChannels([0])
    val = myAtoD.readVoltage()
    print(val)




Installation
=========

* Install through github

* Install through Pip

A Sub-Section
-------------

Numbered lists look like you'd expect:

1. hi there

2. must be going

Urls are http://like.this and links can be
written `like this <http://www.example.com/foo/bar>`_.
