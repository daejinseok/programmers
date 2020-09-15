// 모의고사

function p1(n){
    return n%5 + 1
}

function p2(n){
    if ( n % 2 == 0) return 2
    const n8 = ( n % 8 + 1 ) / 2
    return ( n8 == 1) ? 1 : n8 + 1
}

function p3(n){
    const n10 = parseInt( n % 10 / 2 ) 
    if ( n10 === 0 ) return 3
    return ( n10 > 2 ) ? n10+1 : n10
}

// function equals( rst, f){
//     for(let i = 0, len = rst.length; i < len; i++){
//         if (rst[i] != f(i)) console.log(rst[i], f(i))
//     }    
// }

// const rp1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
// const rp2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
// const rp3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5]

// equals( rp1, p1)
// equals( rp2, p2)
// equals( rp3, p3)

//log = console.log

function solution(answers) {

    const players = [0, 0, 0]
    const method  = [p1, p2, p3]

    for(let i = 0, end = answers.length; i < end; i++){
        for(const p in players){
            //log(p)
            players[p] += (method[p](i) === answers[i])? 1 : 0
        }
    }

    const max_score = Math.max(...players)
    //log(max_score)

    const result = []

    for(let i = 0, end = players.length; i < end; i++){
        if (max_score === players[i]) result.push(i+1)
    }

    return result
}


const data_list = [ 
    [[1,2,3,4,5], [1]],
    [[1,3,2,4,2],	[1,2,3]],
]

function isEquare(a, b){

    if (a.length !== b.length) return false;

    for(let i=0, len=a.length; i<len; i++){
        if( a[i] !== b[i]) return false;
    }
    return true;
}

data_list.forEach(element => {

    const data   = element[0]
    const result = element[1]

    // console.log(data)
    // console.log(result)    

    const data_rst = solution(data)

    if ( !isEquare(data_rst, result)) {
        console.log("=== error ===")
        console.log(data)
        console.log(result)
        console.log(data_rst)
    }
});