#!/bin/bash

netconvert --offset.x=1.0 --offset.y=1.0 --node-files=s.nod.xml --edge-files=s.edg.xml --output-file=s.net.xml
sumo -c s.sumo.cfg --netstate-dump tracefile.xml
java -jar traceExporter.jar ns2 -n s.net.xml -t tracefile.xml -a a.out -c c.out -m s.tcl -b 200 -e 600 -p 1.0



