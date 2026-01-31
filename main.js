function generate() {
  const topic = document.getElementById("topic").value;
  const mode = document.getElementById("mode").value;

  fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ topic, mode })
  })
  .then(res => res.json())
  .then(data => {
    const output = document.getElementById("output");
    output.innerHTML = "";

    if (data.audio) {
      output.innerHTML = `
        <p>🔊 Generated Audio:</p>
        <audio controls autoplay>
          <source src="${data.audio}" type="audio/mpeg">
          Your browser does not support audio playback.
        </audio>
        <br>
        <a href="${data.audio}" download>⬇ Download Audio</a>
      `;
    } else {
     const rawContent = data.result || data.prompt || "No output generated.";
output.innerHTML = marked.parse(rawContent);
    }
  })
  .catch(err => console.error(err));
}
