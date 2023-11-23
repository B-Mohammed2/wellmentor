// DUMMY CODE FOR SURVEY

import data from '../js/questions.json' assert { type: 'json'}
const DATA = data

const questionText = document.getElementById("question");
const answersText = document.getElementById("answers");
const answersBtns = answersText.querySelectorAll(".btn");
const display = document.getElementById("display");
const score = document.querySelector("score");

let TOTALINDEX = 0;
let SCORE = 0;

//   const html = `  <button class="btn">${questions[index].answers[0]}</button>
//           <button class="btn">${questions[index].answers[1]}</button>
//           <button class="btn">${questions[index].answers[2]}</button>
//           <button class="btn">${questions[index].answers[3]}</button>`;

document.addEventListener("DOMContentLoaded", () => {
  nextQuestion(DATA, TOTALINDEX);
});

async function nextQuestion(data, index) {
  if (data.length <= index) {
    const stateObject = { score: SCORE };
    window.history.pushState(stateObject, null, "survey/results");
    window.location.href = `results`;

    return;
  }

  console.log("second ");
  questionText.innerHTML = `<h2>${data[index].question}</h2>`;

  while (answersText.firstChild) {
    answersText.removeChild(answersText.firstChild)
  }
  const answersCount = data[index].answers.length;
  const scoreRange = 100/answersCount;

  for (var n=0; n<answersCount;n++) {
    var button = document.createElement("button");
    button.innerHTML = data[index].answers[n];
    answersText.appendChild(button);
  }

  TOTALINDEX++;
}

function storeAnswer(e) {
  const buttonValue = e.target.closest("button").value;
  console.log(buttonValue);

  SCORE += +buttonValue;

  nextQuestion(DATA, TOTALINDEX);
}

answersBtns.forEach((button) => {
  button.addEventListener("click", (e) => storeAnswer(e));
});
