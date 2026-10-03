const visor = document.querySelector('.inputTela');

function digitar(caractere){
    if (visor.value === "0 ") {
        visor.value = caractere;
    }else{
        visor.value = visor.value + caractere;
    }
}
function limpar() {
    visor.value = "";
}
function apagar() {
    visor.value = visor.value.slice(0, -1);
}
function resultado() {
    try {
        visor.value = eval(visor.value);
    } catch (e) {
        visor.value = "ERRO";
    }
}