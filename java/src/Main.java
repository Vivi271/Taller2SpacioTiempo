import java.io.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Main {
    public static void main(String[] args) {
        try {
            BufferedReader reader = new BufferedReader(new FileReader("dummy_data.csv")); // O(1)
            BufferedWriter writer = new BufferedWriter(new FileWriter("processed_data.csv")); // O(1)

            String line = reader.readLine(); // O(1)
            String[] headers = line.split(","); // O(n)
            writer.write("Username,Birthdate,Age,Income,Debt,IncomeMinusDebt\n"); // O(1)

            SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd"); // O(1)
            Date currentDate = new Date(); // O(1)

            while ((line = reader.readLine()) != null) { // O(n)
                String[] values = line.split(","); // O(m)
                String username = values[0]; // O(1)
                Date birthdate = dateFormat.parse(values[1]); // O(1)
                double income = Double.parseDouble(values[2]); // O(1)
                double debt = Double.parseDouble(values[3]); // O(1)

                long ageInMillis = currentDate.getTime() - birthdate.getTime(); // O(1)
                int age = (int) (ageInMillis / (1000 * 60 * 60 * 24 * 365.25)); // O(1)

                double incomeMinusDebt = income - debt; // O(1)

                writer.write(username + "," + values[1] + "," + age + "," + income + "," + debt + "," + incomeMinusDebt + "\n"); // O(1)
            }

            reader.close(); // O(1)
            writer.close(); // O(1)

            System.out.println("ETL process completed."); // O(1)
        } catch (IOException | ParseException e) { //  O(1)
            e.printStackTrace(); // O(1)
        }
    }
}
// EL BIG-O DEL CÓDIGO ES: O(n*m)