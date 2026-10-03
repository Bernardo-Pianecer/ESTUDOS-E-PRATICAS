#include <stdio.h>

int main(){


    int n;
    int par;
    

    printf("Digite o numero:");
    scanf("%d", &n);    
    par = (n % 2);
    printf("Par ou Impar: %d\n", par);

    

    return 0;    
}
