# naver search api활용한 맛집 리스트 서비스

## 1. DB 설계

- 메모리 DB로 구현
- MemoryDbRepositoryIfs

```java
package com.example.pjtrestaurant.db;

public interface MemoryDbRepositoryIfs<T> {

    Optional<T> findByid(int index); // 해당 값에 대해 옵셔널하게 반환. index값에 해당하는 엔티티를 찾아서 반환하는 메서드
    T save(T entity);
    void deleteById(int index);
    List<T> listAll();

}
```
- MemoryDbRepositoryAbstract
  - T가 upper Bounded wildcard로 MemoryDbEntity를 상속받았기 때문에 MemoryDbEntity를 상속받은 클래스 타입들이 올 수 있음

```java
package com.example.pjtrestaurant.db;

abstract public class MemoryDbRepositoryAbstract<T extends MemoryDbEntity> implements MemoryDbRepositoryIfs<T>{

    private final List<T> db = new ArrayList<>(); // 데이터를 저장할 곳
    private int index = 0; // primary key authIncrement index

    @Override
    public Optional<T> findByid(int index) {
        // T가 upper Bounded wildcard로 MemoryDbEntity를 상속받았기 때문에 MemoryDbEntity를 상속받은 클래스가 올 수 있음
        return db.stream().filter(it -> it.getIndex() == index).findFirst();
    }

    @Override
    public T save(T entity) {
        var optionalEntity = db.stream().filter(it -> it.getIndex() == entity.getIndex()).findFirst();
        if(optionalEntity.isEmpty()){
            // db에 데이터가 없는 경우
            index++;
            entity.setIndex(index);
            db.add(entity);
            return entity;
        }else{
            // db에 이미 데이터가 있는 경우
            var preIndex = optionalEntity.get().getIndex();
            entity.setIndex(preIndex);

            deleteById(preIndex);
            db.add(entity);
            return entity;
        }
    }

    @Override
    public void deleteById(int index) {
        var optionalEntity = db.stream().filter(it -> it.getIndex() == index).findFirst();
        if(optionalEntity.isPresent()){
            db.remove(optionalEntity.get());
        }
    }

    @Override
    public List<T> listAll() {
        return db;
    }
}

```
- MemoryDbEntity
  - 모든 데이터베이스를 가진 클래스는 MemoryDbEntity를 상속받도록 함

  
```java
package com.example.pjtrestaurant.db;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class MemoryDbEntity {
    protected int index;
}

```

### 2. WishList(맛집 목록)

- WishListRepository
  - generic type, T가 WishListEntity가 된다

```java
package com.example.pjtrestaurant.wishList.repository;

@Repository
public class WishListRepository extends MemoryDbRepositoryAbstract<WishListEntity> {
    // generic type, T가 WishListEntity가 된다.    
}

```
- WishListDto
  - 응답받은 정보를 담을 클래스
  - 필요한 정보의 필드를 가진 entity
  - Db에 저장하는 entity와 유사하지만 별도로 구성해서 역할을 나눠야 함
  
```java
package com.example.pjtrestaurant.wishList.dto;


@Data
@NoArgsConstructor
@AllArgsConstructor
public class WishListDto {

    private int index;

    private String title;                   // 음식명, 장소명
    private String category;                // 카테고리
    private String address;                 // 주소
    private String roadAddress;             // 도로명
    private String homePageLink;            // 홈페이지 주소
    private String imageLink;               // 음식, 가게 이미지 주소
    private boolean isVisit;                // 방문여부
    private int visitCount;                 // 방문 횟수
    private LocalDateTime lastVisitDate;    // 마지막 방문 일자

}

```

## 3. naver search API 통신


- application.yaml

```yaml
naver:
  url:
    search:
      local: https://openapi.naver.com/v1/search/local.json
      image: https://openapi.naver.com/v1/search/image
  client:
    id:
    secret:

```

- 지역/이미지 검색 요청 dto
- 지역/이미지 검색 응답 dto
- 요청-응답

```java
package com.example.pjtrestaurant.naver.dto;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class SearchLocalReq {

    private String query = "";
    private int display = 1;
    private int start = 1;
    private String sort = "random";

    public MultiValueMap<String, String> toMultivalueMap(){

        var map = new LinkedMultiValueMap<String, String >();
        map.add("query", query);
        map.add("display", String.valueOf(display));
        map.add("start", String.valueOf(start));
        map.add("sort", sort);
        return map;
    }

}
//--------------------------------------------------------------
package com.example.pjtrestaurant.naver.dto;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class SearchLocalRes {

    private String lastBuildDate;
    private int total;
    private int start;
    private int display;
    private List<SearchLocalItem> items;

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class SearchLocalItem{
        private String title;
        private String link;
        private String category;
        private String description;
        private String telephone;
        private String address;
        private String roadAddress;
        private int mapx;
        private int mapy;

    }
}
// -----------------------------------------------------------------

package com.example.pjtrestaurant.naver.dto;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class SearchImageReq {

    private String query = "";
    private int display = 1;
    private int start = 1;
    private String sort = "sim";
    private String filter = "all";

    public MultiValueMap<String, String> toMultivalueMap(){

        var map = new LinkedMultiValueMap<String, String >();
        map.add("query", query);
        map.add("display", String.valueOf(display));
        map.add("start", String.valueOf(start));
        map.add("sort", sort);
        map.add("filter", filter);

        return map;
    }

}
// -----------------------------------------------------------------
package com.example.pjtrestaurant.naver.dto;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class SearchImageRes {

    private String lastBuildDate;
    private int total;
    private int start;
    private int display;
    private List<SearchImageItem> items;

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class SearchImageItem {
        private String title;
        private String link;
        private String thumnail;
        private int sizeheight;
        private int sizewidth;

    }

}

```

- NaverClient
  1. 지역검색
  2. 이미지 검색
  3. 결과 반환
   
```java
package com.example.pjtrestaurant.naver;

@Component
public class NaverClient {

    @Value("${naver.client.id}") // application.yaml에서 정보 가져오기
    private String naverClientId;

    @Value("${naver.client.secret}")
    private String naverSecret;

    @Value("${naver.url.search.local}")
    private String naverLocalSearchUrl;
    @Value("${naver.url.search.image}")
    private String naverImageSearchUrl;



    public SearchLocalRes searchLocal(SearchLocalReq searchLocalReq){
        // 요청하는 주소
        var uri = UriComponentsBuilder
                .fromUriString(naverLocalSearchUrl)
                .queryParams(searchLocalReq.toMultivalueMap())
                .build()
                .encode()
                .toUri();

        // header
        var headers = new HttpHeaders();
        headers.set("X-Naver-Client-Id", naverClientId);
        headers.set("X-Naver-Client-Secret", naverSecret);
        headers.setContentType(MediaType.APPLICATION_JSON);


        var httpEntity = new HttpEntity<>(headers);
        var responseType = new ParameterizedTypeReference<SearchLocalRes>(){};
        // 요청보내고 응답받아오기
        var responseEntity = new RestTemplate().exchange(
                uri,
                HttpMethod.GET,
                httpEntity,
                responseType
        );

        return responseEntity.getBody();

    }

    public SearchImageRes searchImage(SearchImageReq searchImageReq){

        // url만들기
        var uri = UriComponentsBuilder
                .fromUriString(naverImageSearchUrl)
                .queryParams(searchImageReq.toMultivalueMap())
                .build()
                .encode()
                .toUri();

        // header 달기
        var headers = new HttpHeaders();
        headers.set("X-Naver-Client-Id", naverClientId);
        headers.set("X-Naver-Client-Secret", naverSecret);
        headers.setContentType(MediaType.APPLICATION_JSON);

        var httpEntity = new HttpEntity<>(headers);
        var responseType = new ParameterizedTypeReference<SearchImageRes>(){};

        // 요청-응답
        var responseEntity = new RestTemplate().exchange(
                uri,
                HttpMethod.GET,
                httpEntity,
                responseType
        );
        return responseEntity.getBody();

    }
}
```

## 4.  TEST

```java
package com.example.pjtrestaurant.service;

@SpringBootTest
public class WishListServiceTest {
    @Autowired
    private WishListService wishListService;

    @Test
    public void searchTest(){
        var result = wishListService.search("갈비집");
        System.out.println(result);
        Assertions.assertNotNull(result);
    }
}

```

## 5. controller

- springfox boot starter library 추가
- application.yaml에 버전 차이에 따른 pathMatch 설정
  - `spring.mvc.pathmatch.matching-strategy: ant-path-matcher`

```java
package com.example.pjtrestaurant.controller;

import com.example.pjtrestaurant.wishList.dto.WishListDto;
import com.example.pjtrestaurant.wishList.service.WishListService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/restaurant")
@RequiredArgsConstructor
public class ApiController {
    private final WishListService wishListService;
    @GetMapping("/search")
    public WishListDto search(@RequestParam String query){
        return wishListService.search(query);
    }
}

```

## 맛집 추가 기능

- controller
  
```java
package com.example.pjtrestaurant.controller;

@Slf4j
@RestController
@RequestMapping("/api/restaurant")
@RequiredArgsConstructor
public class ApiController {
    
    private final WishListService wishListService;
    
    ...

    @PostMapping("")
    public WishListDto add(@RequestBody WishListDto wishListDto){
      log.info("{}", wishListDto);

      return wishListService.add(wishListDto);
    }
}

```

- service
  - entity와 dto 역할을 분리했기 때문에 서로 변환해주는 과정이 필요함

```java
package com.example.pjtrestaurant.wishList.service;

@Service
@RequiredArgsConstructor
public class WishListService {
    private final NaverClient naverClient;

    private final WishListRepository wishListRepository;


    public WishListDto add(WishListDto wishListDto) {

        var entity = dtoToEntity(wishListDto);
        var saveEntity = wishListRepository.save(entity);
        return entityToDto(saveEntity);
    }
    public WishListEntity dtoToEntity(WishListDto wishListDto) {
        var entity = new WishListEntity();
        entity.setIndex(wishListDto.getIndex());
        entity.setTitle(wishListDto.getTitle());
        entity.setCategory(wishListDto.getCategory());
        entity.setAddress(wishListDto.getAddress());
        entity.setRoadAddress(wishListDto.getRoadAddress());
        entity.setHomePageLink(wishListDto.getHomePageLink());
        entity.setImageLink(wishListDto.getImageLink());
        entity.setVisit(wishListDto.isVisit());
        entity.setVisitCount(wishListDto.getVisitCount());
        entity.setLastVisitDate(wishListDto.getLastVisitDate());
        return entity;
    }
    
    public WishListDto entityToDto(WishListEntity wishListEntity) {
        var dto = new WishListDto();
        dto.setIndex(wishListEntity.getIndex());
        dto.setTitle(wishListEntity.getTitle());
        dto.setCategory(wishListEntity.getCategory());
        dto.setAddress(wishListEntity.getAddress());
        dto.setRoadAddress(wishListEntity.getRoadAddress());
        dto.setHomePageLink(wishListEntity.getHomePageLink());
        dto.setImageLink(wishListEntity.getImageLink());
        dto.setVisit(wishListEntity.isVisit());
        dto.setVisitCount(wishListEntity.getVisitCount());
        dto.setLastVisitDate(wishListEntity.getLastVisitDate());

        return dto;
    }
}

```
## 전체 맛집 목록 조회

- controller


```java
package com.example.pjtrestaurant.controller;

@Slf4j
@RestController
@RequestMapping("/api/restaurant")
@RequiredArgsConstructor
public class ApiController {
    private final WishListService wishListService;

    ...
    
    @GetMapping("/all")
    public List<WishListDto> findAll(){
        return wishListService.findAll();
    }
}
```

- service

```java

package com.example.pjtrestaurant.wishList.service;

@Service
@RequiredArgsConstructor
public class WishListService {
    private final NaverClient naverClient;

    private final WishListRepository wishListRepository;
    ...

    public List<WishListDto> findAll() {

        return wishListRepository.listAll()
                .stream()
                .map(it -> entityToDto(it))
                .collect(Collectors.toList());
    }

    public WishListDto add(WishListDto wishListDto) {

        var entity = dtoToEntity(wishListDto);
        var saveEntity = wishListRepository.save(entity);
        return entityToDto(saveEntity);
    }
    public WishListEntity dtoToEntity(WishListDto wishListDto) {
        var entity = new WishListEntity();
        entity.setIndex(wishListDto.getIndex());
        entity.setTitle(wishListDto.getTitle());
        entity.setCategory(wishListDto.getCategory());
        entity.setAddress(wishListDto.getAddress());
        entity.setRoadAddress(wishListDto.getRoadAddress());
        entity.setHomePageLink(wishListDto.getHomePageLink());
        entity.setImageLink(wishListDto.getImageLink());
        entity.setVisit(wishListDto.isVisit());
        entity.setVisitCount(wishListDto.getVisitCount());
        entity.setLastVisitDate(wishListDto.getLastVisitDate());
        return entity;
    }
    public WishListDto entityToDto(WishListEntity wishListEntity) {
        var dto = new WishListDto();
        dto.setIndex(wishListEntity.getIndex());
        dto.setTitle(wishListEntity.getTitle());
        dto.setCategory(wishListEntity.getCategory());
        dto.setAddress(wishListEntity.getAddress());
        dto.setRoadAddress(wishListEntity.getRoadAddress());
        dto.setHomePageLink(wishListEntity.getHomePageLink());
        dto.setImageLink(wishListEntity.getImageLink());
        dto.setVisit(wishListEntity.isVisit());
        dto.setVisitCount(wishListEntity.getVisitCount());
        dto.setLastVisitDate(wishListEntity.getLastVisitDate());

        return dto;
    }

}
```

## delete 기능 & 방문횟수 카운트

```java
package com.example.pjtrestaurant.controller;

@Slf4j
@RestController
@RequestMapping("/api/restaurant")
@RequiredArgsConstructor
public class ApiController {
    private final WishListService wishListService;
    
    ...

    @DeleteMapping("/{index}")
    public void delete(@PathVariable Integer index){
        wishListService.delete(index);
    }

    @PostMapping("/{index}")
    public void addVisit(@PathVariable Integer index){
        wishListService.addVisit(index);
    }


}

```

- wishListService

```java
package com.example.pjtrestaurant.wishList.service;

@Service
@RequiredArgsConstructor
public class WishListService {
    private final NaverClient naverClient;

    private final WishListRepository wishListRepository;

    ...

    public void delete(Integer index) {
        wishListRepository.deleteById(index);
    }

    public void addVisit(Integer index){
        var wishItem = wishListRepository.findByid(index);
        if (wishItem.isPresent()){
            var item = wishItem.get();
            item.setVisit(true);
            item.setVisitCount(item.getVisitCount() + 1);

        }
    }
}

```
