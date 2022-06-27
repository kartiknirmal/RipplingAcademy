let currPlayer = "X";
let gameOn = true;
let playerXScore = 0;
let playerOScore = 0;
let resultString = "";

let sqrArr = Array.from(document.querySelectorAll(".sqr"));
let XScore = document.querySelector(".XScore");
let OScore = document.querySelector(".OScore");
let result = document.querySelector(".result");
let turn = document.querySelector(".turn");
let resetBtn = document.querySelector(".reset-btn");


const switchPlayer = () =>{
    if(currPlayer == "X"){
        turn.innerHTML = "O's turn";
        return "O";
    }
    else{
        turn.innerHTML = "X's turn";
        return "X";
    }
}

let winState = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

let gameTie;

const updateResult = () =>{
    winState.forEach(e => {
        if(sqrArr[e[0]].innerHTML != ""){
            if(sqrArr[e[0]].innerHTML == sqrArr[e[1]].innerHTML && sqrArr[e[0]].innerHTML == sqrArr[e[2]].innerHTML){
                if(currPlayer == "X"){
                    playerXScore = playerXScore + 1;
                    resultString = "Player X wins";
                    XScore.innerHTML = playerXScore;
                }
                else{
                    playerOScore = playerOScore + 1;
                    resultString = "Player O wins";
                    OScore.innerHTML = playerOScore;
                }
                gameOn = false;
                result.innerHTML = resultString;
            }
        }
    })
    if(gameOn){
        gameTie = true;
        sqrArr.forEach(e => {
            if(e.innerHTML == ""){
                gameTie = false;
            }
        });
        if(gameTie){
            resultString = "Tie";
            gameOn = false;
            result.innerHTML = resultString;
        }
    }
}

sqrArr.forEach(e =>{
    e.addEventListener('click', f=>{
        if(gameOn){
            if(f.target.innerHTML == ""){
                f.target.innerHTML = currPlayer;
                updateResult();
                currPlayer = switchPlayer();
            }
        }
    })
})

resetBtn.addEventListener('click', () => {
    sqrArr.forEach(e => {
        e.innerHTML = "";
    })
    currPlayer = "X";
    turn.innerHTML = "X's turn";
    gameOn = true;
    resultString = "";
    result.innerHTML = resultString;
})