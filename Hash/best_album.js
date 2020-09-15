function solution(genres, plays) {

    const dic = {}

    for(let i = 0, len = genres.length; i < len; i++){

        const key = genres[i];
        const play_count = plays[i];

        if ( !dic[key] ){
            dic[key] = { 
                play : play_count,
                list :[{No : i, play : play_count}]
            }
        } else {
            dic[key].play += play_count;
            dic[key].list.push({No : i, play : play_count})
        }
    }

    const stat_sort_list = Object.keys(dic).sort((a,b) => dic[b].play - dic[a].play);

    for(const k in dic){
        dic[k].list = dic[k].list.sort((a,b) => b.play - a.play)
        //console.log("genres_play_count : ", dic[k].play)
        //console.log(dic[k].list)
    }

    //console.log(stat_sort_list);
    var answer = [];
    stat_sort_list.forEach( k => {
        //console.log(k)
        const song_list = dic[k].list

        for( let i = 0, len = (song_list.length > 1)? 2:1; i < len; i++){
            //console.log(song_list[i])
            answer.push(song_list[i].No)
        }
    })
    return answer;
}

const data_list = [{
    genres : ["classic", "pop", "classic", "classic", "pop"],
    plays :[500, 600, 150, 800, 2500],
    result : [4, 1, 3, 0]
},
{
    genres : ["classic", "pop", "classic", "classic", "pop"],
    plays :[100, 600, 1600, 1400, 2500],
    result : [2, 3, 4, 1]
},
{
    genres : ["classic", "pop", "classic", "kpop", "classic", "pop"],
    plays :[100, 600, 1600, 300, 1400, 2500],
    result : [2, 4, 5, 1, 3]
},]

function isEquare(a, b){
    for(let i=0, len=a.length; i<len; i++){
        if( a[i] !== b[i]) return false;
    }

    return true;
}

data_list.forEach(e => {

    const genres = e.genres;
    const plays = e.plays;
    const result = e.result;

    const sol_reuslt = solution(genres, plays);

    if (!isEquare(result, sol_reuslt)) {
        console.log("=== error ===");
        console.log(e);
        console.log("result : " + sol_reuslt);
    }
});

