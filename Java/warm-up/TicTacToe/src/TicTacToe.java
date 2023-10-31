import java.util.*;

public class TicTacToe {
    static ArrayList<Integer> playerPositions = new ArrayList<Integer>();
    static ArrayList<Integer> pcPositions = new ArrayList<Integer>();
    public static void main(String[] args) {
        char[][] gameBoard = {{' ','|',' ','|',' '},
                              {'-','+','-','+','-'},
                              {' ','|',' ','|',' '},
                              {'-','+','-','+','-'},
                              {' ','|',' ','|',' '}};
        printGameBoard(gameBoard);
        Scanner scan = new Scanner(System.in);

        while (true){
            System.out.println("Enter your position (1-9): ");
            int position = scan.nextInt();
            while (playerPositions.contains(position) || pcPositions.contains(position)){
                System.out.println("Position taken, enter a correct position ");
                position = scan.nextInt();
            }

            placePiece(gameBoard, position,"player");

            Random rand = new Random();
            int pcPosition = rand.nextInt(9)+1;
            while (playerPositions.contains(pcPosition) || pcPositions.contains(pcPosition)){
                System.out.println("Position taken, enter a correct position ");
                pcPosition = rand.nextInt(9)+1;
            }

            placePiece(gameBoard, pcPosition,"pc");
            printGameBoard(gameBoard);
            String result = checkWinner();
            System.out.println(result);
            if(playerPositions.size()+ pcPositions.size()==9){
                break;
            }
        }

    }

    public static void printGameBoard(char[][] gameBoard){
        for(char[] row:gameBoard){
            for(char c:row){
                System.out.print(c);
            }
            System.out.println();
        }

    }

    public static void placePiece(char[][] gameBoard, int position, String user){
        char symbol='X';

        if(user.equals("pc")){
            symbol='O';
            playerPositions.add(position);
        }else {
            pcPositions.add(position);
        }


        switch(position){
            case 1:
                gameBoard[0][0]=symbol;
                break;
            case 2:
                gameBoard[0][2]=symbol;
                break;
            case 3:
                gameBoard[0][4]=symbol;
                break;
            case 4:
                gameBoard[2][0]=symbol;
                break;
            case 5:
                gameBoard[2][2]=symbol;
                break;
            case 6:
                gameBoard[2][4]=symbol;
                break;
            case 7:
                gameBoard[4][0]=symbol;
                break;
            case 8:
                gameBoard[4][2]=symbol;
                break;
            case 9:
                gameBoard[4][4]=symbol;
                break;
            default:
                break;
        }
    }
    public static String checkWinner(){
        List topRow = Arrays.asList(1,2,3);
        List midRow = Arrays.asList(4,5,6);
        List botRow = Arrays.asList(7,8,9);
        List leftCol = Arrays.asList(1,4,7);
        List midCol = Arrays.asList(2,5,8);
        List rightCol = Arrays.asList(3,6,9);
        List crossOne = Arrays.asList(1,5,9);
        List crossTwo = Arrays.asList(7,5,3);

        List<List> winning = new ArrayList<List>();
        winning.add(topRow);
        winning.add(midRow);
        winning.add(botRow);
        winning.add(leftCol);
        winning.add(midCol);
        winning.add(rightCol);
        winning.add(crossOne);
        winning.add(crossTwo);

        for(List l : winning){
            if(playerPositions.containsAll(l)){
                return "you won! ";
            } else if (pcPositions.containsAll(l)) {
                return "Pc wins ";
            } else if (playerPositions.size()+ pcPositions.size()==9) {
                return "Nobody wins";
            }
        }

        return "";
    }
}
