# # Git bash Command Language

### 상대경로

- `./` : 현재 작업하고 있는 폴더
- `../` : 현재 작업하고 있는 폴더의 상위폴더.

### 기본 명령어

- `touch` : 파일 생성

- `mkdir` : 새폴더 생성

- `ls` : 현재 작업중인 디렉토리 폴더/파일 목록 반환

- `cd` : 현재 작업중인 디렉토리를 변경
  
  - `cd ..` : 상위폴더로 이동

- `start`, `open` : 폴더/파일을 여는 명령어

- `rm` : 파일을 삭제
  
  - `-r` 옵션을 주면, 폴더 삭제 기능
  - `-rf` : -r로 삭제가 안될 때 강제로 삭제하는 방법

- `code` : vscode로 파일 열기(vscode가 있을 때)

### git bash 명령어

- `ls -a` : 숨긴 폴더까지 같이 보임

- 작성자 정보 입력하기(깃헙 정보로. 전용 컴퓨터 아니면 local로 하기)
  
  `git config --global user.email "you@example.com"`
  `git config --global user.name "Your Name"`

- `git config —global —list` : 입력한 작성자 정보 확인하기

- `git rm --cached <file>…`  : working directory로 옮기기

- git status : 깃의 상태를 확인하기
  
  - 붉은색 파일 : untracked
  - 초록색 파일 : changes to be committed : tracked 파일. staging area에 있는 파일

- `git log` : commit history 출력

- `git diff hashcode1 hashcode2` : 두 커밋 사이의 차이를 출력

- `git log —oneline` : 깃로그를 한줄로 보기

- `git remote -v `: 현재 등록된 리모트 레퍼지토리 주소

- `git branch -M (master/main)` : main 브랜치 명 변경
  
  

- `git stash apply` : 다시 가져오기

- `git push/pull -u origin master` : 다음부터 git push/pull만 쳐도 됨.

- `git stash` : 현재 나의 수정사항을 stash 공간으로 이동시키고 가장 최근버전으로 되돌리는 명령어
  
  

### 실습 **git bash로 git 실행하기**

1. `git config —global [user.email](http://user.email) “email”`
2. `git config —global [user.name](http://user.name) “닉네임”`
3. `git init`
4. touch [readme.md](http://readme.md)
5. start [readme.md](http://readme.md)
6. `git status` : 현재 로컬 영역 상태 확인
   - 붉은색 파일 : untracked
   - 초록색 파일 : changes to be committed : tracked 파일. staging area에 있는 파일
7. `git add 파일명` : untracted or modified files to staging area
8. `git commit` (여기서 바로 메세지를 넣으면 vim모드로 안들어감)
9. vim 모드
10. insert + 메세지 작성 + esc + :wq
    1. 커밋메세지 : 내가 이 파일을 왜 저장했는지(변경 추가 내용) 메세지 남기면 나중에 확인할 때 편함
11. 커밋된파일 수정 >> 파일이 modified로 바뀌고
12. 다시 add commit하기
13. `git add . `
14. `git commit -m “message”` : staging area 파일들 커밋하기

> 💡 **vim 2가지 모드**
> 
> 1. command 모드
> 2. edit 모드 : insert 누르기
>    1. command로 돌아가기 : esc + :wq(저장하고 나가기)
>    2. esc + :q(저장안하고 나가기)

### GitHub 이용하기

- `git remote add origin(별명) 레포주소` : 레포와 로컬과 연결하기

- `git remote -v` : 등록된 주소 보기

- `git push origin master` : 로컬 레포에서 서버로 옮기기

- `git clone github-repository-url` : 서버레포를 복제해서 가져오기
  
  > `주의점` Sync맞추기
  > 기준버전은 Github!!!
  > 시작할 때 clone or pull부터 하자

- `git pull origin master` : 연결된 레포에서 최신 버전 내려받기
