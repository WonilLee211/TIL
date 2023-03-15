package bitmask_10726;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Bitmask {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testcase = Integer.parseInt(br.readLine());
        for (int i = 1; i <= testcase ; i++ ){
            StringTokenizer st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int testBit = (1 << N) - 1;
            if (testBit == (M & testBit)) System.out.println("#" + i + " " + "ON");
            else System.out.println("#" + i + " " + "OFF");
        }
    }
}