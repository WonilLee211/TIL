# 처리명령어

## 1. 문자열 처리

- 문자열의 변경, 검색, 비교 등의 처리를 위한 명령어

### `awk`

- 입력을 주어진 분리자(field seperator)로 분리하여 명령을 처리함

| 옵션 | 설명 |
| -- | -- |
| F | 문자열을 분리할 기준이 되는 분리 문자 입력 |
| v | 파라미터 전달 |


### 내장함수

| 함수 | 설명 |
| -- | -- |
| sub | 지정한 문자열 치환 |
| gsub | 문자열 일괄 치환 |
| index | 주어진 문자열과 일치하는 문자의 인덱스를 반환 |
| length | 문자열의 길이를 반환 |
| substr | 시작위치에서 주어진 길이 만큼의 문자열 반환 |
| split | 문자열을 분리하여 배열로 반환 |
| print | 문자열 출력 |
| printf | 지정한 포맷에 따라 함수 출력 |
| system | 추가 명령 실행 |

`print`

```bash
# 현재 라인을 출력
$ echo "Hello World" | awk "{ print $0 }"

# 주어진 입력을 분리자로 분리하여 첫 번째 필드를 출력


$ echo "Hello World" | awk "{ print $1 }"

# 주어진 입력을 분리자로 분리하여 두 번째 필드를 출력
$ echo "Hello World" | awk "{ print $2 }"

# 주어진 입력을 특정 분리자로 분리하여 두 번째 필드를 출력
$ echo "Hello,World" | awk -F "," '{ print $2 }'
```

`sub`

```bash
# 입력 문자열을 주어진 분리자로 분리 후 특정 문자를 치환한 후 출력
$ echo "i have a glass of water." | awk -F " " '{ sub("a", "b", $4 ); print $0}'
# >> i have a glbss of water. 
```

`gsub`

```bash
# 입력 문자열을 주어진 분리자로 분리 후 지정한 치환 조건으로 각 필드의 문자를 일괄 치환
$ echo "i have a glass of water." | awk -F " " '{ gsub("a", "b"); print $0 }'
# >> i hbve b glbss of wbter.
```

`index`
```bash
# 입력문자열을 분리자로 분리 후 네 번째 필드에서 "a" 문자의 위치 출력
$ echo "i have a glass of water" | awk -F " " '{ print index($4, "a") }'
# >> 3
```


`length`

```bash
# 입력 문자열을 분리 후 특정 필드의 문자열 길이 출력
$ echo "i have a glass of water" | awk -F " " '{ print length($4) }'
# >> 5
```

`substr(target_field, start_index, length)`

```bash
# 입력 문자열을 분리 후 첫 번째 필드에서 세 번째 문자부터 2개 문자 출력
$ echo "1234567890" | awk -F " " '{ print substr($1, 3, 2) }'
# >> 34
```

`split(field, array_name, seperator)`

```bash
# 입력 문자열을 분리 후 첫 번째 필드를 / 로 분리하여 배열로 저장하고, 첫 번째와 세 번째 원소를 출력
$ echo "A/B/C/D/E/F/G" | awk -F " " '{ print split($1, array, "/"); print array[1]; print array[3]; }'
# >> 7
# >> A
# >> C
```

`printf`

```bash
# 원하는 포맷에 맞춰서 출력
$ echo | awk '{ printf("%.1f + %.2f = %.3f\n", 40.1, 40.2, 40.1 + 40.2); }'
# >> 40.1 + 40.20 = 80.300
```

`system`

```bash
# system echo로 첫 번째 필드 출력하기
$ echo "Hello World" | awk -F " " '{ system("echo "$1) }'
# >> Hello
```

