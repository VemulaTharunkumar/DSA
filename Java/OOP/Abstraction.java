import java.util.Scanner;

abstract class Abstract {
    private double balance;
    Abstract(){

    }
    Abstract(double balance){
        this.balance=balance;
    }
    protected void deposit(double amount){
        balance+=amount;
        System.out.println("Available Balance:"+balance);
    }
    protected void withdrawl(double amount){
        balance-=amount;
        System.out.println("Available Balance:"+balance);
    }
    abstract void pay(double amount);
    void generateReceipt(double balance){
        System.out.println("Receipt generated");
        System.out.println("Present Balance:"+balance);
    }
}
class CreditCardPayment extends Abstract{
    void pay(double amount){
        System.out.println("Payment done by CreditCard -Amount :"+amount);
    }
}
class UPIPayment extends Abstract{
    void pay(double amount){
        System.out.println("Payment done by UPI -Amount :"+amount);
    }
}
class NetBanking extends Abstract{
    void pay(double amount){
        System.out.println("Payment done by NetBanking -Amount :"+amount);
    }
}
public class Abstraction{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        double amount=sc.nextInt();
        Abstract a=new CreditCardPayment();
        a.pay(amount);
        a.deposit(amount);
        a.generateReceipt(amount);
        Abstract a1=new UPIPayment();
        a1.pay(amount);
        a1.deposit(amount);
        a1.generateReceipt(amount);
        Abstract a2=new NetBanking();
        a1.pay(amount);
        a1.deposit(amount);
        a1.generateReceipt(amount);
    }
}
