public class Main {
	
    public static void Main(String[] args) {
	    Course c1 = new Course ("OPP", "19:00-20:40", "Luis Guerra",5202);
        Course c2 = new Course ("Bases de Datos", "20:40-10:10", "Silvia Barrera",3205);
		
        welcome_message();
        System.out.println("Materias dadas de alta: ");
        c1.show_info();
        c2.show_info();
        classroom_reserved();

    }

}
