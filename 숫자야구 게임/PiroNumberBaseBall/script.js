let attempts = document.getElementById("attempts");

let a = document.getElementById("number1");
let b = document.getElementById("number2");
let c = document.getElementById("number3");
let inputs = document.getElementsByClassName("input-field");
let inputNum = [];
for(let i=0 ; i<3 ; i++) {
    inputNum.push(inputs[i].value);
}

let randNum = [];

function randomNum() {
    let r = [];
    while(r.length < 3) {
        let i = Math.floor(Math.random() * 10);
        if (r.includes(i)) continue;
        r.push(i);
    }
    return r;
}

function init() {
    attempts.innerHTML = 9;
    randNum = randomNum();
    console.log(randNum);
    inputNum = [];
}

function check_numbers() {
    if(a.value.trim() === "" || b.value.trim() === "" || c.value.trim() === "") {
        a.value = "";
        b.value = "";
        c.value = "";
        console.log("no!!")
    }

    let inputNum = [
    parseInt(a.value),
    parseInt(b.value),
    parseInt(c.value)
    ];

    let strike = 0;
    let ball = 0;

    for(let i=0 ; i<3 ; i++) {
        console.log(inputNum);
        console.log(inputNum[i]);
        console.log(randNum[i]);

        if(inputNum[i] == randNum[i]) {
            strike++;
        }

        else if(randNum.includes(inputNum[i])) {
            ball++;
        }
        a.value = "";
        b.value = "";
        c.value = "";
    }

    attempts.innerHTML -= 1;

    console.log(strike);
    console.log(ball);



    if(strike === 3) {
        document.getElementById("game-result-img").src = "success.png";
        document.querySelector("button").disabled = true;
    }
    else if(attempts.innerHTML == 0) {
        document.getElementById("game-result-img").src = "fail.png";
        document.querySelector("button").disabled = true;
    }
}

window.onload = init();



