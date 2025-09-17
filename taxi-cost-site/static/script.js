const form = document.getElementById("fareForm");
const result = document.getElementById("result");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(form).entries());
  for (const k in data) data[k] = Number(data[k]); // str -> number

  result.className = "result";
  result.textContent = "Predicting…";

  try {
    const r = await fetch("/predict", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(data),
    });
    const j = await r.json();
    if (!r.ok) {
      result.classList.add("error");
      result.textContent = `Error: ${j.error || r.statusText}`;
      return;
    }
    result.classList.add("success");
    result.textContent = `Estimated fare: $${j.prediction.toFixed(2)}`;
  } catch (err) {
    result.classList.add("error");
    result.textContent = `Network error: ${err}`;
  }
});
