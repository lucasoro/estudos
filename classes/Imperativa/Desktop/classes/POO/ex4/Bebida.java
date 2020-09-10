
class Bebida {

    // Atributos comuns entre o vinho e a cerveja 
    protected String marca;
    protected Double preco;
    protected int estoque;

    // Métodos de venda, compra e atualiação de preços
    protected void vender(int qtde) {
        this.estoque = this.estoque - qtde;
    }

    protected void comprar(int qtde) {
        this.estoque = this.estoque + qtde;
    }

    protected void atualizarPreco(Double preco_novo) {
        this.preco = preco_novo;
    }

    // Getters dos atributos comuns
    protected String getMarca() {
        return this.marca;
    }

    protected Double getPreco() {
        return this.preco;
    }

    protected int getEstoque() {
        return this.estoque;
    }

}