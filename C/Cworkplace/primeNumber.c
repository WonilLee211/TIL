#include <stdio.h>

/**
 * 배열을 이용한 소수 찾기 프로그램 
 * 
 * 
 */

int main() {
    int guess = 5; // 소수인지 판별하고 있는 수
    int prime[1000]; // 현재까지 찾은 소수의 개수 - 1
    // 아래 두 개의 소수를 미리 찾았으므로 초기값은 1이 된다.
    int index = 1; // for 문 변수
    int i; // 소수인지 판별하기 위해 쓰는 변수
    int ok; // 처음 두 소수는 특별한 경우로 친다.
    prime[0] = 2;
    prime[1] = 3;
    for (;;) {
        ok = 0;
        for (i = 0; i <= index; i++){
            if (guess % prime[i] != 0){
                ok++;
            }
            else {
                break;
            }
        }
        // 소수라면 ok 값이 index + 1과 같아짐
        if (ok == (index + 1)){
            index++;
            prime[index] = guess;
            printf("소수 : %d \n", guess);
            if (index == 999) break;
        }
        guess += 2;
    }
    return 0;
}