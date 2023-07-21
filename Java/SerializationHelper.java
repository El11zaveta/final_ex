import java.io.*;
import java.util.ArrayList;
import java.util.List;


public class SerializationHelper {
    public static void serializeToys(List<Toy> toys, String filename) {
        try (ObjectOutputStream outputStream = new ObjectOutputStream(new FileOutputStream(filename))) {
            outputStream.writeObject(toys);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static List<Toy> deserializeToys(String filename) {
        List<Toy> toys = new ArrayList<>();
        try (ObjectInputStream inputStream = new ObjectInputStream(new FileInputStream(filename))) {
            toys = (List<Toy>) inputStream.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return toys;
    }
}
