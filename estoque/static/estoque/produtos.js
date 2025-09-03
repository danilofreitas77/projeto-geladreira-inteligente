const botoesAdicionar = document.querySelectorAll('.btnAdicionar');

botoesAdicionar.forEach(botao => {
    botao.addEventListener('click', function() {
        const produtoId = this.dataset.id; // pega o id do produto do data-id
        document.getElementById('produtoId').value = produtoId; // coloca no input hidden do modal
    });
});

const btnConfirmar = document.getElementById('btnConfirmarAdicionar');

btnConfirmar.addEventListener('click', function() {
    const produtoId = document.getElementById('produtoId').value;
    const quantidade = parseint(document.getElementById('quantidadeProduto').value);

    console.log(produtoId, quantidade)
    fetch('/api/carrinho/adicionar/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken') // Django precisa do CSRF token
    },
    body: JSON.stringify({
        produto_id: produtoId,
        quantidade: quantidade
    })
})
.then(response => response.json())
.then(data => {
    if(data.status === 'ok'){
        alert('Produto adicionado ao carrinho!');
        // opcional: atualizar quantidade na tela ou fechar modal
    } else {
        alert(data.msg);
    }
});
});



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
