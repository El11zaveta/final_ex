import java.util.ArrayList;
import java.util.List;


public class ToyStore {
    private List<Toy> toys;

    public ToyStore() {
        toys = new ArrayList<>();
    }

    public void addNewToy(Toy toy) {
        toys.add(toy);
    }

    public void updateToyWeight(int toyId, double weight) {
        for (Toy toy : toys) {
            if (toy.getId() == toyId) {
                toy.setWeight(weight);
                break;
            }
        }
    }

    public Toy getPrizeToy() {
        double totalWeight = 0;
        for (Toy toy : toys) {
            totalWeight += toy.getWeight();
        }

        double randomWeight = Math.random() * totalWeight;

        double currentWeight = 0;
        for (Toy toy : toys) {
            currentWeight += toy.getWeight();
            if (randomWeight <= currentWeight) {
                Toy prizeToy = new Toy(toy.getId(), toy.getName(), 1, toy.getWeight());
                toy.setQuantity(toy.getQuantity() - 1);
                return prizeToy;
            }
        }

        return null;
    }

    public void saveToysToFile(String filename) {
        SerializationHelper.serializeToys(toys, filename);
    }

    public void loadToysFromFile(String filename) {
        toys = SerializationHelper.deserializeToys(filename);
    }

}