const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(express.static('public'));

// Route to handle the form submission
app.post('/predict', async (req, res) => {
    try {
        const { text } = req.body;

        if (!text || text.trim() === "") {
            return res.status(400).json({ error: "Input text cannot be empty" });
        }

        const response = await axios.post('http://127.0.0.1:8000/predict', { text });
        res.json(response.data);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: "Error processing the request" });
    }
});

app.listen(port, () => {
    console.log(`Frontend running at http://localhost:${port}`);
});
