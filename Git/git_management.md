# git 관리
### 목차

[git mirroring을 통한 commit을 보존한 repository clone](#git-mirroring을-통한-commit을-보존한-repository-clone)

[100MB를 넘어가는 크기의 파일을 지닌 저장소 미러링](#100mb를-넘어가는-크기의-파일을-지닌-저장소-미러링)


## git mirroring을 통한 commit을 보존한 repository clone

### 1. 원본 저장소를 clone --bare

> --bare와 --mirror의 차이
> **bare** : 일반적인 복제와 달리 저장소를 bare repository로 복제합니다. 즉, 작업 디렉토리를 생성하지 않습니다. 이는 보통 다른 저장소에 푸시하기 전에 중간 저장소로 사용됩니다.
> **mirror** : 원격 저장소의 모든 브랜치, 태그 및 리모트 추적 브랜치를 복제합니다. 또한 원격 저장소에서 발생한 모든 이벤트를 캡처합니다. 이는 보통 백업용으로 사용됩니다.

<br>

저희는 저장소를 커밋을 보존하여 다른 저장소로 옮기는 것이 목적이기 때문에, --bare 명령어를 통해 클론 받습니다.

```bash
git clone --bare [원본 저장소 주소]
```

- old-repostory.git 형태로 클론이 됩니다.

<br>

### 2. 복사할 저장소로 push

```bash
cd old-repository.git
git push --mirror [저장할 원격 저장소 주소]
```

<br>

## 100MB를 넘어가는 크기의 파일을 지닌 저장소 미러링

대용량 파일이 올라간 후 커밋이 반복적으로 찍히게 되면 .git이 비대해지는 문제가 발생합니다.

이를 해결하기 위해서 .git에서 풀필요한 commit을 삭제해줄 필요가 있습니다.

<br>


### 1. 원본 저장소를 clone --bare

```bash
git clone --bare [원본 저장소 주소]
```

### 2. git lfs와 BFG Repo Cleaner 설치

- 모든 브랜치와 태그를 대상으로 Git 저장소의 모든 커밋에서 특정 확장자를 가진 파일을 Git LFS로 추적하도록 설정합니다.
- old-repository.git이 있는 위치에 bfg-1.14.0.jar이 있어야 합니다.
    - 각자의 버전에 맞게 bfg 파일을 별도로 설치하시면 됩니다.

```bash
$ ls
old-repository.git  bfg-1.14.0.jar
```

### 3. 커밋 히스토리에서 large file을 찾아 트래킹

- old-repository.git에 들어가서 lfs를 설치합니다.
- 위에서 push했을 때 발생한 에러를 주의깊게 보면 어떤 확장자가 문제인지 확인할 수 있습니다.
    - 확장자가 복수일 경우, "*.{def dic}"와 같이 작성하시면 됩니다.

```bash
$ cd old-repository.git
$ git lfs install
$ git filter-branch --tree-filter 'git lfs track "*.{트래킹할 확장자}"' -- --all
```

--tree-filter 옵션은 모든 커밋을 수정하고 지정된 명령어를 실행하여 결과를 다시 커밋합니다. 

여기서는 "git lfs track" 명령어가 트래킹할 확장자를 가진 파일을 Git LFS로 추적하도록 설정하도록 수정하고 다시 커밋합니다.

### 4. 100MB가 넘어가는 commit을 .git에서 삭제
- 삭제가 완료되면, old-repo.git 폴더 내에서 복사해 넣을 원격 저장소로 mirror push하면 됩니다.

```bash
$ java -jar ../bfg-1.14.0.jar --strip-blobs-bigger-than 100M --delete-files *.gif --no-blob-protection
$ git push --mirror <git 저장소>
```

<br>

- `--strip-blobs-bigger-than 100M` : 100MB가 넘어가는 파일을 삭제합니다.
- `--delete-files *.gif` : 특정 확장자를 가진 파일을 삭제합니다.
- `--no-blob-protection` : protected commoits 에러 발생: protected commits을 포함시켜서 제거해주어야 하기 때문에 jarfile 실행 명령어에 조건을 추가합니다.

