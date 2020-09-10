import java.util.Scanner;

class BasicVerification {
    
    // Incializa atributos
    private String USER;
    private String PASSWD;
    
    // Método construtor
    public BasicVerification() {
        this.USER = "puc";
        this.PASSWD = "senha";
    }

    // Método de verificação
	public void verifica(Scanner scan) {
        // Leitura do input - usuário e senha
        System.out.print("Digite o usuário: ");
        String user_input = scan.next();
        System.out.print("Digite a senha: ");
        String pass_input = scan.next();

        // Verificação das informações
        if(user_input.equals(this.USER) && pass_input.equals(this.PASSWD)) {
            System.out.println("Acesso concedido!");
        } else {
            System.out.println("Acesso negado!");
        }
	}
}