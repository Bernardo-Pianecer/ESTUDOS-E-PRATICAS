#include <stdio.h>

int main(){

    //soma
    int n1;
    int n2;
    int resultado;
    

    printf("Some dois numeros:");
    scanf("%d", &n1);
    scanf("%d", &n2); 
    resultado = (n1 + n2 );       
    printf("resultado: %d\n", resultado);

    //area
    int base;
    int altura;
    int area;
    

    printf("Fale a base e altura do quadrado respectivamente:");
    scanf("%d", &base);
    scanf("%d", &altura); 
    area = (base * altura );       
    printf("Area: %d\n", area);

    //Media
    float nota1;
    float nota2;
    float nota3;
    float media;

    printf("Digite a primera nota:");
    scanf("%f", &nota1);
    printf("Digite um numero:");
    scanf("%f", &nota2); 
    printf("Digite um numero:");
    scanf("%f", &nota3); 
    
    media = (nota1 + nota2 + nota3)/3;
    
    printf("Média: %.1f\n", media);
    printf("Aprovado? %d\n", media >= 7);

    //Conversor de temperatura
    int celsius;
    int far;
    

    printf("Fale a temperatura:");
    scanf("%d", &celsius);
    far = (celsius * 9/5 + 32 );       
    printf("Far: %d\n", far);

    //troco da compra
    int valor_da_compra;
    int quantia_de_dinheiro;
    int troco;
    
    printf("Quanto foi a compra:");
    scanf("%d", &valor_da_compra);
     printf("Quanto de dinehiro que voce deu:");
    scanf("%d", &quantia_de_dinheiro); 
    troco = (quantia_de_dinheiro - valor_da_compra );       
    printf("troco: %d\n", troco);

    //Salario cortado
    int salario;
    int desc_iss;
    int desc_saude;
    int sal_liq;
    
    printf("Qual o salario bruto:");
    scanf("%d", &salario);
    desc_iss = (salario * 0.11);
    desc_saude = (salario * 0.05);  
    sal_liq = (salario - desc_iss - desc_saude);       
    printf("salario bruto: %d\n", salario);
    printf("desconto iss: %d\n", desc_iss);
    printf("desconto saude: %d\n", desc_saude);
    printf("Salario Liquido: %d\n", sal_liq);

    //Amigos e Gorjeta
    int conta;
    int conta_indv;
    int conta_gorj;

    printf("Qual o valor total da conta:");
    scanf("%d", &conta);
    conta_indv = (conta/3);
    conta_gorj = (conta_indv + conta_indv/10);
    printf("Valor a ser pago por cada Amigo: %d\n", conta_gorj);

    //par ou impar

    int par_ou_impar;
    int resultado;
    

    printf("Digite o numero:");
    scanf("%d", &par_ou_impar);    
    resultado = (n % 2);
    printf("Par ou Impar: %d\n", resultado);

    //Media de consumo
    int area_percorrida;
    int consumo;
    int media;
    

    printf("Quando voce percorreu:");
    scanf("%d", &area_percorrida);
    printf("Quanto seu carro consumiu:");
    scanf("%d", &consumo); 
    media = (area_percorrida / consumo );       
    printf("media: %d\n", media);


    return 0;    
}