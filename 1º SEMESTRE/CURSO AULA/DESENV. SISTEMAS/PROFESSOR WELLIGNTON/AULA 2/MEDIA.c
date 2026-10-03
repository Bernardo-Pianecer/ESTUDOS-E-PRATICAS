#include <stdio.h>

int main(){


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
    
}
