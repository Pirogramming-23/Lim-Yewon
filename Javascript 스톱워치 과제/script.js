const startBtn = document.getElementById("start");
const stopBtn = document.getElementById("stop");
const resetBtn = document.getElementById("reset");
const trashbinBtn = document.getElementById("trash-bin");
const selectAllCheckbox = document.getElementById("all-checkbox");

let startTime;
let elapsed = 0;
let timerId;
let running = false;

startBtn.onclick = start;
stopBtn.onclick = stop;
resetBtn.onclick = reset;

function timeSetting(ms) {
    const totalSeconds = ms / 1000;
    const textContent = totalSeconds.toFixed(2).replace('.', ' : ').padStart(7, '0');
    document.getElementById("stopwatch-time").textContent = textContent;
}

function start() {
    if(running) return;
    running = true;
    startTime = Date.now() - elapsed;
    timerId = setInterval(() => {
        elapsed = Date.now() - startTime;
        timeSetting(elapsed);
    }, 10);
}

function stop() {
    if(!running) return;
    running = false;
    clearInterval(timerId);

    const totalSeconds = elapsed / 1000;
    const displaySeconds = totalSeconds.toFixed(2).replace('.', ' : ').padStart(7, '0');

    const recordElement = document.createElement("div");
    recordElement.className = "record-item";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.className = "checkbox";

    const text = document.createElement("div");
    text.className = "record-body-time";
    text.textContent = `${displaySeconds}`;

    recordElement.appendChild(checkbox);
    recordElement.appendChild(text);

    document.getElementById("record-body").appendChild(recordElement);

    attachCheckbox(checkbox);
}

function reset() {
    running = false;
    clearInterval(timerId);
    elapsed = 0;
    timeSetting(0);
}

trashbinBtn.onclick = function () {
    const checkboxes = document.querySelectorAll(".checkbox");
    checkboxes.forEach((checkbox) => {
        if (checkbox.checked) {
            checkbox.parentElement.remove();
        }
    });
};

selectAllCheckbox.addEventListener("change", function () {
    const allCheckboxes = document.querySelectorAll(".checkbox");
    allCheckboxes.forEach((c) => {
        if (c !== selectAllCheckbox) {
            c.checked = selectAllCheckbox.checked;
        }
    });
});

function attachCheckbox(checkbox) {
    checkbox.addEventListener("change", () => {
        const allCheckboxes = document.querySelectorAll(".checkbox");
        const targetCheckboxes = Array.from(allCheckboxes).filter(c => c !== selectAllCheckbox);

        const allChecked = targetCheckboxes.every(c => c.checked);
        selectAllCheckbox.checked = allChecked;
    });
}