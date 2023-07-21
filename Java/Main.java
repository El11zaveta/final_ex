public class Main {
    public static void main(String[] args) {
        ToyStore toyStore = new ToyStore();

        toyStore.addNewToy(new Toy(1, "Teddy bear", 10, 10));
        toyStore.addNewToy(new Toy(2, "Barbie", 7, 20));
        toyStore.addNewToy(new Toy(3, "Car", 2, 40));

        toyStore.updateToyWeight(1, 15);

        Toy prizeToy = toyStore.getPrizeToy();
        if (prizeToy != null) {
            System.out.println("Ура! Ты выиграл(а) " + prizeToy.getName() +  ".");
            toyStore.saveToysToFile("toys_data.txt");
        } else {
            System.out.println("Эта игрушка не учавствует в розыгрыше.");
        }
    }
}
