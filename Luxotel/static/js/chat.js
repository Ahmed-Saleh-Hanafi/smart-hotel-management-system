const chatMessages = document.getElementById('chatMessages');
  const chatForm = document.getElementById('chatForm');
  const chatInput = document.getElementById('chatInput');
  const closeBtn = document.getElementById('closeBtn');

  // Scroll chat to bottom on load
  window.onload = () => {
    chatMessages.scrollTop = chatMessages.scrollHeight;
  };

  // Close chat (just hide container)
  closeBtn.addEventListener('click', () => {
    document.querySelector('.chatbot-container').style.display = 'none';
  });

  // Simulate sending a message - for demo, just add user message and a bot reply
  chatForm.addEventListener('submit', e => {
    e.preventDefault();
    const message = chatInput.value.trim();
    if (!message) return;

    // Add user message
    const userMsg = document.createElement('article');
    userMsg.className = 'message user';
    userMsg.setAttribute('tabindex', '0');

    const imageurl  = "{% static 'img/profile.webp'%}";
    const userAvatar = document.createElement('img');
    userAvatar.className = 'avatar';
    userAvatar.src = imageurl
    userAvatar.alt = "User's profile picture";

    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    bubble.textContent = message;

    userMsg.appendChild(userAvatar);
    userMsg.appendChild(bubble);
    chatMessages.appendChild(userMsg);

    chatInput.value = '';
    chatInput.focus();

    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Simulate bot reply after delay
    setTimeout(() => {
      const botMsg = document.createElement('article');
      botMsg.className = 'message bot';
      botMsg.setAttribute('tabindex', '0');

      const botIcon = document.createElement('div');
      botIcon.className = 'bot-icon';
      botIcon.setAttribute('aria-hidden', 'true');
      botIcon.innerHTML = `
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
          <circle cx="12" cy="12" r="10" fill="#5a22d1"/>
          <rect x="7" y="10" width="10" height="4" rx="2" ry="2" fill="white"/>
          <circle cx="9" cy="12" r="1" fill="#5a22d1"/>
          <circle cx="15" cy="12" r="1" fill="#5a22d1"/>
          <rect x="11" y="6" width="2" height="2" rx="1" ry="1" fill="white"/>
        </svg>
      `;

      const botBubble = document.createElement('div');
      botBubble.className = 'bubble';
      botBubble.textContent = "Sorry, I'm a demo chatbot and cannot respond right now.";

      botMsg.appendChild(botIcon);
      botMsg.appendChild(botBubble);

      chatMessages.appendChild(botMsg);
      chatMessages.scrollTop = chatMessages.scrollHeight;
      botMsg.focus();
    }, 1000);
  });

  document.addEventListener("DOMContentLoaded", function() {
    const chatBtn = document.getElementById("chat-btn");
    const chatbot_container = document.querySelector(".chatbot-container");

    chatBtn.addEventListener("click", function(e) {
        e.preventDefault();

        // Apply popup styles directly via JS
        chatbot_container.style.display = "block";
        chatbot_container.style.position = "fixed";
        chatbot_container.style.top = "50%";
        chatbot_container.style.left = "50%";
        chatbot_container.style.transform = "translate(-50%, -50%)";
        chatbot_container.style.zIndex = "1000";
        chatbot_container.style.backgroundColor = "white";



        document.querySelector('.chatbot-container').style.display = 'block';


    });
});
