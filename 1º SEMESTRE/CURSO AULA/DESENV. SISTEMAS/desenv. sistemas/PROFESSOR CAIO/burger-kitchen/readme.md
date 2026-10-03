# 🍔 Burger Tech — Monitor da Cozinha (KDS)

O **Burger Tech KDS (Kitchen Display System)** é um sistema de monitoramento de cozinha industrial desenvolvido para otimizar o fluxo de preparação de pedidos em restaurantes. O projeto simula a integração entre um Totem de autoatendimento (onde os pedidos são gerados através de menus interativos) e a equipe da cozinha (que visualiza, inicia o preparo e dá baixa nos pedidos concluídos).

Este projeto marca o encerramento da Unidade Curricular de **Lógica de Programação e Sistemas Web**.

---

## 🚀 Funcionalidades

* **Simulador de Totem Integrado:** Seleção de produtos (Hambúrguer, Acompanhamento e Bebida) usando caixas de listagem estruturadas (`<select>`).
* **Aviso Sonoro Automatizado:** Emissão de um alerta em áudio (Bip de cozinha) em tempo real assim que um novo pedido é enviado pelo Totem.
* **Gerenciamento Dinâmico de Estados:** Alteração visual dos cards de acordo com o status atual do pedido:
    * 🟡 **Pendente:** Pedido aguardando na fila (Borda laranja).
    * 🟢 **Preparando:** Chapeiro iniciou a produção (Borda verde).
    * 🔴 **Finalizado:** Pedido concluído (é removido automaticamente da tela para não sobrecarregar o monitor).
* **Contador em Tempo Real:** Monitoramento no topo do painel indicando quantos pedidos ainda estão pendentes.
* **Carregamento de Dados Iniciais:** O sistema já inicia com pedidos simulados na memória para testes imediatos.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as três tecnologias pilares do desenvolvimento Web Front-End, sem o uso de frameworks externos:

1.  **HTML5:** Estruturação semântica do painel de controle e formulários de seleção.
2.  **CSS3:** Estilização moderna em *Dark Mode*, uso de **CSS Grid Layout** para responsividade dos cards e **Flexbox** para alinhamentos internos.
3.  **JavaScript (ES6):** Inteligência do sistema, manipulação de Array de Objetos (banco de dados simulado), escutadores de eventos (`onclick`), métodos de array (`forEach`, `find`, `filter`) e manipulação dinâmica de elementos no DOM (`createElement`).

---

## 📂 Estrutura de Arquivos

```text
burger-kitchen/
├── index.html     # Estrutura e marcação da página
├── style.css      # Design, cores e layout em Grid
├── script.js      # Lógica de negócio e manipulação do DOM
└── README.md      # Documentação do projeto