console.log("validateForm.js carregado");

function validateForm() {
    // Definindo os limites de validação
    const limits = {
        income: [1730.0, 666666.0],
        recency: [0.0, 99.0],
        num_deals_purchases: [0.0, 15.0],
        num_web_purchases: [0.0, 27.0],
        num_catalog_purchases: [0.0, 28.0],
        num_store_purchases: [0.0, 13.0],
        num_web_visits_month: [0.0, 20.0],
        response: [0.0, 1.0]
    };

    // Definindo os nomes dos campos
    const fieldNames = {
        income: "Orçamento Anual",
        recency: "Número de dias da última compra",
        num_deals_purchases: "Número de compras feitas com desconto",
        num_web_purchases: "Número de compras no site",
        num_catalog_purchases: "Número de compras em catálogo",
        num_store_purchases: "Número de compras na loja física",
        num_web_visits_month: "Número de visitas no site",
        response: "Resposta na ultima campanha"
    };

    // Obtendo os valores dos campos
    for (const field in limits) {
        const input = document.getElementById(field);
        const value = Number(input.value);
        const [min, max] = limits[field];
        
        console.log(`Validando ${field}: valor=${value}, min=${min}, max=${max}`); // Adicione este log

        if (isNaN(value) || value < min || value > max) {
            alert(`O valor para "${fieldNames[field]}" deve estar entre ${min} e ${max}.`);
            return false; // Impede o envio do formulário
        }
    }
    return true; // Permite o envio do formulário se todos os valores forem válidos
}
