# 패턴 매칭

## 패턴 매칭에 사용되는 알고리즘

- 고지식한 패턴 검색 알고리즘
- 카프-라빈 알고리즘
- KMP 알고리즘
- 보이어-무어 알고리즘

## 1. 고지식한 알고리즘(brute Force)

- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작
    
    ```python
    p = 'is'
    t = 'This is a book~!'
    M = len(p)
    N = len(t)
    
    def BruteForce(p, t):
        i, j = 0, 0
        while j < M and i < N:
            if t[i] != p[j]:
                i = i - j # 일치하지 않을 경우,  i는 비교 시작점의 다음 위치
                j = -1 # 패턴 첫자리
            i += 1
            j += 1
        
            if j == M:
                return i - M # 검색 성공
            else:
                return -1 # 검색 실패
    ```
    
    ```python
    p = 'is'
    t = 'This is a book~!'
    M = len(p)
    N = len(t)
    
    def BruteForce(p, t):
        for idx in range(N - M + 1):
            for jdx in range(M):
                if t[idx] != p[jdx]:
                    break
    
            else: # 패턴이 매칭된 상태
                return idx
        else:
            return -1
    ```
    

### 시간복잡도

- 최악의 경우 : O(NM)

## 2. KMP 알고리즘(Knuth-Moriss-Pratt)

- 불일치가 발생한 텍스트 스트링의 앞부분에 어떤 문자가 있는지 미리 알고 있으므로 불일치가 발생한 앞부분에 대하여 다시 비교하지 않고 매칭을 수행
- 패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화
    - next[M] : 불일치가 발생했을 때 이동할 다음 위치

### 시간복잡도

- O(M + N)

### 구현

1. 패턴 전처리
    - 패턴마다 매칭실패 시 돌아갈 인덱스를 저장
    - 맨 앞자리 글자부터 일치해야 returnidx를 쌓아나갈 수 있음

```python
def pre_process(pattern):
    # 전처리를 위한 테이블을 작성 (LPS table longest prefix suffix)
    lps = [0] * len(pattern)
    j = 0  # lps를 만들기 위한 prefix index

    for i in range(1, len(pattern)):  # 0번째 자리는 패턴 확인할 필요없음
        # prefix index 위치에 있는 문자와 비교
        if pattern[i] == pattern[j]:
            lps[i] = j + 1    # i 의 앞에 중복되는 패턴이 존재한다
            j += 1            # j 는 중복된 글자의 자리수
        else:
            j = 0
            # 여기서 0으로 이동한 다음 prefix idx 비교를 한 번 더 해야함.
            if pattern[i] == pattern[j]:
                lps[i] = j + 1
                j += 1

    return lps

pattern = 'abcdabcef'
# [0, 0, 0, 0, 1, 2, 3, 0, 0]
```

```python
pattern = 'ABCDABD'
text = 'ABC ABCDAB ABCDABCDABDE'
M = len(p)
N = len(t)

def KMP(text, pattern):
    lps = pre_process(pattern)   # 전처리로 lps 테이블 생성

    i = 0   # text index
    j = 0   # pattern index
    while i < len(text):
        if pattern[j] == text[i]:    # 같은 문자라면
            # 다음 문자 비교
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == len(pattern):   # pattern 이 전부 일치할 때
            return i - j        # text의 위치

    return -1     # 일치하는 문장이 없는 경우

text = 'ABC ABCDAB ABCDABCDABDE'
pattern = 'ABCDABD'

print(KMP(text, pattern))
```

### 알고리즘

1. 전처리
    - 패턴에 대한 리턴 인덱스를 생성한다.
    - 패턴은 문자열 내에서 앞 부분 문자부터 일정길이가 중복되어야 한다.
    - 
    

## 3. 보이어 무어 알고리즘

- 오른쪽에서 왼쪽으로 비교
- 대부분의 상용 소프트웨어에서 채택하고 있는 알고리즘
- 패턴에 오른쪽 끝에 있는 문자가 불일치하고 문자가 패턴 내에 존재하지 않는 경우 이동거리는 무려 패턴의 기리만큼
- 텍스트 문자를 다 보지 않아도 된다.
- 패턴의 오른쪽부터 비교한다.

### 시간복잡도

최악의 경우 : O(mn)

- 입력에 따라 다르지만 일반적으로 O(n)보다 시간이 덜 든다.

### 구현

- 전처리

```python
def pre_process(pattern):
    M = len(pattern)  # 패턴의 길이

    skip_table = dict()
    for i in range(M-1):
        skip_table[pattern[i]] = M - i - 1

    return skip_table
```

- 보이어 무어 알고리즘

```python
def boyer_moore(text, pattern):
    skip_table = pre_process(pattern)
    M = len(pattern)

    i = 0  # text index
    while i <= len(text) - M:
        j = M - 1   # 뒤에서 비교해야 되기 때문 j를 끝에 index
        k = i + (M-1)  # 비교를 시작할 위치 (현재위치 + M번째 인덱스)

        # 비교할 j가 남아있고, text와 pattern이 일치하면
        # 그 다음 앞에 글자를 비교하기 위해 인덱스 감소
        while j >= 0 and pattern[j] == text[k]:
            j -= 1
            k -= 1

        if j == -1:  # 일치 함
            return i
        # 일치하지 않는다면
        else:
            # i를 비교할 시작 위치를 skip table에서 가져온다.
            i += skip_table.get(text[i+M-1], M)

    return -1  # 일치되는 패턴이 없음

text = 'ABC ABCDAB ABCDABCDABDE'
pattern = 'ABCDABD'

print(boyer_moore(text, pattern))
```

---

# 문자열 매칭 알고리즘 비교

- 찾고자 하는 문자열 패턴의 길이 m, 총 문자열 길이 n
- 고지식한 패턴 검색 알고리즘 : 수행시간 O(mn)
- 카프-라빈 알고리즘 : 수행시간 O(n)
- KMP 알고리즘 : 수행시간 O(n)