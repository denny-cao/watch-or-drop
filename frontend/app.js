const shows = ["Crash Landing on You", "Stranger Things", "Skating into Love", "My Love From Another Star", "Breaking Bad"];
let currentIndex = 0;
const history = []; // hold { title, decision }

function updateCard() {
  if (currentIndex < shows.length) {
    document.getElementById("show-card").innerText = shows[currentIndex];
  } else {
    document.getElementById("show-card").innerText = "All Done!";
    document.getElementById("watch-btn").disabled = true;
    document.getElementById("drop-btn").disabled = true;
  }
}

document.getElementById("watch-btn").addEventListener("click", function () {
  history.push({ title: shows[currentIndex], decision: "watch" });
  currentIndex++;
  updateCard();
});

document.getElementById("drop-btn").addEventListener("click", function () {
  history.push({ title: shows[currentIndex], decision: "drop" });
  currentIndex++;
  updateCard();
});

updateCard();
