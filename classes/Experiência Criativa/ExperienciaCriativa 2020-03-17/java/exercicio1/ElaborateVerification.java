import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Formatter;
import java.util.Scanner;
import java.util.stream.Collectors;

class ElaborateVerification {

    // Define o nome do arquivo com as credenciais
    private static final String PATH = "credenciais.txt";

    // Método estático que adiciona um usuário e uma senha ao banco
    public static void adicionaAoBanco(Scanner scan) throws IOException, NoSuchAlgorithmException {

        // Cria o arquivo se ainda não existir
        File file = new File(PATH);
        if (!file.exists()) {
            file.createNewFile();
        }

        // objeto writer - responsável por escrever em um arquivo
        BufferedWriter writer = new BufferedWriter(new FileWriter(PATH, true));

        // Captura de informações
        System.out.print("Digite o usuário a ser inserido no banco: ");
        String user = scan.next();
        System.out.print("Digite a senha: ");
        String pass = scan.next();

        // Conversão da senha em texto para a hash (SHA-1)
        MessageDigest mensagem_sha1 = MessageDigest.getInstance("SHA-1");
        mensagem_sha1.reset();
        mensagem_sha1.update(pass.getBytes("UTF-8"));
        String sha1 = byteToHex(mensagem_sha1.digest());

        // Concatena as informações e uma quebra de linha
        String encoded_string = user + " : " + sha1 + "\n";

        // Escreve no arquivo e fecha o objeto aberto inicialmente
        writer.write(encoded_string);
        writer.close();

        // Notifica a inserção dos dados
        System.out.println("Usuário " + user + " adicionado ao banco!");
    }

    public static void verificaExistenciaNoBanco(Scanner scan) throws IOException, NoSuchAlgorithmException {

        // Instancia o objeto leitor, lê o arquivo e fecha o leitor
        BufferedReader reader = new BufferedReader(new FileReader(PATH));
        String lines = reader.lines().collect(Collectors.joining());
        reader.close();

        // Captura de informações
        System.out.print("Digite o usuário: ");
        String user = scan.next();
        System.out.print("Digite a senha: ");
        String pass = scan.next();

        // Conversão da senha em texto para a hash (SHA-1)
        MessageDigest mensagem_sha1 = MessageDigest.getInstance("SHA-1");
        mensagem_sha1.reset();
        mensagem_sha1.update(pass.getBytes("UTF-8"));
        String sha1 = byteToHex(mensagem_sha1.digest());

        // Concatena as informações e uma quebra de linha
        String encoded_string = user + " : " + sha1;

        // Verifica a existência das credenciais no banco
        if (lines.contains(encoded_string)) {
            System.out.println("Acesso concedido!");
        } else {
            System.out.println("Acesso Negado!");
        }
    }

    // Formatando byte para hexadecimal - StackOverflow
    private static String byteToHex(final byte[] hash) {

        // Instancia um objeto formatador
        Formatter formatter = new Formatter();

        // Formata cada byte na hash
        for (byte b : hash) {
            formatter.format("%02x", b);
        }

        // Atribui o resultado do formatador a uma string através do método toString
        String result = formatter.toString();

        // Fecha o formatador e retorna o resultado
        formatter.close();
        return result;
    }
}