// TEMPORARY CODE FOR PUSHING SCORE STATE ONTO RESULTS PAGE

const stateObject = window.history.state;

const score = stateObject ? stateObject.score : null;

document.addEventListener("DOMContentLoaded", () => {
  const scoreElement = document.getElementById("score");

  console.log(score);
  scoreElement.innerHTML = score;
});
