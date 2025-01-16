class ChatManager {
    constructor(roomName, currentUser, receiverId) {
        this.roomName = roomName;
        this.currentUser = currentUser;
        this.receiverId = receiverId;
        this.socket = null;
        this.messageInput = document.querySelector('#messageInput');
        this.chatMessages = document.querySelector('#chatMessages');
        
        this.initializeWebSocket();
        this.setupEventListeners();
    }

    initializeWebSocket() {
        this.socket = new WebSocket(
            'ws://' + window.location.host + '/ws/chat/' + this.roomName + '/'
        );

        this.socket.onmessage = (e) => {
            const data = JSON.parse(e.data);
            this.addMessage(data.message, data.sender_id === this.currentUser);
        };

        this.socket.onclose = () => {
            console.error('Chat socket closed unexpectedly');
        };
    }

    setupEventListeners() {
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });
    }

    sendMessage() {
        const message = this.messageInput.value.trim();
        
        if (message && this.socket) {
            this.socket.send(JSON.stringify({
                'message': message,
                'receiver_id': this.receiverId
            }));
            this.messageInput.value = '';
        }
    }

    addMessage(message, isSent) {
        const messageElement = document.createElement('div');
        messageElement.className = `message ${isSent ? 'sent' : 'received'}`;
        messageElement.textContent = message;
        this.chatMessages.appendChild(messageElement);
        messageElement.scrollIntoView();
    }
}