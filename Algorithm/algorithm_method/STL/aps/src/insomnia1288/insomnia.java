package insomnia1288;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;

public class insomnia {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testcase = Integer.parseInt(br.readLine());
        int oneToNine = (1 << 10) - 1;

        for (int i = 1; i <= testcase; i++){
            int n = Integer.parseInt(br.readLine());
            int visited = 0;
            int count = 0;

            while (visited != oneToNine){
                count++;

                char[] charArray = String.valueOf(n * count).toCharArray();

                for (char c : charArray){
                    int num = c -'0';
                    visited |= (1 << num);
                }
            }
            System.out.println("#" + i + " " + n * count);
        }
    }
}
