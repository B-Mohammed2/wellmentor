const stateObject = window.history.state;

const score = stateObject ? stateObject.score : null;

document.addEventListener("DOMContentLoaded", () => {
  const scoreElement = document.getElementById("score");
  scoreElement.innerHTML = score;
});
