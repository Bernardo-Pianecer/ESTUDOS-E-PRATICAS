// 1. MAPEAMENTO DO HTML (Usando Seletores do CSS)
const containerPedidos = document.querySelector("#container-pedidos");
const contadorPedidos = document.querySelector("#contador-pedidos");
const selectLanche = document.querySelector("#select-lanche");
const selectAcompanha = document.querySelector("#select-acompanhamento");
const selectBebida = document.querySelector("#select-bebida");
const somNotificacao = document.querySelector("#som-notificacao");

// 2. BANCO DE DADOS SIMULADO (Lista de Pedidos)
let pedidos = [
    
];
let proximoId = 103;

// 3. FUNÇÃO QUE DESENHA OS CARDS NA TELA
function renderizarPainel() {
    containerPedidos.innerHTML = ""; // Limpa a tela antes de desenhar
    let pendentes = 0;

    // Percorre a lista para criar os cartões na tela
    pedidos.forEach((pedido, posicao) => {
        
        // Se o pedido já foi finalizado, ele some do painel da cozinha
        if (pedido.status !== "finalizado") {
            pendentes++;

            // Define o texto do botão baseado no estado do pedido
            let textoBotao = "👨‍🍳 INICIAR PREPARO";
            if (pedido.status === "preparando") {
                textoBotao = "✅ CONCLUIR PEDIDO";
            }

            // Adiciona o HTML do card na tela de forma dinâmica
            containerPedidos.innerHTML += `
                <div class="card-pedido ${pedido.status}">
                    <div class="card-header">
                        <span>PEDIDO #${pedido.id}</span>
                        <span>⏱️ ${pedido.horario}</span>
                    </div>
                    <ul class="itens-pedido">
                        <li>📌 ${pedido.itens.join("</li><li>📌 ")}</li>
                    </ul>
                    <button class="btn-status" onclick="avancarPedido(${posicao})">
                        ${textoBotao}
                    </button>
                </div>
            `;
        }
    });

    // Atualiza o contador lá no topo
    contadorPedidos.innerText = `Pedidos Pendentes: ${pendentes}`;
}

// 4. FUNÇÃO QUE ALTERA O STATUS DO PEDIDO
function avancarPedido(posicao) {
    let pedidoClicado = pedidos[posicao];

    if (pedidoClicado.status === "pendente") {
        pedidoClicado.status = "preparando";
    } else if (pedidoClicado.status === "preparando") {
        pedidoClicado.status = "finalizado";
    }

    renderizarPainel(); // Redesenha a tela atualizada
}

// 5. FUNÇÃO QUE RECEBE O PEDIDO DO TOTEM
function criarPedidoDoTotem() {
    // Captura os valores selecionados usando nossas variáveis curtas
    const lanche = selectLanche.value;
    const acompanha = selectAcompanha.value;
    const bebida = selectBebida.value;

    // Validação: não deixa enviar se tudo estiver vazio
    if (lanche === "" && acompanha === "" && bebida === "") {
        alert("Escolha pelo menos um produto!");
        return;
    }

    // Pega o horário atual do computador
    const agora = new Date();
    const hora = String(agora.getHours()).padStart(2, '0') + ":" + String(agora.getMinutes()).padStart(2, '0');

    // Junta as escolhas em uma lista descartando o que ficou em branco
    let listaItens = [lanche, acompanha, bebida].filter(item => item !== "");

    // Cria o novo objeto do pedido
    let novoPedido = {
        id: proximoId,
        horario: hora,
        itens: listaItens,
        status: "pendente"
    };

    pedidos.push(novoPedido); // Guarda na nossa lista
    proximoId++; // Soma 1 para o próximo número de pedido

    somNotificacao.play(); // Toca o som de "Bip" utilizando a variável

    // Limpa os seletores da tela voltando para a opção padrão
    selectLanche.value = "";
    selectAcompanha.value = "";
    selectBebida.value = "";

    renderizarPainel(); // Mostra o novo card na tela
}

// Executa o sistema pela primeira vez ao carregar a página
renderizarPainel();