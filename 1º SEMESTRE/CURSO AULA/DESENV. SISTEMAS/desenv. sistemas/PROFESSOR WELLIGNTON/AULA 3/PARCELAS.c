#include <stdio.h>

int main(){

    float valor_do_produto;
    int num_parcela;
    float tx_mensal;
    float lim_mensal;
    float total_juros;
    float valor_final;
    float valor_parcela;

    printf("Qual o valor do produto?");
    scanf("%f", &valor_do_produto);
    printf("Quantas parcelas?");
    scanf("%d", &num_parcela);
    printf("Quantas a taxa de juros mensal?");
    scanf("%f", &tx_mensal);
    printf("Quantas o limite mensal?");
    scanf("%f", &lim_mensal);
    printf("\n");
    total_juros = (valor_do_produto * (tx_mensal/100)*num_parcela);
    valor_final = (valor_do_produto + total_juros);
    valor_parcela = (valor_final / num_parcela );
    printf("\n");


    printf("Valor do produto: R$%f\n", valor_do_produto);
    printf("Numero de parcelas:: R$%c\n", num_parcela);
    printf("Taxa de juros mensal (%): %f\n", tx_mensal);
    printf("Limite mensal (R$): %f\n", lim_mensal);
    printf("Total de juros: %f\n", total_juros);
    printf("Valor final: %f\n", valor_final);
    printf("Valor da parcela: %f\n", valor_parcela);


    if(valor_parcela <= lim_mensal){
        printf("Cabe no orçamento\n");
    }
    else{
        printf("Nao cabe no orçamento\n");
    }

    
    if(total_juros > valor_do_produto * 30 / 100){
        printf("é maior que 30%\n");
    }
    else{
        printf("É menor que 30%\n");
    }



    
return 0;

}