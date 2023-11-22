const DATA = [
  {
    question:
      "How would you rate your overall emotional well-being right now on a scale of 1 to 10?",
    answers: ["ham", "cheese", "bacon", "eggs"],
  },
  {
    question:
      "How often do you feel overwhelmed or stressed in a typical week, and how intense are those feelings?",
    answers: ["ham", "cheese", "bacon", "eggs"],
  },
  {
    question:
      "On a scale of 1 to 10, how would you rate the quality of your sleep in the past month?",
    answers: ["ham", "cheese", "bacon", "eggs"],
  },
  {
    question:
      "Are there specific situations contributing to anxiety or depression for you?",
    answers: ["ham", "cheese", "bacon", "eggs"],
  },
  {
    question:
      "How comfortable are you discussing your emotions and mental health on a scale of 1 to 10?",
    answers: ["ham", "cheese", "bacon", "eggs"],
  },
  {
    question:
      "How satisfied are you with your ability to cope with daily challenges, 1 to 10?",
    answers: ["ham", "cheese", "bacon", "eggs"],
  },
  {
    question:
      "On a scale of 1 to 10, how fulfilled do you feel in your personal and professional life?",
    answers: ["ham", "cheese", "bacon", "eggs"],
  },
  {
    question:
      "How often do you engage in activities bringing joy or relaxation, and how impactful are they?",
    answers: ["ham", "cheese", "bacon", "eggs"],
  },
  {
    question:
      "On a scale of 1 to 10, how well do you understand and accept your own emotions and thoughts?",
    answers: ["ham", "cheese", "bacon", "eggs"],
  },
  {
    question:
      "Have you noticed any recent changes in mood or behavior, and how would you rate their impact on your daily life?",
    answers: ["ham", "cheese", "bacon", "eggs"],
  },
];

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
