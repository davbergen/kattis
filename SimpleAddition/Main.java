import java.util.*;
import java.util.Scanner;



public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String first = in.nextLine(); //read first integer
        String second = in.nextLine(); //read second integer
        char[] arrayA = first.toCharArray(); //convert integer to char array to allow handling of large integers
        char[] arrayB = second.toCharArray();
        String result = charArrayAddition(arrayA, arrayB);
        System.out.println(result);
    }

    /**
     * Performs addition on each element in the char array. Has a carry over variable in case elementwise addition exceeds 9.
     * @param arrayA first integer stored as array
     * @param arrayB second integer stored as array
     * @return the result of the addition in the form of a string
     */
    private static String charArrayAddition(char[] arrayA, char[] arrayB) {
        int max = Math.max(arrayA.length, arrayB.length);
        char[] result = new char[max];
        int carryOver = 0;
        int toAdd, a, b;
        for (int i = 0; i < max; i++) {
            //If arrays A and B are of different length, the shorter array should act as 0 where there are no integers.
            if(arrayA.length - 1 - i >= 0) {
                a = Character.getNumericValue(arrayA[arrayA.length - 1 - i]);
            } else {
                a=0;
            }
            if(arrayB.length - 1 - i >= 0) {
                b = Character.getNumericValue(arrayB[arrayB.length - 1 - i]);
            } else {
                b=0;
            }
            toAdd = (a + b + carryOver) % 10;
            if (a + b + carryOver >= 10) {
                result[max-i-1] = Character.forDigit(toAdd, 10);
                carryOver = 1;
            } else {
                result[max-i-1] = Character.forDigit(toAdd, 10);
                carryOver = 0;
            }
        }
        //if the result array becomes longer than any of the parameter arrays, copy into a new, larger array
        if(carryOver != 0){
            char[] temp = new char[max+1];
            for (int i = 0; i<max; i++){
                temp[max-i] = result[max-1-i];
            }
            temp[0] = '1';
            result = temp;
        }
        return new String(result);
    }
}
