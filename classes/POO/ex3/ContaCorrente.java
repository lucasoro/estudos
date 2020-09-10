// 1. Classe ContaCorrente
// a. Contém os	seguintes atributos	privados:
// i. numero, do tipo int
// ii. saldo, do tipo double
// b. Contém os	seguintes métodos públicos:
// i. construtor, cujos	parâmetros são o número e o saldo inicial da conta corrente
// ii. depositar um	valor (double) na conta
// iii. retirar um	valor (double) da conta, desde que o saldo seja suficiente
// iv. imprimir todos os dados da conta corrente
// c. Possui a seguinte invariante: o saldo	nunca é	negativo.

class ContaCorrente {

    // Declaração de atributos
    private int numero;
    private double saldo;

    // Construtor
    public ContaCorrente(int numero, double saldo) {
        this.numero = numero;
        this.saldo = saldo;
    }

    // Deposita na conta
    public String deposita(double valor, String cliente) {
        if (valor > 0) {
            this.saldo += valor;
            return "Saldo atualizado de " + cliente + ": " + this.saldo;
        }
        return "Valor inválido! Insira um valor positivo.";
    }

    // Saca um valor da conta
    public String retira(double valor, String cliente) {
        if (this.saldo > valor) {
            this.saldo -= valor;
            return "Saldo atualizado de " + cliente + ": "+ this.saldo;
        }
        return "Valor inválido! Insira um valor positivo.";
    }

    // Imprime dados da conta
    public void imprime() {
        System.out.println("Número da Conta: " + this.numero);
        System.out.println("Saldo Disponível: " + this.saldo);

    }
}