// const nums = [1,2,3,4,5,6,7,8]
// for (num of nums) {
//   console.log(num, typeof num)
// }
function palindrome(str) {
    
    
    let n = str.length

    for (let i = 0; i <= parseInt(n/2); i++) {
        if (str[i] !== str[n - 1 - i]) {
            console.log(false)
            return
        }
    }
    console.log(true)
    return

  }
palindrome('level')
palindrome('hi')