async function sendMessage() {
    const inputField = document.getElementById('userInput');
    const message = inputField.value.trim();
    if (!message) return;

    const chatBox = document.getElementById('chatBox');

    // Display User Message
    const userDiv = document.createElement('div');
    userDiv.className = 'message user-msg';
    userDiv.innerHTML = `<div class="msg-content">${message}</div>`;
    chatBox.appendChild(userDiv);

    inputField.value = '';
    chatBox.scrollTop = chatBox.scrollHeight;

    // Display Loading indicator
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'message bot-msg';
    loadingDiv.innerHTML = `<div class="msg-content">Thinking...</div>`;
    chatBox.appendChild(loadingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const res = await fetch('/api/chat/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: message })
        });
        const data = await res.json();
        
        // Remove loading state and show response
        loadingDiv.remove();
        const botDiv = document.createElement('div');
        botDiv.className = 'message bot-msg';
        botDiv.innerHTML = `<div class="msg-content">${data.response || data.message}</div>`;
        chatBox.appendChild(botDiv);
    } catch (err) {
        loadingDiv.remove();
        const errDiv = document.createElement('div');
        errDiv.className = 'message bot-msg';
        errDiv.innerHTML = `<div class="msg-content">Error processing request. Check connection or API key.</div>`;
        chatBox.appendChild(errDiv);
    }
    chatBox.scrollTop = chatBox.scrollHeight;
}