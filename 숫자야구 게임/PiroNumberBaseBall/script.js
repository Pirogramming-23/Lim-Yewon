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
    inputNum = [];

    a.value = "";
    b.value = "";
    c.value = "";

    document.getElementById("results").innerHTML = "";
    document.getElementById("game-result-img").src = "";
    document.querySelector("button").disabled = false;
}

function check_numbers() {
    if(a.value.trim() === "" || b.value.trim() === "" || c.value.trim() === "") {
        a.value = "";
        b.value = "";
        c.value = "";
    }

    let inputNum = [
    parseInt(a.value),
    parseInt(b.value),
    parseInt(c.value)
    ];

    let strike = 0;
    let ball = 0;

    for(let i=0 ; i<3 ; i++) {

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

    let result = document.createElement("div");
    if(strike == 0 && ball == 0) {
        result.innerHTML = `
        <span>${inputNum.join(" ")}</span>
        <span>:</span>
        <span>O</span>
        `;
    } else {
        result.innerHTML = `
        <span>${inputNum.join(" ")}</span>
        <span>:</span>
        <span>${strike}S ${ball}B</span>
        `;
    }

    let results = document.getElementById("results");
    result.style.display = "flex";
    result.style.alignItems = "center";
    result.style.justifyContent = "space-around";
    results.appendChild(result);

    if(strike === 3) {
        document.getElementById("game-result-img").src = "success.png";
        document.querySelector("button").disabled = true;
        setTimeout(() => {
            let ret = confirm("게임을 다시 시작하겠습니까?");
            if(ret == true) init();
            else alert("게임이 종료되었습니다.")
        }, 3000);
    }
    else if(attempts.innerHTML == 0) {
        document.getElementById("game-result-img").src = "fail.png";
        document.querySelector("button").disabled = true;
        setTimeout(() => {
            let ret = confirm("게임을 다시 시작하겠습니까?");
            if(ret == true) init();
            else alert("게임이 종료되었습니다.")
        }, 3000);
    }
}

window.onload = init();



