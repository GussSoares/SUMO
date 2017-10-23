#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string>
double ExpRnd(double mean) {
	double unif_rnd, exp_rnd;

	unif_rnd = (double) rand() / (double) RAND_MAX;

	exp_rnd = -mean * log(1 - unif_rnd);
	return (exp_rnd);
}

void selectionsort(int *vetor, int tamanho){
	int i,j;
	int aux, min;
	
	for(i=0; i<tamanho-1; i++){
		min = i;
		for(j=i+1; j<tamanho; j++){
			if (vetor[j] < vetor[min]) min=j;
		}
		if (i != min){
			aux = vetor[i];
			vetor[i] = vetor[min];
			vetor[min] = aux;
		}		
	}
}

int main(int argc, char ** argv) {
	int i;
	int cnt;
	srand(time(0));
	cnt = atoi(argv[1]);
	//printf("%lf\n",ExpRnd(10));
	std::string cars[7];
	int vet[cnt];
	cars[0] = "type0\0";
	cars[1] = "type1\0";
	cars[2] = "type2\0";
	cars[3] = "type3\0";
	cars[4] = "type4\0";
	cars[5] = "type5\0";
	cars[6] = "type6\0";
	int depart;
	int c=1,car, t = 0;

	for (i = 0; i < cnt; i++) {
		vet[i] = ((int)ExpRnd(1000) + 1) % 300;
	}

	selectionsort(vet, cnt);

	for (i = 0; i < cnt; i++) {
		
		car = rand() % 7;
		
		printf("<vehicle id=\"%d\" type=\"%s\" route=\"routedist0\" depart=\"%d\" color=\"1,0,0\"/>\n",i, cars[car].c_str(), vet[i] + i);
		
				
		//t += (c % 5) + 1; 

	}
	printf("</routes>\n");	
	
}
	//printf("<vehicle id="%d" type="%s" route="%s" depart="%d" color="%d,%d,%d"/>")
