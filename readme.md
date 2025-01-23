# 8-K Filing Analyzer 📊

A modern web application that analyzes SEC 8-K filings using AI to provide concise, actionable summaries of company events.

🔗 **Live Demo**: [8-K Analyzer](https://eightkanalyzer.onrender.com/)

## 🌟 Features

- **Real-time 8-K Analysis**: Fetches and analyzes the latest 8-K filings from SEC EDGAR database
- **AI-Powered Summaries**: Uses Gemini AI to generate concise, readable summaries
- **Multiple View Options**: 
  - 📊 Table View for structured data analysis
  - 📝 Card View for easy reading
- **Dark Mode Interface**: Modern, eye-friendly design
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.9
- **AI Model**: Google Gemini AI
- **Data Source**: SEC EDGAR Database
- **Containerization**: Docker
- **Deployment**: Render

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Docker (optional)
- Google API Key for Gemini AI

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd 8k-analyzer
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Add your Google API key to .env file
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

### 🐳 Docker Setup

1. **Build and run using Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Or using Docker directly**
   ```bash
   docker build -t 8k-analyzer .
   docker run -p 8501:8501 --env-file .env 8k-analyzer
   ```

## 📦 Project Structure
8k-analyzer/
├── streamlit_app.py # Main Streamlit application
├── agent.py # AI processing logic
├── edgar_connector.py # SEC EDGAR integration
├── models.py # Data models
├── config.py # Configuration settings
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
├── docker-compose.yml # Docker Compose configuration
└── README.md # Project documentation


## 🔑 Environment Variables

Create a `.env` file with the following:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

## 🎯 Usage

1. Visit the application URL.
2. Enter a stock ticker (e.g., AAPL, MSFT, ORCL).
3. Click "Analyze Filings".
4. View the AI-generated summaries in either Table or Card view.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini AI for natural language processing.
- SEC EDGAR for providing financial filing data.
- Streamlit for the amazing web framework.
- Render for hosting the application.

## 📧 Contact

For any queries or suggestions, please reach out to:
- Email: Subhadipmondal789@gmail.com
- LinkedIn: [https://www.linkedin.com/in/subhadipmondal89]

