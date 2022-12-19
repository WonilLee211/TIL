package com.example.pjtrestaurant.naver;

import com.example.pjtrestaurant.naver.dto.SearchImageReq;
import com.example.pjtrestaurant.naver.dto.SearchImageRes;
import com.example.pjtrestaurant.naver.dto.SearchLocalReq;
import com.example.pjtrestaurant.naver.dto.SearchLocalRes;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;

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
