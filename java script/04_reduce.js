const numbers = [90, 80, 70, 100]

const sumNum = numbers.reduce( function (result, number) {
    return result + number
}, 0)
console.log(sumNum)

const sumNum = numbers.reduce((result, number) => {
    return result + number
}, 0)
console.log(sumNum)

const sumNum = numbers.reduce((result, number) => result + number, 0)
console.log(sumNum)