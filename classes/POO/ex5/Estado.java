import java.util.ArrayList;

public class Estado {

    private ArrayList<Municipio> municipios = new ArrayList<Municipio>();

    public Estado(Municipio... lista_municipios) {  
        for (Municipio municipio : lista_municipios) {
            this.municipios.add(municipio);
        }
    }

    public void incluir(Municipio municipio) {
        this.municipios.add(municipio);
    }

    public int populacao() {
        int local = 0;
        for (Municipio mun : this.municipios) {
            local = local + mun.populacao();
        }
        return local;
    }

    public double area() {
        double local = 0;
        for (Municipio mun : this.municipios) {
            local = local + mun.area();
        }
        return local;
    }

    public double densidade() {
        return populacao() / area();
    }
}