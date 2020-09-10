// 2. Classe Cliente
// a. Contém os	seguintes atributos privados:
// i. nome, do tipo String
// ii. conta corrente, do tipo ContaCorrente
// b. Contém os seguintes métodos públicos:
// i. construtor, cujo parâmetro é o nome do cliente
// ii. ligar uma conta corrente (previamente criada) ao	cliente
// iii. depositar um valor (double) na conta do cliente
// iv. retirar um valor (double) da	conta do cliente
// v. imprimir os dados do cliente,	o que inclui o seu	nome e todos os dados da sua conta corrente

class Cliente {
    // Declaração de atributos
    private String nome;
    private ContaCorrente conta_corrente;

    // Construtor
    public Cliente(String nome) {
        this.nome = nome;
    }

    // Método que liga uma ContaCorrente ao Cliente
    public void ligaContaCorrente(ContaCorrente conta) {
        this.conta_corrente = conta;
    }

    // Deposita na conta ligada ao Cliente
    public void deposita(double valor) {
        System.out.println("\n" + this.conta_corrente.deposita(valor, this.nome) + "\n");
    }

    // Retira da conta ligada ao Cliente
    public void retira(double valor) {
        System.out.println("\n" + this.conta_corrente.retira(valor, this.nome) + "\n");
    }

    // Imprime dados do cliente
    public void imprime() {
        System.out.println("\n" + "Nome do Cliente: " + this.nome);
        this.conta_corrente.imprime();
        System.out.println("\n");
    }
}
