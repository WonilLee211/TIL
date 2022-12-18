package com.example.pjtrestaurant.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class SearchLocalReq {

    private String query = "";
    private int display = 1;
    private int start = 1;
    private String sort = "random";

}
