// 모의고사

// 수포자별 푸는 방법
function pm(player, idx){

    const m = [   
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    const mp = m[player]
    return mp[idx%mp.length]
}

const rp1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
const rp2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
const rp3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5]

function equals(rst, p){
    for(let i = 0, len = rst.length; i < len; i++){
        if (rst[i] != pm(p,i)) console.log(i, rst[i], pm(p,i))
    }    
}

equals(rp1, 0)
equals(rp2, 1)
equals(rp3, 2)

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

    return players.reduce( (acc, cur, idx) => {
        if( cur === max_score) acc.push(idx+1)
        return acc
    }, [])

}


const data_list = [ 
    [[1,2,3,4,5], [1]],
    [[1,3,2,4,2], [1,2,3]],
]

function arrayEquals(a, b) {
    return Array.isArray(a) &&
        Array.isArray(b) &&
        a.length === b.length &&
        a.every((val, index) => val === b[index]);
}

// data_list.forEach(element => {

//     const data   = element[0]
//     const result = element[1]

//     const data_rst = solution(data)

//     if ( !arrayEquals(data_rst, result)) {
//         console.log("=== error ===")
//         console.log(data)
//         console.log(result)
//         console.log(data_rst)
//     }
// });