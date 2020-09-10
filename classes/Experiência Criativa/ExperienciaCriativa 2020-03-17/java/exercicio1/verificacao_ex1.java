import java.io.IOException;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

class Verifica1x {
    public static void main(String[] args) throws IOException, NoSuchAlgorithmException {

        // Limpa a tela
        System.out.print("\033[H\033[2J");
        System.out.flush();

        // Instancia o Scanner
        Scanner scan = new Scanner(System.in);
        System.out.print("Escolha uma opção:\n1: Básico\n2: Encriptado\nDigite a opção: ");
        int option = 0;
        try {
            option = scan.nextInt();
        } catch (Exception e) {
            System.out.println("Opção inválida!");
            System.exit(1);
        }
        switch (option) {
            case 1:
                // Instancia o objeto BasicVerification e chama o método verifica
                new BasicVerification().verifica(scan);
                System.exit(0);
            case 2:
                // Chama o método estático que apresenta o segundo menu
                segundoMenu(scan);
                System.exit(0);
            default:
                System.out.println("Opção inválida!");
                System.exit(1);
        }
    }

    private static void segundoMenu(Scanner scan) throws IOException, NoSuchAlgorithmException {
        // Limpa a tela
        System.out.print("\033[H\033[2J");
        System.out.flush();

        // Lista opções no segundo menu
        System.out.println("Registro 'encriptado' no 'banco de dados'");
        System.out.println("Opção 1: inserir registro novo no banco");
        System.out.println("Opção 2: verificar existência de registro no banco");
        System.out.println("Selecione a opção: ");
        int opcao_segundo_menu = scan.nextInt();
        switch (opcao_segundo_menu) {
            case 1:
                // Chama o método de adição estaticamente
                ElaborateVerification.adicionaAoBanco(scan);
                scan.close();
                System.exit(0);
            case 2:
                // Chama o método de verificação estaticamente
                ElaborateVerification.verificaExistenciaNoBanco(scan);
                scan.close();
                System.exit(0);
            default:
                System.out.println("Opção inválida!");
                System.exit(1);
        }
    }
}