#include <stdio.h>

int main(){

    int dist_total;
    float preço_gasolina;
    int consumo_medio;
    float litros_nesc;
    float custo_total_comb;
    float custo_pedagio;
    float custo_total_viagem;
    float custo_p_pessoa;

    printf("Qual a distancia total ida e volta da viagem?");
    scanf("%d", &dist_total);
    printf("Qual o preço da gasolina?");
    scanf("%f", &preço_gasolina);
    printf("Qual o consumo médio do seu carro?");
    scanf("%d", &consumo_medio);
    printf("\n");
    litros_nesc = (dist_total / consumo_medio);
    custo_total_comb = (litros_nesc * preço_gasolina);
    custo_pedagio = 45.8;
    custo_total_viagem = (custo_total_comb + custo_pedagio);
    custo_p_pessoa = (custo_total_viagem/4);
    printf("\n");
    printf("Distancia total (km):%d\n", dist_total);
    printf("Preco do litro (R$):%f\n",preço_gasolina);
    printf("Consumo do carro (km/l):%d\n", consumo_medio);
    printf("Litros necessarios:%f\n", litros_nesc);
    printf("Custo combustivel:%f\n", custo_total_comb);
    printf("Custo pedagio:%f\n", custo_pedagio);
    printf("Custo total:%f\n", custo_total_viagem);
    printf("Custo por pessoa:%f\n", custo_p_pessoa);
    if(custo_p_pessoa < 100){
        printf("Cabe no Orçamento\n");
    }
    else{
        printf("Não Cabe no orçamento\n");
    }



    
return 0;

}