# 💻 chapter 1. 디자인 패턴

# questionnaire

## section UI 디자인 패턴

### ❓ 1. MVVM 패턴이란

> ❗MVP 패턴에서 view와 presenter의 높은 의존도를 해결하기 위해 고안된 패턴으로
>  model, View, View Model의 준말입니다.
> 데이터 바인딩을 통해 view와 view model을 연결하고 view가 데이터 업데이트에 대한 출력을 선택하게 됩니다.
> 뷰 로직과 비지니스 로직이 분리된 덕분에 테스트 코드 또한 독립적으로 수행할 수 있게 됩니다.
> 또한 코드의 양이 줄어든다는 장점이 있습니다.

### ❓ 2. MVVM의 단점은 뭔가요?

> ❗프로젝트가 커지면서 View Model이 비대해진다는 경향이 있습니다.
> 

### ❓ 3. UI 디자인 패턴 패러다임의 변화를 간략하게

> ❗MVC 패턴에서 apple이 독자적인 OS 운영 환경에 부적합했음.
> 일관성있는 앱의 느낌을 제공하기 위해 View의 재사용성을 높혀야 하며, Model의 데이터도 다른 여러 곳에서 사용하기 때문에 재사용성을 높혀야 했다. 그래서 View와 Model간의 의존성 해결이 요구됐음
>  이를 보완하기 위해 고안된 것이 apple's MVC(MVC Cocoa)
> 컨트롤러를 중심으로 view와 model이 분리됨. 하지만 대규모 프로젝트에서 controller의 역할이 혼자 비대해졌음
> 이를 보완하기 위해 MVP 패턴 등장. view model을 view로 취급하고 중계자로 presenter 도입
> 생명 주기, 화면 전환, 콜백 처리만 vm에서 처리하도록 하고 나머지는 presenter로 위임하며 중계자의 비중을 줄이려고 노력
> 하지만 presenter가 view를 업데이트하는 과정에서 view의 역할이 전혀 없어 둘 간에 높은 의존도가 형성됨.
> 이를 개선한 것이 MVVM 패턴. 데이터 바인딩으로인해 제대로된 구현은 RxSwift를 써야한다는 제한점 등으로 인해
> 현재 현업에서는 VIPER 패턴 사용

### ❓ 4. VIPER패턴에 대해서 설명해주세요.

> ❗VIPER의 컨셉은 책임분리원칙을 기반으로 클래스는 하나의 기능만을 가지고 클래스가 제공하는 모든 서비스는 그 하나의 책임을 수행하는 데 집중되어야 한다는 원칙 아래 높은 응집도와 낮은 결합도라는 특징을 가진 디자인 패턴입니다.
> View는 View controller를 의미하며 UI처리 역할을 맡습니다. presenter와 의존성을 가지며 presenter의 요청에 따라 UI를 업데이트합니다.
> presenter는 view, Router, Interactor에 대한 의존성을 가지며 view에서 event를 받아 interator를 통해 처리하고, view에 데이터와 함께 UI Update 요청을 보내거나 Router를 통한 화면 이동을 처리합니다.
> Interator는 business logic을 담당하며 API통신, networking이나 Entity에 대한 처리를 하고 결과를 Presenter에 전달합니다.
> Router(WireFrame)은 화면 전환과 각 구성 요소에 DI 처리합니다.
> Entity는 속성들을 가지는 Data Model을 의미합니다.


### ❓ 5. OSI 7 Layer 또는 TCP/IP Layer에서 계층화하는 이유가 무엇인가요?

> ❗

### ❓ 6. Encapsulation과 Decapsulation을 서로 비교하며 설명해주세요

> ❗

### ❓ 7. IP란?

> ❗ 

### ❓ 8. IP 주소란?

> ❗

### ❓ 9. IPV4 vs IPV6 을 설명해주세요.

> ❗

### ❓ 10. IPv4의 주소 부족현상을 해결하기 위해 현재 어떤 방법을 사용하고 있나요?

> ❗