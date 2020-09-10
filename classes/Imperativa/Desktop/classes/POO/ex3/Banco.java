// 3. Classe Banco
// a. Contém somente o método main,	com	os seguintes passos:
// i. criar três instâncias	de Cliente e três respectivas instâncias de ContaCorrente, devidamente ligadas, com	os seguintes dados:
// 1. Jandira Silva, conta número 84037, saldo inicial R$2.500,00
// 2. Sandra Rodrigues, conta número 70662,	saldo inicial R$1.800,00
// 3. Luciana Teixeira,	conta número 20718,	saldo inicial R$5.000,00
// ii. Imprimir	os dados dos três clientes	criados
// iii. Retirar	R$1.000,00 da conta	de Jandira	Silva
// iv. Imprimir	os dados da	cliente	Jandira	Silva
// v. Retirar R$2.000,00 da	conta de Sandra	Rodrigues
// vi. Depositar R$500,00 na conta de Sandra Rodrigues
// vii. Imprimir os	dados da cliente Sandra	Rodrigues
// viii. Retirar R$2.000,00	da conta de Sandra Rodrigues
// ix. Imprimir	os	dados da cliente Sandra	Rodrigues
// x. Depositar	R$1.000,00 na conta de Luciana Teixeira
// xi. Imprimir	os dados da cliente Luciana	Teixeira

class Banco {
    public static void main(String[] args) {
        // Cliente Jandira Silva
        Cliente jandira = new Cliente("Jandira Silva");
        jandira.ligaContaCorrente(new ContaCorrente(84037, 2500));

        // Cliente Sandra Rodrigues
        Cliente sandra = new Cliente("Sandra Rodrigues");
        sandra.ligaContaCorrente(new ContaCorrente(70662, 1800));

        // Cliente Luciana Teixeira
        Cliente luciana = new Cliente("Luciana Teixeira");
        luciana.ligaContaCorrente(new ContaCorrente(20718, 5000));

        // Imprime os dados das três clientes
        jandira.imprime();
        sandra.imprime();
        luciana.imprime();

        // Retira 1000 da conta da Jandira e imprime os dados atualizados
        jandira.retira(1000);
        jandira.imprime();

        // Sandra: retira 2000, deposita 500, imprime os dados, retira 2000, imprime os dados
        sandra.retira(2000);
        sandra.deposita(500);
        sandra.imprime();
        sandra.retira(2000);
        sandra.imprime();

        // Luciana: Deposita 1000 e imprime seus dados
        luciana.deposita(1000);
        luciana.imprime();

    }
}