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

async function nextQuestion(questions, index) {
  if (questions.length <= index) {
    const stateObject = { score: SCORE };
    window.history.pushState(stateObject, null, "survey/results");
    window.location.href = `results`;

    return;
  }

  console.log("second ");
  questionText.innerHTML = `<h2>${questions[index].question}</h2>`;

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
