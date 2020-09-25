
const set = [];
const log = console.log
function print_arr(arr, size){
    const rst = [];
    for(let i = 0; i<size; i++){
        rst.push(arr[i]);
    }

    log( rst.join(' '));
}








function main(){
    print_arr([1, 2, 3, 4], 0)
    print_arr([1, 2, 3, 4], 1)
    print_arr([1, 2, 3, 4], 2)
    print_arr([1, 2, 3, 4], 3)
    print_arr([1, 2, 3, 4], 4)

}


main()