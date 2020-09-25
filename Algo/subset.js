const log = console.log

function print_arr(arr, arr_len){
    const rst = []

    for(let i = 0; i < arr_len; i++){
        rst.push(arr[i])
    }
    log( rst.join(' '));
}

//print_arr([1,2,3,4], 3)


// const N = 4
// for (let i = 0; i<N; i++){
//     set.push(i);
// }

//log(set);
let set = [];
function subset(pset, set_size, n, idx){
    if(idx === n){
        print_arr(pset, set_size);
        return;
    }

    pset[set_size] = idx;

    subset(pset, set_size+1, n, idx +1)
    subset(pset, set_size, n, idx +1)
}

subset(set, 0, 3, 0)