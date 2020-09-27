const cm = require('./cm.js')
const log = console.log

function subset(set, set_size, n, idx){


    log('size : ' + set_size, 'idx : ' + idx, 'set : ' + set, )

    if(idx === n){
        log(cm.print_arr(set, set_size));
        return;
    }

    set[set_size] = idx;

    subset(set, set_size+1, n, idx +1)
    subset(set, set_size, n, idx +1)
}

subset([], 0, 3, 0)