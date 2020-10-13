// 모의고사
log = console.log

// 수포자 푸는 방법 ( math_giveup_answer)
function mg_answer(player, idx){

    const m = [   
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    const mp = m[player]
    return mp[idx%mp.length]
}

function solution(answers) {

    const scores = [0, 0, 0]

    answers.forEach((val, idx) =>{
        scores.forEach((v, j) => {
            scores[j] += val === mg_answer(j, idx) ? 1 : 0    
        })
    })

    const max_score = Math.max(...scores)

    return scores.reduce( (acc, cur, idx) => {
        if( cur === max_score) acc.push(idx+1)
        return acc
    }, [])
}

// Test mg_answer

// 수포자 푸는 방법 테스트 데이터
const mg_answer_td = [
    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5]
]

mg_answer_td.forEach((val, idx) =>{
    //val.every((v, i) => v === mg_answer(idx, i))
    val.forEach((v,j) => {
        if( v !== mg_answer(idx, j)) log(i, j, v,mg_answer(idx, j))
    })
})


// Test solution

const test_data = [ 
    [[1,2,3,4,5], [1]],
    [[1,3,2,4,2], [1,2,3]],
]

function arrayEquals(a, b) {
    return Array.isArray(a) &&
        Array.isArray(b) &&
        a.length === b.length &&
        a.every((val, index) => val === b[index]);
}

test_data.forEach(element => {

    const data   = element[0]
    const result = element[1]

    const data_rst = solution(data)

    if ( !arrayEquals(data_rst, result)) {
        console.log("=== error ===")
        console.log(data)
        console.log(result)
        console.log(data_rst)
    }
});