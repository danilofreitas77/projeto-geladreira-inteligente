document.addEventListener("DOMContentLoaded", function() {
    const modal = document.getElementById("modalQuantidade");
    const nomeProdutoSpan = document.getElementById("nomeProduto");
    const estoqueProdutoSpan = document.getElementById("estoqueProduto");
    const quantidadeInput = document.getElementById("quantidadeProduto");
    const confirmarBtn = document.getElementById("confirmarAdd");

    let produtoId = null;
    let estoqueDisponivel = 0;

    // Abrir modal ao clicar no botão de adicionar
    document.querySelectorAll(".btn-adicionar").forEach(btn => {
        btn.addEventListener("click", function() {
            produtoId = this.dataset.id;
            const nomeProduto = this.dataset.nome;
            estoqueDisponivel = parseInt(this.dataset.estoque);

            nomeProdutoSpan.textContent = nomeProduto;
            estoqueProdutoSpan.textContent = estoqueDisponivel;
            quantidadeInput.value = 1;
            quantidadeInput.max = estoqueDisponivel;

            modal.classList.remove("d-none"); // mostra o modal
        });
    });

    // Fechar modal clicando fora
    modal.addEventListener("click", function(e) {
        if (e.target === modal) {
            modal.classList.add("d-none");
        }
    });

    // Fechar modal pelo botão de fechar
    document.querySelector("#modalQuantidade button.btn-secondary").addEventListener("click", function() {
        modal.classList.add("d-none");
    });

    // Apenas teste: mostrar alerta ao clicar em confirmar
    confirmarBtn.addEventListener("click", function() {
        const quantidade = parseInt(quantidadeInput.value);
        if (quantidade > 0 && quantidade <= estoqueDisponivel) {
            alert(`Adicionar ${quantidade} do produto ${nomeProdutoSpan.textContent}`);
            modal.classList.add("d-none");
        } else {
            alert(`Quantidade inválida. Máximo disponível: ${estoqueDisponivel}`);
        }
    });
});
