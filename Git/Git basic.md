## why Git & Github

**Git이란**

- 분산 버전 관리 시스템
    - 버전 : 컴퓨터 소프트웨어의 특정 상태
    - 관리 : 어떤 일의 사무, 시설이나 물건의 유지 개량
    - 프로그램 : 컴퓨터에서 실행될 때 명령어의 모음
- 버전관리 :
    - 코드의 히스토리를 관리하는 도구
    - 개발되어온 과정 파악 가능
    - 이전 버전과의 **변경 사항 비교 및 분석**
- 분산 : 약간.. 블록체인 느낌.
    - 서버의 버전 데이터베이스를 개인 컴퓨터에도 같이 가지고 있음
    - sync만 맞다면 안전하게 관리 가능
- git 기반의 저장소 서비스 제공 업체
    1. gitLab : 삼성에서 서버를 관리하는 곳
    2. GitHub :
        1. TIL(to i learned) 정리하는 법 배우기(오늘)
    3. Bitbucket : 

**GitHub을 사용하면 뭐가 좋을까?**

- 열정, 성실함, 능력까지 증명할 수 있음.
    - 잔디
        - git에 파일을 올리면 1commit!
        - 잔디에 초록색으로 색칠하게 된다.
    - repository
        - git에 commit하면 repository하나에 매칭이 된다..
        
---
## **CLi & markdown**

CLi(Command Line Interface): 명령어를 통해서 사용자와 컴퓨터가 상호작용하는 방식

- 수많은 서버, 개발 시스템이 CLi를 통한 조작환경을 제공
- 그래서 개발자할거니까 CLi를 배우자!

GUI(Graphic User Interface) : 그래픽을 통해 사용자와 컴퓨터가 상호작용하는 방식

- 사용하기 쉬움
- 단계가 많고 컴터 성능을 더 많이 소모

**절대경로**

- 전체적인 경로가 다 있는 것
- 윈도우 바탕 화면의 절대경로는 C드라이브부터 시작

**상대경로**

- 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
- 현재 C:/Users라면, 바탕화면은 saffy/Desktop
- ./ : 현재 작업하고 있는 폴더
- ../ : 현재 작업하고 있는 폴더의 상위폴더.
  
---
## **CLi 기본 명령어**

touch : 파일 생성

mkdir : 새폴더 생성

ls : 현재 작업중인 디렉토리 폴더/파일 목록 반환

cd : 현재 작업중인 디렉토리를 변경

cd .. : 상위폴더로 이동

start, open : 폴더/파일을 여는 명령어

rm : 파일을 삭제

-r 옵션을 주면, 폴더 삭제 기능

-rf : -r로 삭제가 안될 때 강제로 삭제하는 방법

code : vscode로 파일 열기(vscode가 있을 때)

---

## markdown

- 텍스트 기반의 가벼운 마크업(markup) 언어
- 마크다운 cheat sheet
- [Markdown Reference](https://support.typora.io/Markdown-Reference/)


### markdown 연습하기

# 개발자로 성장하기

- 대체 어디서부터 시작해서 어디까지 해야할까?
- Python과 Java를 배우면 개발자가 되는걸까?

		제일 중요한 건 ==**꾸준한 학습**을 할 수 있는 사람==

> 인용문을 작성할 수 있는 블럭 :>
>
> > 인용문 안에 인용문
> >
> > > 또 인용문

1. 순서가 있는 리스트
2. 엔터치면 자연스럽게 다음 번호로

Task List

- [x] : '- [ ]'

코드 블럭 : ``` 백틱 세개 치고 엔터

```python
print("코드 블럭 만들기 ```")
```

한줄은 백틱 한개로 감싸기

테이블 | | |

|      |      |
| ---- | ---- |
| \|   |      |

링크 

[네이버](http://naver.com)

이미지

![양양이](./image/20180221120711081_1.gif)

기울이기


*기울이기*

취소선 

~~취소선~~


GITHUB에서 read.md로 명명하면 공식문서로 인정됨

개인플젝트의 소개문서로 작성

매일학습한 내용정리

마크다운을 이용한 블로그 운영

---
## Git basic

- README.md
    - 프로젝트에 대한 설명 문서
    - Github 프로젝트에서 가장 먼저 보는 문서
    - 일반적으로 소프트웨어와 함께 배포
    - 작성 형신은 따로 없으나 일반적으로 마크다운을 이용해서 작성티
    
    - 템플릿

- Repository
    - 특정 디렉토리를 버전관리하는 저장소
    - git init 명령어로 로컬 저장소를 생성(>>.git)
    - .git 디렉토리에 버전 관리에 필요한 모든 것들이 들어있음
    - 주소 옆에 (master)라고 뜨면 git으로 관리되고있음을 의미함
        

#### **git의 3가지 영역**

1. working directory : 내가 작압하고 있는 실제 디렉토리
2. staging area : 커밋으로 남기고 싶은 특정 버전으로 관리하고 싶은 파일이 있는 곳
    - repository에 저장하기전에 내가 관리하고싶은 파일들만 !
3. Repository : 커밋들이 저장되는 곳. 버전관리가 저장되는 곳


>💡 
>1. working directory에 있는 뉴비파일 1,2,3,4,5 중에 내가 버전관리하고 싶은 대상파일인, 1,2,3만 staging area로 임시 저장하고 repository에 최종 커밋한다.
>2. 여기서 4,5파일은 untracked라고 표현.(버전관리대상이 아님)
>3. 1,2,3을 staging area로 이동하기 위해 명령어 git add
>4. 최종 Repository에 저장하기 위해 git commit


>💡 파일이 수정되었을 때
>1. tracked 파일들이 modified로 변하고
>2. git add + git commit을 통해
>3. 새로운 버전을 저장한다.



### 실습 **git bash로 git 실행하기**

1. git config —global [user.email](http://user.email) “email”
2. git config —global [user.name](http://user.name) “닉네임”
3. git init
4. touch readme.md
5. start readme.md
6. git status
7. git add a.txt
8. git commit (여기서 바로 메세지를 넣으면 vim모드로 안들어감)
9. vim 모드
10. insert + 메세지 작성 + esc + :wq
    1. 커밋메세지 : 내가 이 파일을 왜 저장했는지(변경 추가 내용) 메세지 남기면 나중에 확인할 때 편함
11. 커밋된파일 수정 >> 파일이 modified로 바뀌고
12. 다시 add commit하기
13. git add .
14. git commit -m “message”

> 💡 **vim 2가지 모드**
> 
> 1. command 모드
> 2. edit 모드 : insert 누르기
>     1. command로 돌아가기 : esc + :wq(저장하고 나가기)
>     2. esc + :q

### 웹 깃헙 이용하기 remote repository(깃헙)


>💡 SSAFY 교육관련 내용은 private으로 올리기


1. 저장되는 장소 만들기. 웹에서 create a repository
2. 터미널에서 레퍼지토리 위치 등록
    1. git remote add origin(별명) 레포주소
3. git remote -v : 등록된 주소 보기
4. 이제 파일들을 올리기(로컬에 있는 commit 내역을 repository로 업데이트)
    1. git push origin master
5. 내려받기
    1. `git clone github-repository-url`


>💡 주의점 Sync맞추기
>- 기준버전은 Github!!!
>- github에서 더하던 빼던 해야 함.


6. 깃헙에 최신버전 내려받기
    1. git pull origin master
    
---
### **git bash 명령어**

- ls -a : 숨긴 폴더까지 같이 보임
- 작성자 정보 입력하기(깃헙 정보로. 전용 컴퓨터 아니면 local로 하기)
    
    git config --global user.email "[you@example.com](mailto:you@example.com)"
    git config --global [user.name](http://user.name/) "Your Name"
    
- git config —global —list : 입력한 작성자 정보 확인하기
- git add : untracked 파일을 staging area로 올림
    - git add . : 현재 디렉토리안에 모든 파일을 staging area로 임시저장
- git rm --cached <file>… : working directory로 옮기기
- git commit : staging area의 파일을 repository에 저장됨
    - git commit -m “message” : vim모드를 피할 수 있음
- git status : 깃의 상태를 확인하기
    - 붉은색 파일 : untracked
    - 초록색 파일 : changes to be committed : tracked 파일. staging area에 있는 파일
- git log : commit history 출력
- git diff hashcode1 hashcode2 : 두 커밋 사이의 차이를 출력
- git log —oneline : 깃로그를 한줄로 보기
- git remote -v : 현재 등록된 리모트 레퍼지토리 주소

>💡 **최종 github 사용 순환구조**
>1. 깃허브에서 pull 받기
>2. 공부하기
>3. add하기
>4. commit하기
>5. push하기


💡 **clone과 pull 차이**
1. clone : 깃허브 레포를 로컬로 복제
    - 이때, .git도 같이 복제됨. >> git 설정이 있는 폴더. 즉, 리모트 주소도 같이 복제된다.>>`git remote add ~` 명령이 불필요.
2. pull : remote repository에 있는 버전과 동일한 버전으로 다운로드.사전에 리모트 정보가 있었어야 함.& 이미 .git이 존재해야 함.
- 클론 이후에 푸쉬와 풀만 하면 됨
- 깃허브에 레퍼지토리가 등록조차 되지않았을 때.
- git init부터 시작
- 깃허브에 레퍼지토리 등록 후에
- 클론을 통해 깃허브 레퍼지토리 유알엘을 통해 clone으로 폴더에 복제받기
- 이후에 설정이 완료되면 일부의 수정 후에 pull add commit push를 통해 업데이트하기

---
### 깃헙 레퍼지토리 삭제

1. github repository에서 settings
2. 제일 아래 Danger Zone
    1. delete this repository
    
---
### TIL 레퍼지토리 만들기

구글에 TIL (기억은 기록을 이길 수 없다.를 reference 삼기