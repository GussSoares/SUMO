#!/bin/bash

sumo -c teste.sumo.cfg --netstate-dump tracefile.xml
java -jar traceExporter.jar ns2 -n teste.net.xml -t tracefile.xml -a a.out -c c.out -m s.tcl
