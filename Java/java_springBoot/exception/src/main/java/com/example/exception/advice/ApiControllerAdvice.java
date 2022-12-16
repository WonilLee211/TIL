package com.example.exception.advice;

import com.example.exception.controller.ApiController;
import com.example.exception.dto.Error;
import com.example.exception.dto.ErrorResponse;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.MissingServletRequestParameterException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.validation.ConstraintViolationException;
import javax.validation.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;


@RestControllerAdvice(basePackageClasses = ApiController.class)
public class ApiControllerAdvice {

    @ExceptionHandler(value=Exception.class) // value : 어떤 에러를 잡을 건지 작성하는 부분(Exception.class : 모든 예외를 의미)
    public ResponseEntity exception(Exception e){

        System.out.println(e.getClass().getName());
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("");

    }


    @ExceptionHandler(value= MethodArgumentNotValidException.class)
    public ResponseEntity methodArgumentNotValidException(MethodArgumentNotValidException e, HttpServletRequest httpServletRequest){// HttpServletRequest : 현재의 request 가져올 수 있음

        BindingResult bindingResult = e.getBindingResult();
        List<Error> errorList = new ArrayList<>(); // 에러들 담을 곳

        bindingResult.getAllErrors().forEach(error -> {
            FieldError field = (FieldError) error;
            String fieldName = field.getField();
            String message = field.getDefaultMessage();
            String invalidValue = field.getRejectedValue().toString();

            Error errorMessage = new Error(); // Error 객체에 각 정보 입력
            errorMessage.setField(fieldName);
            errorMessage.setMessage(message);
            errorMessage.setInvalidValue(invalidValue);

            errorList.add(errorMessage);    // error 객체 errorList에 담기
        });

        ErrorResponse errorResponse = new ErrorResponse();
        errorResponse.setErrorList(errorList);
        errorResponse.setMessage("");
        errorResponse.setRequestUrl(httpServletRequest.getRequestURI());
        errorResponse.setStatusCode(HttpStatus.BAD_REQUEST.toString());
        errorResponse.setResultCode("Fail");

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);

    }

    // 인자는 받았는데 제약조건에 맞지않을 때 발생하는 에러
    @ExceptionHandler(value= ConstraintViolationException.class)
    public ResponseEntity ConstraintViolationException(ConstraintViolationException e, HttpServletRequest httpServletRequest){

        List<Error> errorList = new ArrayList<>(); // 에러들 담을 곳

        e.getConstraintViolations().forEach(error -> {

            Stream<Path.Node> stream = StreamSupport.stream(error.getPropertyPath().spliterator(), false);
            List<Path.Node> list = stream.collect(Collectors.toList());

            String fieldName = list.get(list.size() - 1).getName();
            String message = error.getMessage();
            String invalidValue = error.getInvalidValue().toString();


            Error errorMessage = new Error();
            errorMessage.setField(fieldName);
            errorMessage.setMessage(message);
            errorMessage.setInvalidValue(invalidValue);

            errorList.add(errorMessage);

        });

        ErrorResponse errorResponse = new ErrorResponse();
        errorResponse.setErrorList(errorList);
        errorResponse.setMessage("");
        errorResponse.setRequestUrl(httpServletRequest.getRequestURI());
        errorResponse.setStatusCode(HttpStatus.BAD_REQUEST.toString());
        errorResponse.setResultCode("Fail");

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
    }


    // 요청과정에서 받아야하는 인자가 비어있을때 발생하는 에러
    @ExceptionHandler(value = MissingServletRequestParameterException.class)
    public ResponseEntity missingServletRequestParameterException(MissingServletRequestParameterException e, HttpServletRequest httpServletRequest){

        List<Error> errorList = new ArrayList<>(); // 에러들 담을 곳

        String fieldName = e.getParameterName();
        String message = e.getMessage();

        Error errorMessage = new Error();
        errorMessage.setField(fieldName);
        errorMessage.setMessage(message);

        ErrorResponse errorResponse = new ErrorResponse();
        errorResponse.setErrorList(errorList);
        errorResponse.setMessage("");
        errorResponse.setRequestUrl(httpServletRequest.getRequestURI());
        errorResponse.setStatusCode(HttpStatus.BAD_REQUEST.toString());
        errorResponse.setResultCode("Fail");

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
    }
}

//{
//        "statusCode": "400 BAD_REQUEST",
//        "requestUrl": "/api/user",
//        "code": null,
//        "message": "",
//        "resultCode": "Fail",
//        "errorList": [
//            {
//            "field": "name",
//            "message": "크기가 2에서 2147483647 사이여야 합니다",
//            "invalidValue": ""
//            },
//            {
//            "field": "age",
//            "message": "1 이상이어야 합니다",
//            "invalidValue": "0"
//            }
//        ]
//}
