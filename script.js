document.addEventListener('DOMContentLoaded', function() {
    const chatMessages = document.getElementById('chat-messages');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    const fileInput = document.getElementById('file-input');
    const fileNameDisplay = document.getElementById('file-name');
    let currentFile = null;

    // Handle file selection
    fileInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            currentFile = file;
            fileNameDisplay.textContent = `Selected file: ${file.name}`;
            
            // Add message about file selection
            addMessage(`File "${file.name}" selected. You can now ask questions about the data.`, 'bot');
        }
    });

    // Handle sending messages
    sendButton.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const message = messageInput.value.trim();
        if (!message) return;

        // Add user message to chat
        addMessage(message, 'user');
        messageInput.value = '';

        // Show loading indicator
        const loadingMessage = addMessage('Thinking...', 'bot');
        loadingMessage.classList.add('loading');

        // Prepare the request based on whether a file is selected
        if (currentFile) {
            const formData = new FormData();
            formData.append('file', currentFile);
            formData.append('message', message);

            // Send message to server with file
            fetch('http://localhost:5000/chat', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Remove loading message
                loadingMessage.remove();
                
                if (data.error) {
                    addMessage(`Error: ${data.error}`, 'bot');
                } else {
                    addMessage(data.response, 'bot');
                }
            })
            .catch(error => {
                // Remove loading message
                loadingMessage.remove();
                
                addMessage('Sorry, there was an error processing your request.', 'bot');
                console.error('Error:', error);
            });
        } else {
            // Regular chat without file
            fetch('http://localhost:5000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            })
            .then(response => response.json())
            .then(data => {
                // Remove loading message
                loadingMessage.remove();
                
                if (data.error) {
                    addMessage(`Error: ${data.error}`, 'bot');
                } else {
                    addMessage(data.response, 'bot');
                }
            })
            .catch(error => {
                // Remove loading message
                loadingMessage.remove();
                
                addMessage('Sorry, there was an error processing your request.', 'bot');
                console.error('Error:', error);
            });
        }
    }

    function addMessage(content, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.textContent = content;
        
        messageDiv.appendChild(messageContent);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        return messageDiv;
    }
}); 