#!/bin/bash
# argv[1] = numero de carros
# argv[2] = numero de onibus
# argv[3] = primeira linha de veiculos no arquivo teste.rou.xml para q ele apague os existentes e insira outros a partir dali
python add_vehicle.py 30 30 21
# abre o sumo para rodar a simulacao
sumo-gui teste.sumo.cfg
