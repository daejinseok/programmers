function solution(clothes) {

    const d = {};

    clothes.forEach( e => {
        d[e[1]] = (d[e[1]]||0) + 1;
    })

    return Object.keys(d).reduce((r, e) => (d[e]+1)*r,1) -1;
}

const data_list = [
    [[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]], 5],
    [[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]], 3]
]

data_list.forEach(element => {

    const data = element[0]
    const rst = element[1]

    const data_rst = solution(data)

    if (rst != data_rst) {
        console.log("error")
        console.log(data)
        console.log(data_rst)
    }
});

