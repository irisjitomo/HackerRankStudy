// Example: suppose we want to write a function that sums up nums from 1
// up to, including, some number n

// first function
function addUpTo(n){
    total = 0
    for (let i = 1; i <= n; i++){
        total += i
    }
    return total
}

// second function
function addUpTo(m){
    return m * (m + 1) / 2;
}