async function sendMessage() {
  const input = document.getElementById("user-input").value;
  if (!input) return;

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class="user-msg">${input}</div>`;
  document.getElementById("user-input").value = "";

  const res = await fetch("http://localhost:5000/api/respond", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt: input }),
  });

  const data = await res.json();
  chatBox.innerHTML += `<div class="bot-msg">${data.reply}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}
