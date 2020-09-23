
const set = [];
const log = console.log
function print_arr(arr, size){
    const rst = [];
    for(let i = 0; i<size; i++){
        rst.push(arr[i]);
    }

    log( rst.join(' '));
}

function comb(set, set_size, n, k, index){
    if(k === 0){
        print_arr(set, set_size);
    } else if ( index === n) {
        return;
    }
    else {
        set[set_size] = index;
        comb(set, set_size + 1, n, k - 1, index+1)
        comb(set, set_size, n, k, index+1)
    }
}

function main(){
    //comb(set, 0, 5, 3, 0);
    comb(set, 0, 5, 1, 0);
}


main()