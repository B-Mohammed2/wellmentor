// TEMPORARY CODE FOR PUSHING SCORE STATE ONTO RESULTS PAGE

const stateObject = window.history.state;

const score = stateObject ? stateObject.score : null;

document.addEventListener("DOMContentLoaded", () => {
  const scoreElement = document.getElementById("score");

  const html = `
  <ul style="list-style: none">
      <li>physical : ${score.physical}</li>
      <li>depression : ${score.depression}</li>
      <li>relationships : ${score.relationships}</li>
      <li>mental : ${score.mental}</li>
      <li>anxiety : ${score.anxiety}</li>
      <li>professional : ${score.professional}</li>

    </ul>`;

  scoreElement.innerHTML = html;
});
