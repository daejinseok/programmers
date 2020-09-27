function print_arr(arr, arr_len){
    const rst = []

    for(let i = 0; i < arr_len; i++){
        rst.push(arr[i])
    }
    
    return rst.join(' ');
}


exports.print_arr = print_arr;