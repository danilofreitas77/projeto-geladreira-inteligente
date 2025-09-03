console.log("Carrinho.js carregado");

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

    // Confirmar
    confirmarBtn.addEventListener("click", function() {
        const quantidade = parseInt(quantidadeInput.value);

        if (quantidade > 0 && quantidade <= estoqueDisponivel) {
            fetch("/api/carrinho/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: JSON.stringify({
                    item: produtoId,
                    quantidade: quantidade
                })
            })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    alert("✅ Produto adicionado ao carrinho!");
                    modal.classList.add("d-none");
                    location.reload();
                } else {
                    alert("Erro: " + (data.erro || "Falha inesperada"));
                }
            })
            .catch(err => {
                console.error("Erro na requisição:", err);
                alert("Erro inesperado.");
            });
        } else {
            alert(`Quantidade inválida. Máximo disponível: ${estoqueDisponivel}`);
        }
    });
});

// Função helper pro CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
