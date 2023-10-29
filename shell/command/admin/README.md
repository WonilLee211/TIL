# shell admin command

## 시스템 관리

- 프로세스, 메모리 관리를 위한 명령어

## `crontab`

- cron을 관리하는 테이블

| 옵션 | 설명 |
| --- | --- |
| -e | 등록된 명령어 수정, 명령어가 없을 경우 새로 생성 |
| -l | 등록된 명령어 리스트 확인 |
| -r | 등록된 크론탭을 삭제 |
| -u | 크론탭을 등록할 사용자 지정 |

### 사용법

```zsh
# cron 등록, 등록된 cron이 없다면 vim open
crontab -e
## 반복수행할 조건 입력하면 됨
```

- 작업 일정 및 커멘트 기입
```shell
PROGRAM_PATH='{PATH}'
# 입력형태
"분(0-59) 시(0-23) 일(1-31) 월(1-12) 요일(0-6) 실행 명령(command)

# 5분 마다 program.sh 실행
*/5 * * * * /home/user/program.sh

# 4-10 시 사이에 1시간마다 program.sh 실행
0 4-10/1 * * * /home/user/program.sh

# 매일 1시에 log 로 끝나는 파일을 찾아서 find.log 파일로 저장 
0 1 * * * find -name "*.log" ./ >> /path/find.log

# 매일 1시, 3시에 program.sh 를 실행하고 로그를 저장
0 1,3 * * * /path/program.sh >> /path/`date -u + \%Y\%m\%d.\%H\%M.program.sh.log` 2>$1

* * * * * {PROGRAM_LANGUAGE_PATH}/PROGRAM_LANGUAGE ${PROGRAM_PATH}/FILE_NAME 
" 예
* * * * * /usr/bin/python3 ${PROGRAM_PATH}/FILE_NAME
" 예2

```
- `:wq` 저장

```shell
ECHOTEST_PATH='path'
* * * * * /bin/sh ${ECHOTEST_PATH}/echotest.sh >> ~${ECHOTEST_PATH}/echotest.sh.log 2>&1 
```
- 반복 작업 실행 결과를 로그로 남기기
- `2>&1`
  - 표준오류 출력을 표준 출력과 동일한 파일로 리다이렉트시킴
  - 표준 접근 기호
    - `0` : 표준 입력
    - `1` : 표준 출력
    - `2` : 표준 오류 출력
  - 실행 결과와 표쥰 오류가 log에 함께 남게됨.

```shell
# crontab 리스트 출력
crontab -l

# crontab 백업
crontab -l > {BACKUP_PATH}/{FILENAME}

# crontab 삭제
crontab -r
```

cron이 등록되면 특정 경로의 username의 파일에 저장되기 때문에 해당 파일에 echo 명령어로 직접 입력할 수 있음
```zsh
sudo bash -c 'echo \"
# hadoop log cleansing
0 1 * * * find /var/log/hadoop -not -name \"*.gz\" -type f -mtime +2 -exec gzip {} \;
0 1 * * * find /var/log/hadoop -name \"*.gz\" -mtime +14 -delete \" >> /var/spool/cron/user_name'
```

## `exec`

- 주어진 명령어를 실행하는데 새로운 프로세스를 생성하지 않고 실행한 프로세스로 명령어를 실행함
- 명령어를 실행한 ppid가 유지된다.

### 옵션

| -c | 환경 변수가 없는 상태로 실행 |
| -a[name] | 0번째 인수로 이름을 전달 |
| -l | 0번째 인수로 대쉬를 전달 |

### 사용법

잘 몰르겠음..

## `free`

- 메모리 사용량을 확인하는 명령어
- ubuntu 환경에서만 가능한 명령어

### options

| 옵션 | 내용 |
| --- | --- |
| -h | 사람이 읽을 수 있는 GB, MB, KB 형태로 변경하여 출력 |
| -s | 지정한 초마다 이용량 출력 |










