class Course {
    String name;
    String hour;
    String teacher;
    int classroom;


    public Course (String name,String hour,String teacher,int classroom){
    this.name = name;
    this.hour = hour;
    this.teacher = teacher;
    this.classroom = classroom;
    }

    public String unavailable_classroom (String name, classroom) {
        return "Aula: "+name+"  Enseñando: "+subject;
    }

    public static void show_info(String name,String hour,String teacher,int classroom){
        System.out.println("Nombre de la materia: "+name);
        System.out.println("Horario: "+hour);
        System.out.println("Profesor: "+teacher);
        System.out.println("Salon: "+classroom);
    }
    
    public void welcome_message(){
        System.out.println("Bienvenido al sistema de materias");
    }

    public int classroom_reserved(int classroom){
        return "Aula: "+classroom;
    }

}
