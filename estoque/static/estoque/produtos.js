console.log('produtos.js carregado');

document.addEventListener('DOMContentLoaded', function() {
    console.log('produtos.js carregado');

    // --- ADICIONAR ---
    const botoesAdicionar = document.querySelectorAll('.btnAdicionar');
    botoesAdicionar.forEach(botao => {
        botao.addEventListener('click', function() {
            const produtoId = this.dataset.id;
            const inputProduto = document.getElementById('produtoId');
            if(inputProduto) inputProduto.value = produtoId;
        });
    });

    const btnConfirmar = document.getElementById('btnConfirmarAdicionar');
    if(btnConfirmar){
        btnConfirmar.addEventListener('click', function() {
            const produtoIdEl = document.getElementById('produtoId');
            const quantidadeEl = document.getElementById('quantidadeProduto');
            if(!produtoIdEl || !quantidadeEl) return;

            const produtoId = produtoIdEl.value;
            const quantidade = parseInt(quantidadeEl.value, 10) || 1;

            fetch('/compras/api/carrinho/adicionar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ produto_id: produtoId, quantidade: quantidade })
            })
            .then(res => res.json())
            .then(data => {
                if(data.status === 'ok'){
                    alert('Produto adicionado ao carrinho!');
                    const modalEl = document.getElementById('modalProduto');
                    if(modalEl){
                        const modal = bootstrap.Modal.getOrCreateInstance(modalEl);
                        modal.hide();
                    }

                    // Atualiza quantidade no DOM, se houver
                    const quantidadeElemento = document.querySelector(`.quantidade-produto[data-id='${produtoId}']`);
                    if(quantidadeElemento){
                        quantidadeElemento.textContent = "Qtd: " + data.quantidade;
                        quantidadeElemento.dataset.quantidade = data.quantidade;
                    }
                } else {
                    alert(data.msg);
                }
            });
        });
    }

    // --- REMOVER (EVENT DELEGATION) ---
    const tabela = document.querySelector('table');
    if(tabela){
        tabela.addEventListener('click', function(e){
            if(e.target && e.target.classList.contains('btnRemover')){
                const btn = e.target;
                const produtoId = btn.dataset.id;

                fetch('/compras/api/carrinho/remover/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({ produto_id: produtoId })
                })
                .then(res => res.json())
                .then(data => {
                    if(data.status === 'ok'){
                        // Remove a linha da tabela
                        const linha = btn.closest('tr');
                        if(linha) linha.remove();
                    } else {
                        alert(data.msg);
                    }
                });
            }
        });
    }

    // --- FUNÇÃO COOKIE ---
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
