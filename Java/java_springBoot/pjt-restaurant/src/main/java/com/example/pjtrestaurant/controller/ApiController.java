package com.example.pjtrestaurant.controller;

import com.example.pjtrestaurant.wishList.dto.WishListDto;
import com.example.pjtrestaurant.wishList.service.WishListService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j
@RestController
@RequestMapping("/api/food")
@RequiredArgsConstructor
public class ApiController {
    private final WishListService wishListService;
    @GetMapping("/search")
    public WishListDto search(@RequestParam String query){
        return wishListService.search(query);
    }

    @PostMapping("")
    public WishListDto add(@RequestBody WishListDto wishListDto){
      log.info("{}", wishListDto);

      return wishListService.add(wishListDto);
    }
    @GetMapping("/all")
    public List<WishListDto> findAll(){
        return wishListService.findAll();
    }

    @DeleteMapping("/{index}")
    public void delete(@PathVariable Integer index){
        wishListService.delete(index);
    }

    @PostMapping("/{index}")
    public void addVisit(@PathVariable Integer index){
        wishListService.addVisit(index);
    }


}
