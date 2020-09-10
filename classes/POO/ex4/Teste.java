// Deve ser criada uma classe Teste contendo o método main que instancia um objeto de cada classe e chama todos os seus métodos uma vez, ao menos.

class Teste {

    //Método main
    public static void main(String[] args) {

        // -------------------- VINHO -------------------------
        // Instancia objeto vinho
        Vinho vinho = new Vinho("vinho", "Merlot", 99.99, 20, 1992, "Tinto", "Merlot", "França");

        // Marca, preço, quantidade de garrafas no estoque, ano, cor, uva, país
        System.out.println("-----Vinho-----");
        System.out.println("<Características>");
        System.out.println("Marca: " + vinho.getMarca());
        System.out.println("Preço: " + vinho.getPreco());
        System.out.println("Estoque: " + vinho.getEstoque());
        System.out.println("Ano: " + vinho.getAno());
        System.out.println("Cor: " + vinho.getCor());
        System.out.println("Uva: " + vinho.getUva());
        System.out.println("País: " + vinho.getPais());

        // Vender, comprar, atualizar preço

        // Vender
        System.out.println();
        System.out.println("<Venda>");
        System.out.println("Quantidade atual:" + vinho.getEstoque());
        System.out.println("Quantidade a ser vendida: 3");
        vinho.vender(3);
        System.out.println("Quantidade atualizada: " + vinho.getEstoque());

        // Comprar
        System.out.println();
        System.out.println("<Compra>");
        System.out.println("Quantidade atual:" + vinho.getEstoque());
        System.out.println("Quantidade a ser reposta no estoque: 10");
        vinho.comprar(10);
        System.out.println("Quantidade atualizada: " + vinho.getEstoque());

        // Alterar preço
        System.out.println();
        System.out.println("<Alteração de preço>");
        System.out.println("Preço atual:" + vinho.getPreco());
        vinho.atualizarPreco(119.99);
        System.out.println("Preço foi modificado para R$ 119,99...");
        System.out.println("Preço atualizado:" + vinho.getPreco());


        // Organização do output
        System.out.println();
        System.out.println();
        System.out.println();

        // -------------------- CERVEJA --------------------
        // Instancia objeto cerveja
        Cerveja cerveja = new Cerveja("cerveja", "Corona", 11.99, 2020);

        // Marca, preço, quantidade de garrafas no estoque
        System.out.println("-----Cerveja-----");
        System.out.println("<Características>");
        System.out.println("Marca: " + cerveja.getMarca());
        System.out.println("Preço: " + cerveja.getPreco());
        System.out.println("Estoque: " + cerveja.getEstoque());

        // Vender, comprar, atualizar preço

        // Vender
        System.out.println();
        System.out.println("<Venda>");
        System.out.println("Quantidade atual:" + cerveja.getEstoque());
        System.out.println("Quantidade a ser vendida: 3");
        vinho.vender(3);
        System.out.println("Quantidade atualizada: " + cerveja.getEstoque());

        // Comprar
        System.out.println();
        System.out.println("<Compra>");
        System.out.println("Quantidade atual:" + cerveja.getEstoque());
        System.out.println("Quantidade a ser reposta no estoque: 10");
        vinho.comprar(10);
        System.out.println("Quantidade atualizada: " + cerveja.getEstoque());

        // Alterar preço
        System.out.println();
        System.out.println("<Alteração de preço>");
        System.out.println("Preço atual:" + cerveja.getPreco());
        vinho.atualizarPreco(14.99);
        System.out.println("Preço foi modificado para R$ 14,99...");
        System.out.println("Preço atualizado:" + cerveja.getPreco());
    }
}