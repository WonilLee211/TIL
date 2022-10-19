// // hello.js

// // console.log('hello javascript')

// function add(num1, num2) {
//     return num1 + num2
// }

// console.log(add(2, 7))
// const sub = function (num1, num2) {
//     return num1 - num2
// }
// console.log(sub(7, 2)) // 5

// const arrow1 = function (name) {
//     return 'hello ${name}'
// }

// // 1. function 키워드 삭제
// const arrow2 = (name) => {
//     return 'hello ${name}'
// }

// // 2. 인자가 1일 때 () 생략
// const arrow3 = name => {
//     return 'hello ${name}'
// }

// // 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 {} & return 삭제 가능
// const arrow4 = name => 'hello ${name}'


// const numbers = [1, 2, 3, 4, 5]
// console.log(numbers[0])
// console.log(numbers[-1])
// console.log(numbers[numbers.length - 1])


// 1.
// const colors = ['red', 'blue', 'green']
// const printClr = function (color) {
//     console.log(color)
// }
// colors.forEach(printClr)

// // 2.
// colors.forEach(function (color) {
//     console.log(color)
// })

// // 3. 
// colors.forEach( (color) => {
//     console.log(color)
// })

const numbers = [1, 2, 3, 4, 5, 6]

// const doubleEle = function (number) {
//     return number * 2
// }

// const newArry = numbers.map(doubleEle)
// // console.log(newArry)

// const newArry = numbers.map( function (number) {
//     return number * 2
// })

// const newArry = numbers.map((number) => {
//     return number * 2
// })

// const newArry = numbers.map((number) => { number * 2
// })

// const newArry = numbers.map((number) => number * 2)
// console.log(newArry)

const products = [
    { name: 'cucumber', type: 'vegetable'},
    { name: 'banana', type: 'fruit'},
]

// 함수 정의
const fruitFilter = function (product) {
    return product.type === 'fruit'
}

const fruits = products.filter(fruitFilter)
console.log(fruits)
