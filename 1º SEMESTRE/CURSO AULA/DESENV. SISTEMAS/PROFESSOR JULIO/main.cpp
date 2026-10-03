#include <stdio.h>

int main()
{

    int senha = 1234;
    int tentativa;
    
    printf("Digite Senha: ");
    scanf("%d", &tentativa );
    
    if (tentativa == senha) {
        printf("Acesso Permitido\n");
    }
    else{
        printf("Acesso Negado\n");
    }
    
return 0;
}
