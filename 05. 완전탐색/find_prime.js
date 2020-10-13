
// 소수확인
const isPrime = num => {
    const end = Math.sqrt(num)
    for(let i = 2; i < end; i++)
      if(num % i === 0) return false;
    return num > 1;
}

const addHead = (arr, head) => arr.map( cur => head + cur )

function makeGray(n){
    if( n === 1) return ['0', '1']
    const m1g = makeGray(n-1)
    return addHead(m1g, 0).concat(addHead(m1g, 1))
}






// === test =========================================================

const makeGray_test_data = [
    ['0', '1'],
    ['00', '01', '10', '11'],
    ['000', '001', '010', '011', '100', '101', '110', '111'],
    ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
    '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
]

function arrayEquals(a, b) {
    return Array.isArray(a) &&
        Array.isArray(b) &&
        a.length === b.length &&
        a.every((val, index) => val === b[index]);
}

log = console.log

makeGray_test_data.forEach( (val, idx) => {

    const result = makeGray(idx+1)

    log(idx)
    log(result)

    if ( !arrayEquals(val, result)) {
        log("=== error ===")
        log(idx)
        log(val)
        log(result)
    }
});