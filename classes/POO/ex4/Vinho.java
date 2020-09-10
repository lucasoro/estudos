class Vinho extends Bebida {

    // Atributos específicos do vinho
    private int ano;
    private String cor;
    private String uva;
    private String pais;

    // Construtor
    public Vinho(String marca, Double preco, int estoque, int ano, String cor, String uva, String pais) {
        this.marca = marca;
        this.preco = preco;
        this.estoque = estoque;
        this.ano = ano;
        this.cor = cor;
        this.uva = uva;
        this.pais = pais;
    }

    // Getters
    
    public int getAno() {
        return this.ano;
    }

    public String getCor() {
        return this.cor;
    }

    public String getUva() {
        return this.uva;
    }

    public String getPais() {
        return this.pais;
    }
}