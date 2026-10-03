#include <stdio.h>

int main(){

    float valor_hora;
    int horas_trab;
    int horas_ext;
    float valor_hext;
    float salario_bruto;
    float desc_inss;
    float desc_vl_transp;
    float salario_liq;

    printf("Qual o valor da hora do seu trabalho?");
    scanf("%f", &valor_hora);
    printf("Quantas horas trabalhadas mensais?");
    scanf("%d", &horas_trab);
    printf("Quantas horas extras voce fez?");
    scanf("%d", &horas_ext);
    printf("\n");
    valor_hext = (valor_hora * 1.5);
    salario_bruto = ((valor_hora * horas_trab) + (horas_ext * valor_hext));
    desc_inss = (salario_bruto * (11/100));
    desc_vl_transp = (salario_bruto * (6/100));
    salario_liq = (salario_bruto - desc_inss - desc_vl_transp);
    printf("\n");
    printf("Valor hora extra: R$%.0f\n", valor_hext);
    printf("Salario bruto: R$%.0f\n", salario_bruto);
    printf("Desconto INSS R$ %.0f\n", desc_inss);
    printf("Desconto VT: R$ %.0f\n", desc_vl_transp);
    printf("Salario liquido: %.0f\n", salario_liq);
    if(salario_liq > 2500){
        printf("Seu salario esta acima da Média\n");
    }
    else{
        printf("Seu salario nao esta acima da media\n");
    }



    
return 0;

}