# 이더리움 스마트 컨트랙트 배포와 호출

## 📜Contents

1. [Smart Contract 란?](#1-smart-contract-란)
2. [mart contract 배포와 호출](#2-smart-contract-배포와-호출)

<br>

## 1. Smart Contract 란?

(사전적 의미) 똑똑한 계약

1990년대 Nick Szabo가 소개한 개념

모호성이 없는 아주 단순한 디지털 형태의 계약

프로그래밍 소스코드로 이루어진 하나의 서약, 계약

<br>

### 블록체인에서의 스마트 컨트랙트 정의 : 불변의 컴퓨터 프로그램 (마스터링 이더리움에서)

- 일종의 하나의 컴퓨터 프로그램 알고리즘 소스
- `불변(immutable)` 한 번 이더리움에 배포되고 나면 변경 불가
- `결정적(deterministic)` 누가 실행하던 간에 결과는 모두 같음
- EVM(Ethereum Virtual Machine)` 위에서 동작
    
    이더리움 : 전세계 수천 수만대 컴퓨터로 이루어진 단 한대의 World Computer
    
- 탈중앙화된 World Computer 동일한 상태를 유지

<br>

**⇒ 전체의 여러 대의 컴퓨터가 동일한 프로그래밍 로직을 가지고 있고 동일한 데이터셋을 유지하게 됨**

<br>

### Smart Contract를 작성하는 언어

- `Solidity`
- LLL
- Viper
- Assembly

<br>

## 2. Smart Contract 배포와 호출

1. 소스코드 개발
2. 컴파일
    1. 기계가 읽을 수 있는 형태의 바이트 코드
    2. ABI : Smart Contract가 어떤 Function을 가지고 있는지를 적어놓은 인터페이스
    
    ⇒ 이 두가지를 트랜잭션에 담게 됨
    
3. 트랜잭션이 생성되면 data 영역에 bytecode가 담김
4. 서명
5. 서명된 값이 트랜잭션이 되어서 전체 이더리움 네트워크로 퍼지게 되면서 불변의 프로그램 구축

⇒ 프로그램을 지칭하는 하나의 고유 주소를 받을 수 있음

    = 컨트랙트 주소(CA)

    내가 배포한 프로그램을 어디에 있는지 어떤 프로그램인지 찾을 수 있는 하나의 ID

🧐잘 기억해두어야겠죠~?

**CA와 ABI가 있으면 언제든 이더리움 네트워크 상에서 프로그램을 실행할 수 있게 됨**

> 💡 Bytecode : 작성한 Smart Contract 코드의 컴파일 이후의 코드
> ABI : 컨트랙트 안에 정의되어 있는 Function list
> CA : 배포 후 ID로 쓰게 될 주소
