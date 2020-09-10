import java.util.*;

class ArraySorter{

    // Declaração do Método Main - Construtor
    public static void main(String[] args) {
        
        // Declaração de variáveis e instanciação do objeto Scanner
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o tamanho do array: ");
        int tamanho = scanner.nextInt();
        int[] arr = new int[tamanho];

        // Loop que insere os valores no array
        for(int i = 0; i < tamanho; i++) {
            System.out.println("Digite o valor da posição " + i + ": ");
            arr[i] = scanner.nextInt();
        }

        // Fechando o scanner
        scanner.close();

        // Chamada do método de ordenação
        arr = ordenaArray(arr);

        // Imprime o resultado utilizando o método toString()
        System.out.println(Arrays.toString(arr));
    }

    // Declaração do método de ordenação
    private static int[] ordenaArray(int[] arr) {
        
        // Criação de variáveis locais
        int temp = 0;

        // Ordenação - Nested loops, Brute force:
        for(int j = 0; j < arr.length; j++) {
            for(int k = 0; k < arr.length; k++) {
                if(arr[j] < arr[k]) {
                    temp = arr[k];
                    arr[k] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        
        // Retorna o array final
        return arr;
    }
}