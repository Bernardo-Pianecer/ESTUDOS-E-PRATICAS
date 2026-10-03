#include <stdio.h>

int main(){

    char nome [50];
    int idade;
    char nome_produto1[50];
    float produto1;
    char nome_produto2[50];
    float produto2;
    char nome_produto3[50];
    float produto3;
    float total_inteiro;
    const float desconto = 0.10;
    double valor_do_desconto;
    float total_final;

    printf("Nome do cliente:");
    scanf("%s",nome);
    printf("Idade do cliente:");
    scanf("%d", &idade);

    printf("Nome do Primeiro produto:");
    scanf("%s", nome_produto1);
    printf("Valor %s:",nome_produto1);
    scanf("%f", &produto1);

    printf("Nome do Segundo produto:");
    scanf("%s", nome_produto2);
    printf("Valor %s:",nome_produto2);
    scanf("%f", &produto2);

    printf("Nome do Terceiro produto:");
    scanf("%s", nome_produto3);
    printf("Valor %s",nome_produto3);
    scanf("%f", &produto3);


    total_inteiro = (produto1 + produto2 + produto3);
    valor_do_desconto = (total_inteiro * desconto);
    total_final = (total_inteiro - valor_do_desconto);

    printf("================================\n");
    printf("   CUPOM FISCAL - LOJA SENAI    \n");
    printf("================================\n");
    printf("Cliente: %s\n", nome);
    printf("Idade: %d\n", idade);
    printf("--------------------------------\n");
    printf("%s:", nome_produto1);
    printf("R$   %0.f\n", produto1);
    printf("%s:", nome_produto2);
    printf("R$   %0.f\n", produto2);
    printf("%s:", nome_produto3);
    printf("R$   %0.f\n", produto3);

    printf("--------------------------------\n");

    printf("Subtotal:           R$  %0.f\n", total_inteiro);
    printf("Desconto (10%):   - R$  %0.lf\n", valor_do_desconto);

    printf("================================\n");
    printf("TOTAL:              R$  %0.f\n", total_final);
    printf("================================\n");







    
return 0;

}