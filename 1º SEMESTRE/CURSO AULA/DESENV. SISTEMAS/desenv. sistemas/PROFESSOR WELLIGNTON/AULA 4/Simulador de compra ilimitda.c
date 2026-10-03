#include <stdio.h>

int main(){

    char nome[50];
    int idade;

    int quantidade;

    char nome_produtos[100][50];
    float valores[100];

    float total = 0;
    const float desconto = 0.10;
    float valor_desconto, total_final;

    printf("Nome do cliente: ");
    scanf("%s", nome);

    printf("Idade do cliente: ");
    scanf("%d", &idade);

    printf("Quantos produtos deseja adicionar? ");
    scanf("%d", &quantidade);

    // Entrada de dados
    for(int i = 0; i < quantidade; i++){
        printf("\nProduto %d\n", i + 1);

        printf("Nome: ");
        scanf("%s", nome_produtos[i]);

        printf("Valor: ");
        scanf("%f", &valores[i]);

        total += valores[i];
    }

    // Cálculos
    valor_desconto = total * desconto;
    total_final = total - valor_desconto;

    // Saída
    printf("\n================================\n");
    printf("   CUPOM FISCAL - LOJA SENAI    \n");
    printf("================================\n");
    printf("Cliente: %s\n", nome);
    printf("Idade: %d\n", idade);
    printf("--------------------------------\n");

    for(int i = 0; i < quantidade; i++){
        printf("%s: R$ %.2f\n", nome_produtos[i], valores[i]);
    }

    printf("--------------------------------\n");
    printf("Subtotal:        R$ %.2f\n", total);
    printf("Desconto (10%): -R$ %.2f\n", valor_desconto);
    printf("================================\n");
    printf("TOTAL:           R$ %.2f\n", total_final);
    printf("================================\n");

    return 0;
}