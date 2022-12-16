package com.example.filter.filter;

import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;
import org.springframework.web.util.ContentCachingRequestWrapper;
import org.springframework.web.util.ContentCachingResponseWrapper;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.BufferedReader;
import java.io.IOException;

@Slf4j
@WebFilter(urlPatterns = "/api/user/*")
public class GlobalFilter implements Filter {

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {

        // 전처리 : doFilter를 위한 과정
        // ByteArrayOutputStream cachedContent 변수에 요청 정보를 담아 몇번이든 읽을 수 있도록 함
        // cachedContent에는 길이만 지정하고 있지, 내용은 없음
        ContentCachingRequestWrapper httpServletRequest = new ContentCachingRequestWrapper ((HttpServletRequest) request);
        ContentCachingResponseWrapper httpServletResponse = new ContentCachingResponseWrapper ((HttpServletResponse) response);

        String url = httpServletRequest.getRequestURI();

        chain.doFilter(httpServletRequest, httpServletResponse);// 주의 : doFilter 이후에 읽어야 함

        // 후처리 : 모든 정보를 기록할 곳
        // req
        String reqContent = new String(httpServletRequest.getContentAsByteArray());
        log.info("request url : {}, request body : {}", url, reqContent);

        String resContent = new String(httpServletRequest.getContentAsByteArray());
        int httpStatus = httpServletResponse.getStatusCode();

        httpServletResponse.copyBodyToResponse();

        log.info("response status : {}, responseBody : {} : ", httpStatus, resContent);
    }
}
