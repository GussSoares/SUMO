#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random

def remove_lines(files):                                                                #remove as linhas que possuem vehiculos criados
    line = sys.argv[3]
    with open(files,"r") as file:
        text=file.readlines()
    with open(files,"w") as file:
        for i in text:
            if text.index(i) >= int(line)-1:
                file.write("")
            else:
                file.write(i)

def insert_car(file):                                                                   #insere carros a partir da posicao especificada
    car_qtd = sys.argv[1]
    with open("teste.rou.xml","a") as file:
        for value in range(0,int(car_qtd)):
            file.write("\t<vehicle id=\"car{}\" depart=\"{}\" departLane=\"best\" route=\"route_{}\" type=\"Car\" color=\".{},.{},.{}\"/>\n".format(value, int(value), random.randint(0,3), random.randint(0,9), random.randint(0,9), random.randint(0,9)))

def insert_bus(file):                                                                   #insere onibus a partir da posicao especificada
    bus_qtd = sys.argv[2]
    with open("teste.rou.xml","a") as file:
        for value1 in range(0,int(bus_qtd)):                                            #onibus so fazem rodas que possuem paradas
            file.write("\t<vehicle id=\"bus{}\" depart=\"{}\" departLane=\"best\" route=\"route_2\" type=\"Bus\" color=\".{},.{},.{}\">\n".format(value1, int(bus_qtd)+value1, random.randint(0,9), random.randint(0,9), random.randint(0,9)))
            file.write("\t\t<stop busStop=\"busStop_gneE52_0_0\" duration=\"20\"/>\n")  #paradas q os onibus devem fazer
            file.write("\t\t<stop busStop=\"busStop_gneE57_0_1\" duration=\"20\"/>\n")  #paradas q os onibus devem fazer
            file.write("\t</vehicle>\n")

def main():
    remove_lines("teste.rou.xml")
    insert_car("teste.rou.xml")
    insert_bus("teste.rou.xml")
    with open("teste.rou.xml", "a") as file:
        file.write("</routes>")                                                         #escreve a linha de fecho do arquivo

if __name__ == "__main__":
    main()
