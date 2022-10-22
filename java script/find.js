const avengers = [
    { name: 'Tony stark', age: 45},
    { name: 'steve rogers', age: 32},
    { name: 'Thor', age: 40},
]
const avenger = avengers.find((avenger) => {
    return avenger.name === 'Tony stark'
})

console.log(avenger)