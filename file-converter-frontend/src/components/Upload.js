import React, { useState } from "react";
import axios from "axios";

const Upload = ({ token }) => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return alert("Please select a file");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://127.0.0.1:5000/upload", formData, {
        headers: { Authorization: `Bearer ${token}` },
      });
      alert("File uploaded! URL: " + response.data.file_url);
    } catch (error) {
      alert("Upload failed");
    }
  };

  return (
    <div className="container mt-5">
      <h2>Upload File</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default Upload;
