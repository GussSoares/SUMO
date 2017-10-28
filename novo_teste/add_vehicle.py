#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def remove_lines(files):
    line = sys.argv[3]
    with open(files,"r") as file:
        text=file.readlines()
    with open(files,"w") as file:
        for i in text:
            if text.index(i) >= int(line)-1:
                file.write("")
            else:
                file.write(i)

def insert_car(file):
    car_qtd = sys.argv[1]
    with open("teste.rou.xml","a") as file:
        for value in range(0,int(car_qtd)):
            file.write("\t<vehicle id=\"car{}\" depart=\"{}\" departLane=\"best\" route=\"route_1\" type=\"Car\" color=\".2,0,.2\"/>\n".format(value, int(value), car_qtd))
            # print("\t<vehicle id=\"car{}\" numer=\"{}\" begin=\"0\" end=\"0\" type=\"Car\"/>".format(value, word))
        # print("</routes>")

def insert_bus(file):
    bus_qtd = sys.argv[2]
    with open("teste.rou.xml","a") as file:
        for value1 in range(0,int(bus_qtd)):
            file.write("\t<vehicle id=\"bus{}\" depart=\"{}\" departLane=\"best\" route=\"route_2\" type=\"Bus\" color=\".2,0,.2\">\n".format(value1, int(bus_qtd)+value1, bus_qtd))
            file.write("\t\t<stop busStop=\"busStop_gneE52_0_0\" duration=\"20\"/>\n")
            file.write("\t\t<stop busStop=\"busStop_gneE57_0_1\" duration=\"20\"/>\n")
            file.write("\t</vehicle>\n")
            # print("\t<vehicle id=\"car{}\" numer=\"{}\" begin=\"0\" end=\"0\" type=\"Car\"/>".format(value, word))
        # print("</routes>")


def main():
    remove_lines("teste.rou.xml")
    insert_car("teste.rou.xml")
    insert_bus("teste.rou.xml")
    with open("teste.rou.xml", "a") as file:
        file.write("</routes>")

if __name__ == "__main__":
    main()
