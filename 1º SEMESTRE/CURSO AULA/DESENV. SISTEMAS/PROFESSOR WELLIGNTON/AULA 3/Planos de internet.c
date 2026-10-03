#include <stdio.h>

int main(){

    int gb_mensal;
    int minutos_lig;
    float plan_a;
    float plan_b;;

    printf("Quantos GB voce usa por mes?");
    scanf("%d", &gb_mensal);
    printf("QQuantos minutos de ligação voce faz?");
    scanf("%d", &minutos_lig);
    printf("\n");
    
    plan_a = 49.9;
    if(gb_mensal > 10){
        plan_a = (49.9 + ((gb_mensal - 10)*1.5));
        if(minutos_lig > 100){
            plan_a = (49.9 + ((gb_mensal-10)*1.5)+((minutos_lig-100)*0.35));
        }
        else{
            plan_a = (49.9 + ((gb_mensal - 10)*1.5));
        }
    }
    else{
        plan_a = 49.9;
    }

    plan_b = 69.9;
    if(gb_mensal > 15){
        plan_b = (49.9 + ((gb_mensal - 15)*0.99));
    }
    else{
        plan_b = 69.9;
    }

    printf("GB por mes:%d\n", gb_mensal);
    printf("Minutos por mes:%d\n", minutos_lig);
    printf("Plano A custa:%f\n", plan_a);
    printf("Plano B custa:%f\n", plan_b);

    if(plan_a > plan_b){
        printf("Plano B é a melhor opção\n");
    }
    else{
        printf("Plano A é a melhor opção\n");
    }



    
return 0;

}