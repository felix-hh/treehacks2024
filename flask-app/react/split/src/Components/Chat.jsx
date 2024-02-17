import React from 'react';

const Chat = () => {
  return (
    <div className="chat-container">
      <div className="chat-header">Chat</div>
      <div className="chat-messages">
        <div className="message">User 1: Hello!</div>
        <div className="message">User 2: Hi there!</div>
        <div className="message">User 1: How are you?</div>
        <div className="message">User 2: I'm doing well, thanks!</div>
      </div>
      <div className="chat-input">
        <input type="text" placeholder="Type your message..." />
        <button>Send</button>
      </div>
    </div>
  );
}

export default Chat;
