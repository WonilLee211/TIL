package com.example.validation.validator;


import com.example.validation.annotation.YearMonth;

import javax.validation.ConstraintValidator;
import javax.validation.ConstraintValidatorContext;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class YearMonthValidator implements ConstraintValidator<YearMonth, String> { // 검사 기준과 검사할 값

    private String pattern; // 초기에 확인할 값
    @Override
    public void initialize(YearMonth constraintAnnotation) {
        this.pattern = constraintAnnotation.pattern();

    }

    @Override
    public boolean isValid(String value, ConstraintValidatorContext context) {
        // yyyyMM
        try {
            // DataTimeFormatter는 day까지 포함하기 때문에 전처리 해줘야 함
            LocalDate localDate = LocalDate.parse(value +"01", DateTimeFormatter.ofPattern(this.pattern));
        }catch (Exception e){

            return false;
        }
        return true;
    }
}
