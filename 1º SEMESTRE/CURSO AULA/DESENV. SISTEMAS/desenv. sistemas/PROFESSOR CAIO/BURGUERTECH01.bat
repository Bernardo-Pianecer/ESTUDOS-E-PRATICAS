@echo off

echo BURGUER TECH
color 29
set "pasta_saida=SA1_BURGUER_TECH\pasta_saida"
if not exist "%pasta_saida%" md "%pasta_saida%"

set /p nome=Nome do cliente: 

:: Tabela de Preços
set /a v_xBurguer=20
set /a v_xSalada=17
set /a v_xBacon=22
set /a v_combo=30
set /a v_coca=12
set /a v_suco=8
set /a v_guarana=10
:hamburguer
CLS

echo ===================================
echo ------ CATALOGO de HAMBURGUER ------
echo ===================================
echo [1] X-burguer                  R$ %v_xBurguer%
echo [2] X-Salada                   R$ %v_xSalada%
echo [3] X-Bacon                    R$ %v_xBacon%
echo [5] Combo (X-burguer + Bebida) R$ %v_combo%
echo ===================================

set /p codH=Qual o hamburguer que voce vai querer?

if "%codH%"=="1" set nomeHamb=X-Burguer& set /a precoH=%v_xBurguer%
if "%codH%"=="2" set nomeHamb=X-Salada& set /a precoH=%v_xSalada%
if "%codH%"=="3" set nomeHamb=X-Bacon& set /a precoH=%v_xBacon%
if "%codH%"=="5" set nomeHamb=COMBO& set /a precoH=%v_combo%

CLS
echo ===================================
echo ------ CATALOGO de BEBIDAS --------
echo ===================================
echo [6] Coca Cola                  R$ %v_coca%
echo [7] Suco Natural               R$ %v_suco%
echo [8] Guarana                    R$ %v_guarana%
echo ===================================
set /p codB=Qual bebida que voce vai querer?

if "%codB%"=="6" set nomeBeb=Coca-Cola& set /a precoB=%v_coca%
if "%codB%"=="7" set nomeBeb=Suco Natural& set /a precoB=%v_suco%
if "%codB%"=="8" set nomeBeb=Guarana& set /a precoB=%v_guarana%


:: Cálculo Final e Verificação
set /a total = %precoH% + %precoB%
set "arquivo=%pasta_saida%\nota_%nome%.txt"


CLS
echo ================================
echo          RESUMO DO PEDIDO
echo ================================
echo Cliente: %nome%
echo Hamburguer: %nomeHamb% --- R$ %precoH%
echo Bebida:     %nomeBeb% --- R$ %precoB%
echo --------------------------------
echo TOTAL A PAGAR: R$ %total%
echo ================================
echo [1]sim
echo [2]nao
set /p verify=O pedido esta certo?
if %verify%==2 goto hamburguer
echo ================================>"%arquivo%"
echo          NOTA FISCAL            >>"%arquivo%"
echo ================================>>"%arquivo%"
echo Cliente: %nome%                 >>"%arquivo%"
echo Hamburguer: %nomeHamb% --- R$ %precoH%>>"%arquivo%"
echo Bebida:     %nomeBeb%  --- R$ %precoB%>>"%arquivo%"
echo -------------------------------->>"%arquivo%"
echo TOTAL A PAGAR: R$ %total%       >>"%arquivo%"
echo ================================>>"%arquivo%"
START %arquivo%