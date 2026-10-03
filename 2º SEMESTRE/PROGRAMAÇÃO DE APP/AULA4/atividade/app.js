document.getElementById("nomeLoja").textContent = "Loja Senai"

function testar(){
    const mensagem = document.getElementById("mensagem");
    mensagem.textContent = "JavaScript conectado!";
    mensagem.classList.remove("escondido")

    console.log("JavaScript conectado!")
}

function calcular(){
    let qtd1 = document.getElementById("qtd1");
    console.log("qtd1 value = "+ qtd1.value)
    console.log("typeof antigo do qtde1 = "+ typeof qtd1.value)

    const qtd1n = Number(document.getElementById("qtd1").value);

    const qtd2 = Number(document.getElementById("qtd2").value);
    const qtd3 = Number(document.getElementById("qtd3").value);

    console.log("qtd1 value = "+ qtd1n)
    console.log("typeof antigo do qtde1 = "+ typeof qtd1n)

    console.log("qtd2 value = "+ qtd2)
    console.log("typeof antigo do qtde2 = "+ typeof qtd2)

    console.log("qtd3 value = "+ qtd3)
    console.log("typeof antigo do qtde3 = "+ typeof qtd3)


    const notebook_preco = Number(document.getElementById("notebook_preco").value);
    const subtotal_notebook_preco = notebook_preco * qtd1n;
    document.getElementById("sub1").textContent = subtotal_notebook_preco.toFixed(2)
    console.log(subtotal_notebook_preco)
}