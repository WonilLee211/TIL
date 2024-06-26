# Gradle 프로젝트 구성하기

그런 다음 개별 프로젝트를 build.gradle 을 통해 빌드하는 방식으로 동작합니다.

---

## settings.gradle

- 그래들이 settings.gradle 파일을 참고해 프로젝트의 구조를 파악함
- settings에서는 전체 프로젝트의 구조를 빌드
- 보통 아래와 같이 한 개의 프로젝트를 구성

```groovy
rootProject.name="project-name"
include "project-name"
```

### 여러 모듈 프로젝트 관리 방법

1. 여러 모듈 프로젝트들을 포함하는 경우 아래와 같이 하위 프로젝트들을 포함시켜 줍니다.

```groovy
rootProject.name="project-name"
include ":sub-project1"
include ":sub-project2"
```

2. 모듈 프로젝트들이 많아서 이들을 group 으로 관리하고 싶다면 다음과 같이 자동 빌드하는 스크립트를 쓰면 편리합니다.

```groovy
rootProject.name = 'security-gradle3'

["comp", "web", "server"].each {

    def compDir = new File(rootDir, it)
    if(!compDir.exists()){
        compDir.mkdirs()
    }

    compDir.eachDir {subDir ->

        def gradleFile = new File(subDir.absolutePath, "build.gradle")
        if(!gradleFile.exists()){
            gradleFile.text =
                    """

                    dependencies {

                    }

                    """.stripIndent(20)
        }

        [
                "src/main/java/com/sp/fc",
                "src/main/resources",
                "src/test/java/com/sp/fc",
                "src/test/resources"
        ].each {srcDir->
            def srcFolder = new File(subDir.absolutePath, srcDir)
            if(!srcFolder.exists()){
                srcFolder.mkdirs()
            }
        }

        def projectName = ":${it}-${subDir.name}";
        include projectName
        project(projectName).projectDir = subDir
    }
}
```

---

## build.gradle

- 루트 폴더의 build.gradle 에서는 전체 하위 프로젝트의 공통 설정에 대한 사항을 기술해 넣습니다.

```groovy

buildscript {
    ext {
        spring = "2.4.1"
        boot = "org.springframework.boot"
        lombok = "org.projectlombok:lombok"
    }
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath("$boot:spring-boot-gradle-plugin:$spring")
    }
}

allprojects {
    group = "com.sp.fc"
    version = "1.0.0"
}
subprojects {

    apply plugin: "java"
    apply plugin: boot
    apply plugin: "io.spring.dependency-management"
    apply plugin: "idea"

    repositories {
        mavenCentral()
    }

    configurations {
//        developmentOnly
        runtimeClasspath {
            extendsFrom developmentOnly
        }
    }

    dependencies {
//        developmentOnly("$boot:spring-boot-devtools") // 초기 개발 때 로그인에 문제됨
        implementation "$boot:spring-boot-starter-security"
        implementation 'com.fasterxml.jackson.core:jackson-annotations'

        compileOnly lombok
        testCompileOnly lombok
        annotationProcessor lombok
        testAnnotationProcessor lombok

        testImplementation "$boot:spring-boot-starter-test"
    }

    test {
        useJUnitPlatform()
    }

}


// 서브 프로젝트 별로 설정을 달리 함. 부트 어플리케이션을 만들지 않을 컴포넌트

["comp", "web"].each {
    def subProjectDir = new File(projectDir, it)
    subProjectDir.eachDir {dir->
        def projectName = ":${it}-${dir.name}"
        project(projectName){
            // 기본적으로 스프링 부트 플러그인을 썼기 때문에 bootJar가 생김
            bootJar.enabled(false) // 꺼놓기
            jar.enabled(true)
        }
    }
}

// 부트 어플리케이션을 만들것이기 떄문에 bootJar 켜놓기
["server"].each {
    def subProjectDir = new File(projectDir, it)
    subProjectDir.eachDir {dir->
        def projectName = ":${it}-${dir.name}"
        project(projectName){

        }
    }
}

help.enabled(false)

```

---

## 프로젝트 auth reload 확성화 하기

- IntelliJ 에서 compiler.automake.allow.when.app.running 을 체크하고
- 설정의 Build project automatically 를 체크하고
- Run configuration 에서 On 'Update' action 과 On frame deactivation 의 값을 적절하게 수정해 줍니다.

참고 사이트 : https://velog.io/@bread_dd/Spring-Boot-Devtools
