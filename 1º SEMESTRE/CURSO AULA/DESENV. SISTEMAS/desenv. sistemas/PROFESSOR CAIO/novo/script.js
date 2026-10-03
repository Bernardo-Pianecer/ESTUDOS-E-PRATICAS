let clienteNome = "";
let lancheEscolhido = "";
let valorLanche = 0;


let telaLogin = document.querySelector('#tela-login');
let telaCardapio = document.querySelector('#tela_cardapaio');
let inputCliente = document.querySelector('#nomeCliente');
let spanNome = document.querySelector('#span-nome');
let telaCombo = document.querySelector('#tela-combo');
let resNome = document.querySelector('#res-nome');
let resItem = document.querySelector('#res-item');
let resTotal = document.querySelector('#res-total');
let telaFinal = document.querySelector('#tela-final');

function irParaCardapio() {

    clienteNome = inputCliente.value;

    if(clienteNome == ""){
        alert("DIGITE SEU NOME PRIMEIRO")
        return;
    }
    spanNome.innerText = clienteNome;
    telaLogin.style.display = "none";
    telaCardapio.style.display = "";
}

function selecionarLanche(nome, preço) {
    lancheEscolhido = nome;
    valorLanche = preço;

    telaCardapio.style.display = "none"
    telaCombo.style.display = ""

}
function finalizar(querCombo) {
    let total = valorLanche;
    let itemFinal = lancheEscolhido;

    if (querCombo) {
        total = (valorLanche + 10) - 2;
        itemFinal += "+ COMBO";
    }

    resNome.innerText = "CLIENTE: " +clienteNome;
    resItem.innerText = "PEDIDO: " + itemFinal;
    resTotal.innerText = "TOTAL: R$" + total.toFixed(2);

    telaCombo.style.display = "none"
    telaFinal.style.display = ""
}
function reiniciar(){
    location.reload();
}