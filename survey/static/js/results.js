// TEMPORARY CODE FOR PUSHING SCORE STATE ONTO RESULTS PAGE

const stateObject = window.history.state;

const score = stateObject ? stateObject.score : null;

document.addEventListener("DOMContentLoaded", () => {
  const physicalElement = document.getElementById("physical");
  const depressionElement = document.getElementById("depression");
  const relationshipsElement = document.getElementById("relationships");
  const mentalElement = document.getElementById("mental");
  const anxietyElement = document.getElementById("anxiety");
  const professionalElement = document.getElementById("professional");

  physicalElement.innerText = score.physical;
  depressionElement.innerText = score.depression;
  relationshipsElement.innerText = score.relationships;
  mentalElement.innerText = score.mental;
  anxietyElement.innerText = score.anxiety;
  professionalElement.innerText = score.professional;
});
