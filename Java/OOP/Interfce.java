interface Wheels{
    void count();
}
class BMW implements Wheels{
    public void count(){
        System.out.println("BMW:"+"Its a two wheeler");
    }
}
class Audi implements Wheels{
    public void count(){
        System.out.println("Audi:"+"Its a four wheeler");
    }
}
class Toyota implements Wheels{
    public void count(){
        System.out.println("Toyota:"+"Its a fourwheeler");
    }
}
public class Interfce{
    public static void main(String args[]){
    Wheels w=new BMW();
    w.count();
    Wheels w1=new Audi();
    w.count();
    Wheels w3=new Toyota();
    w.count();
    }
}
