# debugging

## 1. 의존성 옵션 변경 문제

### 현상

- build.gradle에서 Dependencies의 옵션 compile이 실행되지 않음

### 원인

- 기존에 Gradle에서 사용하고 있는 compile은 추후 지원이 중단 되고 implementation으로 대체

### 해결

- compile 대신 implementation으로 대체



<details>
<summary>추가 학습</summary>
<div markdown="1">

의존성 옵션들

- implementation: 의존 라이브러리 수정시 본 모듈까지만 재빌드
  - 본 모듈을 의존하는 모듈은 해당 라이브러리의 api 를 사용할 수 없음

- api: 의존 라이브러리 수정시 본 모듈을 의존하는 모듈들도 재빌드
  - 본 모듈을 의존하는 모듈들도 해당 라이브러리의 api 를 사용할 수 있음

- compileOnly: compile 시에만 빌드하고 빌드 결과물에는 포함하지 않음
  - runtime 시 필요없는 라이브러리인 경우 (runtime 환경에 이미 라이브러리가 제공되고 있는가 하는 등의 경우)
  - 참고: https://blog.gradle.org/introducing-compile-only-dependencies

- runtimeOnly: runtime 시에만 필요한 라이브러리인 경우

- annotationProcessor: annotation processor 명시 (gradle 4.6)

- 참고: 
  - https://docs.gradle.org/4.6/release-notes.html
  - https://blog.gradle.org/incremental-compiler-avoidance#about-annotation-processors 

  - Annotation processing 이 필요없다고 예측되는 경우 빌드 제외


기존에 Gradle에서 사용하고 있는 compile은 추후 지원이 중단 되고 implementation으로 대체

대규모 다중 프로젝트 빌드에서 api/complile 대신 implementation을 사용하면 빌드 시스템이 재컴파일 해야 하는 프로젝트의 크기가 즐어들기 때문에 빌드시간이 상당히 개선 될수 있어 대체했다고 합니다.


</div>
</details>
---





