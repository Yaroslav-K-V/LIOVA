const chat = document.getElementById('chat');
const inputForm = document.getElementById('inputForm');
const userInput = document.getElementById('userInput');
const tokenCountSpan = document.getElementById('tokenCount');
const costSpan = document.getElementById('cost');

let totalTokens = 0;

function approximateTokens(text) {
    // simple approximation: one token per 4 characters
    return Math.ceil(text.trim().length / 4);
}

function updateStats() {
    tokenCountSpan.textContent = totalTokens;
    const cost = (totalTokens / 1000) * 0.002; // $0.002 per 1K tokens
    costSpan.textContent = cost.toFixed(4);
}

function addMessage(text, cls) {
    const div = document.createElement('div');
    div.className = 'message ' + cls;
    div.textContent = text;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

inputForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const text = userInput.value;
    if (!text.trim()) return;
    addMessage(text, 'user');
    const tokens = approximateTokens(text);
    totalTokens += tokens;
    updateStats();
    userInput.value = '';
    addMessage('Received ' + tokens + ' tokens.', 'system');
});
