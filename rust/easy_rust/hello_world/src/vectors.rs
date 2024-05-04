fn main() {
    create_vec1();
    create_vec2();
}

fn create_vec1() {
    
    let mut my_vec = Vec::new();
    // the compiler doesn't know the type of item inside the Vec.
    push_item_into_vec(&mut my_vec);
    // now the compiler knows it
    println!("{:?}", my_vec);
}

fn create_vec2() {
    let mut my_vec: Vec<String> = Vec::new(); // the compiler knows the type.
    
    push_item_into_vec(&mut my_vec);
    
    println!("{:?}", my_vec);
}

fn push_item_into_vec(vec_arg : &mut Vec<String>) {
    let name1 = String::from("Valor");
    let name2 = String::from("programmer");

    vec_arg.push(name1);
    vec_arg.push(name2);
}