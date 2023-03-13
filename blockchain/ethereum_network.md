# 이더리움 네트워크 기본 개념과 Ropsten 네트워크

# 기본 개념

## 블록체인의 분류

| 유형 | 특징 | 관련 기술 |
| --- | --- | --- |
| public | 누구나 네트워크에 참여 | Bitcoin, Ethereum, Litecoin… |
| private | 하나의 조직 혹은 기관이 관장하는 네트워크, 승인된 자료를 읽고, 지정 노드만 거래를 승인 | Quorum, MultiChain, Iroha, Monax…. |
| consortium | 이해 관계자 간에 컨소시엄을 구성하여 네트워크를 구성, 네트워크 참여자에 의해 접근 허용 | Hyperledger Fabric, Tendermint, R3 Corda, Private Thchnologies… |

## 이더리움 네트워크

네트워크 마다 고유의 아이디를 가지며, 해당 아이디에 맞게 거래를 하거나 트랜잭션을 보낼 수 있음.

### 이더리움 네트워크의 종류

- 메인넷
    - 실제 거래가 발생하는 네트워크로, 트랜잭션 수행시 매우 높은 가격에 해당하는 가스를 소모하게된다.
- 테스트넷
    - 무제한으로 테스트할 수 있는 네트워크

> **이더리움 클라이언트란?**
> 

네트워크에 노드로 참여하며, RPC(Remote Procedure Call)요청을 수신하고, 결과를 반환하는 Endpoint

이더리움 클라이언트에는 많은 종류가 있으며 Go언어로 개발된 Geth네트워크를 주로 사용하고있으며, besu 클라이언트도 있다.

<br>

**프라이빗 네트워크** 

- 누구나 공개된 Client SW로 프라이빗 네트워크를 구축 가능
- besu는 엔터프라이즈 환경에 맞게 개량된 Hyperledger의 ethereum 프로젝트

> 지갑(Wallet)이란?
> 

블록체인 네트워크를 사용할 수 있도록 계정의 개인키(private key)를 관리하는 프로그램 (개인키로 sign하여 트랜잭션을 보냄.)

## 계정 생성 절차

1. 개인키 생성 : 256bit의 무작위 숫자 → 64자리의 Hex값으로 인코딩
2. 타원곡선전자서명 알고리즘(ECDSA, secp256k1)을 사용하여 공개키 생성
3. Keccak-256 hashing
4. 계정 주소 (3번에서 생성된 값의 마지막 20Byte가 곧 계정 주소)

## 용어 정리

- 클라이언트
    - 네트워크에 노드로 참여하며, RPC(Remote Procedure Call)요청을 수신하고, 결과를 반환하는 Endpoint
- 프로바이더
    - 클라이언트를 통해 Ethereum에 대한 액세스를 제공하는 소비자가 사용할 수 있는 JavaScript 개체입니다.
- 지갑과 계정
    - Provider와 Client사이에서 middleware로서 행동하고 signing 여산을 수행하고 private key를 관리하는 end-user application.
- 수도꼭지(Faucet)
    - Test network에서 사용할 수 있는 Ether를 제공해주는 프로그램
- 가스
