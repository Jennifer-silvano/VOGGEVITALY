document.addEventListener("DOMContentLoaded", function() {
    // Adicione um evento de clique ao botão Adicionar ao Carrinho
    document.getElementById("add-to-cart-form").addEventListener("submit", function(event) {
        event.preventDefault();  // Impede o envio do formulário padrão

        // Obtenha o ID do produto do campo oculto
        var produtoId = document.getElementById("produto_id").value;

        // Envie uma solicitação POST para o servidor
        fetch("/adicionar_carrinho/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")  // Obtenha o token CSRF
            },
            body: JSON.stringify({
                produto_id: produtoId
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Erro ao adicionar ao carrinho");
            }
            // Se tudo estiver OK, redirecione para a página do carrinho
            window.location.href = "/carrinho/";
        })
        .catch(error => {
            console.error("Erro:", error);
        });
    });
});

// Função para obter o token CSRF
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Se o nome do cookie corresponder, obtenha o valor do cookie
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
