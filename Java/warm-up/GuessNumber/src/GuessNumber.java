import java.util.Random;
import java.util.Scanner;

public class GuessNumber {
    public static void main(String[] args) {
        Random rand = new Random();
        Scanner scanner = new Scanner(System.in);

        int randomNumber = rand.nextInt(10) + 1;

        while (true) {
            System.out.println("Enter your guess (1-10): ");

            int playerGuess = scanner.nextInt();

            if (playerGuess == randomNumber) {
                System.out.println("Correct! 🚀");
                break;
            } else if (randomNumber > playerGuess) {
                System.out.println("Number is higher, guess again");
            } else {
                System.out.println("the number is lower. Guess again");
            }
        }
    }
}
