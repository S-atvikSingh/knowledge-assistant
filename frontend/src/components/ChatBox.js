import React, { useState } from 'react';
import axios from 'axios';

const ChatBox = () => {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!query) return;
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:8000/chat', { query });
      setResponse(res.data.response);
    } catch (error) {
      setResponse("Error: " + error.response?.data?.detail || error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="box">
      <h2>Ask a Question</h2>
      <textarea
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        rows={4}
        placeholder="Type your question..."
      />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? 'Asking...' : 'Ask'}
      </button>
      {response && (
        <div className="response-box">
          <strong>Response:</strong>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
};

export default ChatBox;
