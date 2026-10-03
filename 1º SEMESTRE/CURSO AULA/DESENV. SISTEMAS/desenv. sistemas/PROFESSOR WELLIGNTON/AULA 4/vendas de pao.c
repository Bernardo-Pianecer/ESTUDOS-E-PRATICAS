#include <stdio.h>

int main(){

    float pao_prod;
    float preço_unit;
    float qtd_vendida;
    float custo_de_prod;
    float paes_rest;
    float faturamento;
    float custo_total;
    float lucro;
    float porc_venda;

    printf("Quaantos paes foram produzidos?");
    scanf("%f", &pao_prod);
    printf("Qual o preço unitário?");
    scanf("%f", &preço_unit);
    printf("Quantos pães foram vendidos");
    scanf("%f", &qtd_vendida);
    printf("Qual o custo de produção?");
    scanf("%f", &custo_de_prod);
    printf("\n");

    paes_rest = (pao_prod - qtd_vendida );
    faturamento = (qtd_vendida * preço_unit);
    custo_total = (pao_prod * custo_de_prod );
    lucro = (faturamento - custo_total );
    porc_venda = ((qtd_vendida*100)/pao_prod);


    printf("\n");


    printf("Paes produzidos: %f\n", pao_prod);
    printf("Preco unitario (R$):%f\n", preço_unit);
    printf("Paes vendidos: %f\n", qtd_vendida);
    printf("Custo por pao (R$): %f\n", custo_de_prod);
    printf("Paes restantes: %f\n", paes_rest);
    printf("Faturamento: %f\n", faturamento);
    printf("Custo total: %f\n", custo_total);
    printf("Lucro: %f\n", lucro);
    printf("Percentual vendido: %f\n", porc_venda);


    if(lucro > 0){
        printf("Lucro é positivo\n");
    }
    else{
        printf("Nao é Lucro positivo\n");
    }

    
    if(porc_venda >= 80){
        printf("é maior que 80%\n");
    }
    else{
        printf("É menor que 80%\n");
    }

    if(lucro > 0 && porc_venda >= 80){
        printf("Resultado ideal\n");
    }
    else{
        printf("Resultado nao é ideal\n");
    }



    
return 0;

}