#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def remove_lines(files, line):
    with open(files,"r") as file:
        text=file.readlines()
    with open(files,"w") as file:
        for i in text:
            if text.index(i) >= line-1:
                file.write("")
            else:
                file.write(i)

def insert_cars(file):
    word = sys.argv[1]
    with open("teste.rou.xml","a") as file:
        for value in range(0,int(word)):
            file.write("\t<vehicle id=\"car{}\" depart=\"{}\" departLane=\"best\" route=\"route_1\" type=\"Car\" color=\".2,0,.2\"/>\n".format(value, int(value)+10, word))
            # print("\t<vehicle id=\"car{}\" numer=\"{}\" begin=\"0\" end=\"0\" type=\"Car\"/>".format(value, word))
        # print("</routes>")
        file.write("</routes>")
def main():
    remove_lines("teste.rou.xml", 63)
    insert_cars("teste.rou.xml")

if __name__ == "__main__":
    main()
