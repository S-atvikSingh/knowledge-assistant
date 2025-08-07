import React, { useState } from 'react';
import axios from 'axios';

const UploadBox = () => {
  const [text, setText] = useState('');
  const [status, setStatus] = useState('');

  const handleUpload = async () => {
    if (!text) return;
    try {
      await axios.post('http://localhost:8000/upload', { text });
      setStatus('Upload successful!');
      setText('');
    } catch (error) {
      setStatus('Error: ' + error.response?.data?.detail || error.message);
    }
  };

  return (
    <div className="box">
      <h2>Upload Knowledge</h2>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={4}
        placeholder="Paste knowledge content here..."
      />
      <button onClick={handleUpload}>Upload</button>
      {status && <p>{status}</p>}
    </div>
  );
};

export default UploadBox;
