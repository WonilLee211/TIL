package com.example.springcalculatortdd.controller;

import com.example.springcalculatortdd.component.Calculator;
import com.example.springcalculatortdd.component.ICalculator;
import com.example.springcalculatortdd.dto.Req;
import com.example.springcalculatortdd.dto.Res;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@RequiredArgsConstructor
public class CalculatorApiController {

    private final Calculator calculator;

    @GetMapping("/sum")
    public int sum(@RequestParam int x, @RequestParam int y){
        return calculator.sum(x, y);
    }
//    @GetMapping("/minus")
    @PostMapping("/minus")
    public Res minus(@RequestBody Req req){
        int result = calculator.minus(req.getX(), req.getY());

        Res res = new Res();
        res.setResult(result);
        res.setResponse(new Res.Body());

        return res;

    }

}
