function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    
    if (message === '') return;

    // Add user message to chat
    addMessageToChat('user', message);
    input.value = '';

    // Send message to server
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        // Add analyst response to chat
        addMessageToChat('analyst', data.response);
        
        // Update metrics
        updateMetrics(data.metrics);
        
        // Update analyst state
        updateAnalystState(data.analyst_state);
    });
}

function addMessageToChat(sender, message) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    if (sender === 'analyst') {
        messageDiv.textContent = message[0]; // Start with first character
        const typeWriter = (text, index) => {
            if (index < text.length) {
                messageDiv.textContent = text.substring(0, index + 1);
                chatMessages.scrollTop = chatMessages.scrollHeight;
                setTimeout(() => typeWriter(text, index + 1), 10);
            }
        };
        typeWriter(message, 1); // Start from second character
    } else {
        messageDiv.textContent = message;
    }
    
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function updateMetrics(metrics) {
    document.getElementById('analyses-count').textContent = metrics.analyses_completed;
    document.getElementById('insights-count').textContent = metrics.insights_generated;
    document.getElementById('sessions-count').textContent = metrics.chat_sessions;
}

function updateAnalystState(state) {
    document.getElementById('current-focus').textContent = state.current_focus;
    document.getElementById('confidence-level').textContent = state.confidence_level + '%';
    document.getElementById('processing-mode').textContent = state.processing_mode;
}

// Add event listener for Enter key in input field
document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});
