public class IBGE {
    public static void main(String args[]) {
        Municipio curitiba = new Municipio(3000, 500);
        Municipio guarapuava = new Municipio(400, 100);
        Municipio londrina = new Municipio(600, 400);
        Estado parana = new Estado(curitiba, guarapuava, londrina);
        Municipio salvador = new Municipio(2500, 400);
        Municipio juazeiro = new Municipio(400, 100);
        Municipio ilheus = new Municipio(300, 300);
        Estado bahia = new Estado(salvador, juazeiro, ilheus);
        System.out.println(curitiba.populacao());
        System.out.println(parana.area());
        System.out.println(curitiba.densidade());
        System.out.println(parana.densidade());
        System.out.println(bahia.densidade());
    }
}