package com.example.pjtrestaurant.wishList.repository;

import com.example.pjtrestaurant.db.MemoryDbRepositoryAbstract;
import com.example.pjtrestaurant.wishList.Entity.WishListEntity;
import org.springframework.stereotype.Repository;

@Repository
public class WishListRepository extends MemoryDbRepositoryAbstract<WishListEntity> {
    // generic type, T가 WishListEntity가 된다.

}
