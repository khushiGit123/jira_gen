# Synovus AI SDLC - Multi-Agent Business Analysis System

## Overview

Synovus AI SDLC is a sophisticated multi-agent business analysis system that automates the Software Development Lifecycle process of converting business requirements into structured project artifacts. The system employs three specialized AI agents working in sequence to analyze requirements, create Jira artifacts, and generate technical design documentation.

## 🏗️ Architecture

The system features a modern microservices architecture with:

- **Next.js Frontend** (React/TypeScript) - Professional web interface with real-time status tracking
- **Python Flask API Backend** - Multi-agent orchestration and data processing
- **CrewAI Framework** - Sequential agent coordination and workflow management
- **Professional UI** - Glass morphism effects, gradient backgrounds, and smooth animations

## 🤖 AI Agents

1. **Business Analyst Agent** - Analyzes user input and generates comprehensive business requirements
2. **Project Manager Agent** - Creates Jira epics and user stories based on business requirements  
3. **System Architect Agent** - Produces technical design documentation and system diagrams

## 🚀 Quick Start

### Prerequisites

- **Node.js 18+** - For the frontend application
- **Python 3.11+** - For the backend API and AI agents
- **uv** (Recommended) - Modern Python package manager, or pip as alternative
- **OpenAI API Key** - Required for AI agent functionality
- **Jira Credentials** (Optional) - For creating actual Jira issues

### Installation

1. **Clone and Setup**
   ```bash
   git clone <repository-url>
   cd synovus-ai-sdlc
   ```

2. **Install Dependencies**
   
   **Python Dependencies (using uv - Recommended):**
   ```bash
   # This project uses uv for Python dependency management
   uv sync
   ```
   
   **Alternative Python Installation (using pip):**
   ```bash
   pip install crewai>=0.148.0 crewai-tools>=0.55.0 flask>=3.1.1 flask-cors>=6.0.1 jira>=3.8.0 pydantic>=2.11.7 python-dateutil>=2.9.0.post0 python-dotenv>=1.1.1 requests>=2.32.4
   ```

   **Node.js Dependencies:**
   ```bash
   npm install
   ```
   
   > 📋 **See [DEPENDENCIES.md](DEPENDENCIES.md) for detailed dependency information**

3. **Environment Configuration**
   
   Create a `.env` file in the root directory:
   ```env
   # Required: OpenAI API Key
   OPENAI_API_KEY=your_openai_api_key_here
   
   # Optional: Jira Integration (for creating actual issues)
   JIRA_SERVER=https://your-company.atlassian.net
   JIRA_USERNAME=your_email@company.com
   JIRA_API_TOKEN=your_jira_api_token
   ```

### Running the Application

1. **Start the Python API Backend** (Terminal 1)
   ```bash
   python api_backend.py
   ```
   The API will start on `http://localhost:8000`

2. **Start the Next.js Frontend** (Terminal 2)
   ```bash
   npm run dev
   ```
   The web interface will be available at `http://localhost:5000`

## 🎯 How to Use

### Basic Workflow

1. **Access the Interface**
   - Open your browser to `http://localhost:5000`
   - You'll see a professional interface with an input section and results area

2. **Enter Business Requirements**
   - In the text area, describe your project requirements
   - Example: "Build a customer management system for a retail company with user authentication, customer profiles, order tracking, and reporting dashboard"

3. **Run Analysis**
   - Click the "Analyze Business Requirements" button
   - Watch the real-time status indicators as each agent processes your input:
     - 🔵 Business Analyst (analyzing requirements)
     - 🟡 Project Manager (creating Jira artifacts)
     - 🟢 System Architect (designing technical solution)

4. **Review Results**
   - Navigate through the tabbed interface to see:
     - **Business Requirements** - Detailed analysis and stakeholder information
     - **Jira Artifacts** - Structured epics and user stories with acceptance criteria
     - **Technical Design** - System architecture and implementation details
     - **Diagrams** - Visual representations including system architecture, data flow, and sequence diagrams

5. **Download Artifacts**
   - Use the download buttons to save any generated documents
   - Files are saved in standard formats (Markdown, JSON)

### Sample Input

Try this example to see the system in action:

```
Project: E-commerce Mobile Application

Business Context: We need to develop a mobile application for our retail business to allow customers to browse products, make purchases, and track orders. The app should integrate with our existing inventory management system and payment processing.

Key Requirements:
- User registration and authentication
- Product catalog with search and filtering
- Shopping cart and checkout process  
- Order tracking and history
- Push notifications for order updates
- Integration with existing inventory system
- Support for multiple payment methods
- Admin dashboard for order management

Target Users: Retail customers, store administrators
Timeline: 6 months
Budget: $200,000
```

## 📦 Dependencies

This project uses modern dependency management:

- **Python**: Dependencies managed via `uv` and defined in `pyproject.toml`
- **Node.js**: Dependencies managed via `npm` and defined in `package.json`

For detailed dependency information, see [DEPENDENCIES.md](DEPENDENCIES.md).

## 📁 Project Structure

```
synovus-ai-sdlc/
├── app/                          # Next.js Frontend
│   ├── components/              # React components
│   │   ├── Header.tsx          # Navigation header
│   │   ├── InputSection.tsx    # Requirements input form
│   │   ├── StatusPanel.tsx     # Agent status tracking
│   │   ├── ResultsSection.tsx  # Results display with tabs
│   │   └── MermaidDiagram.tsx  # Diagram rendering
│   ├── api/                    # API route handlers
│   ├── globals.css             # Global styles
│   ├── layout.tsx              # Root layout
│   └── page.tsx                # Main page component
├── agents/                      # AI Agent Definitions
│   ├── business_analyst.py     # Business requirements analysis
│   ├── project_manager.py      # Jira artifacts creation
│   └── architect.py            # Technical design generation
├── tools/                       # Agent Tools
│   ├── jira_tool.py            # Jira integration
│   └── diagram_tool.py         # Mermaid diagram generation
├── models/                      # Data Models
│   └── data_models.py          # Pydantic data validation
├── utils/                       # Utilities
│   └── logger.py               # Logging configuration
├── templates/                   # Document Templates
├── outputs/                     # Generated Artifacts
├── api_backend.py              # Flask API server
├── main.py                     # Core multi-agent logic
├── config.py                   # Agent and task configuration
├── pyproject.toml              # Python dependencies (uv)
├── DEPENDENCIES.md             # Detailed dependency documentation
└── README.md                   # This documentation
```

## 🔧 Configuration

### Agent Customization

Modify `config.py` to customize agent behavior:

```python
# Example: Customize Business Analyst Agent
BUSINESS_ANALYST_CONFIG = {
    "role": "Senior Business Analyst",
    "goal": "Analyze business requirements and create comprehensive documentation",
    "backstory": "Expert in requirements gathering with 10+ years experience...",
    "temperature": 0.3  # Control creativity vs consistency
}
```

### Output Customization

Update templates in `templates/` directory to modify output format:
- `business_requirements.md` - Business analysis template
- `technical_design.md` - Technical documentation template

## 🔌 API Endpoints

The Flask backend provides these REST endpoints:

- `POST /analyze` - Submit business requirements for analysis
- `GET /results/latest` - Retrieve the most recent analysis results
- `GET /outputs/{filename}` - Download generated artifacts
- `GET /health` - Health check endpoint

## 🎨 Features

### Professional UI
- **Modern Design** - Glass morphism effects and gradient backgrounds
- **Real-time Status** - Live agent progress tracking with animations
- **Responsive Layout** - Works on desktop and mobile devices
- **Download System** - Save all generated artifacts locally

### AI-Powered Analysis
- **Intelligent Requirements Analysis** - Extracts key stakeholders, functional requirements, and business rules
- **Automated Jira Creation** - Generates properly structured epics and user stories
- **Technical Architecture** - Creates comprehensive system design documentation
- **Visual Diagrams** - Automatic generation of system architecture, data flow, and sequence diagrams

### Integration Ready
- **Jira Integration** - Direct creation of issues in your Jira instance
- **API-First Design** - Easy integration with existing systems
- **Flexible Output** - Multiple export formats (Markdown, JSON, diagrams)

## 🛠️ Troubleshooting

### Common Issues

1. **"OpenAI API Key not found"**
   - Ensure your `.env` file contains `OPENAI_API_KEY=your_key_here`
   - Restart the Python backend after adding the key

2. **"Port already in use"**
   - Frontend (5000): `lsof -ti:5000 | xargs kill -9`
   - Backend (8000): `lsof -ti:8000 | xargs kill -9`

3. **"Jira connection failed"**
   - Verify your Jira credentials in the `.env` file
   - Ensure your Jira API token has proper permissions
   - Note: Jira integration is optional for core functionality

4. **"Mermaid diagrams not rendering"**
   - Ensure JavaScript is enabled in your browser
   - Check browser console for errors
   - Try refreshing the page

### Debug Mode

Enable debug logging by setting:
```env
LOG_LEVEL=DEBUG
```

## 🔒 Security

- **API Keys** - Store in `.env` file, never commit to version control
- **CORS** - Configured for local development, update for production
- **Input Validation** - All user inputs are validated using Pydantic models

## 📈 Performance

- **Agent Processing** - Typically 30-60 seconds for complete analysis
- **Caching** - Results cached locally in `outputs/` directory
- **Scalability** - Microservices architecture supports horizontal scaling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is proprietary software developed for Synovus Bank.

## 🆘 Support

For technical support or questions:
- Check the troubleshooting section above
- Review the configuration options
- Ensure all prerequisites are installed correctly

---

**Built with ❤️ using CrewAI, Next.js, and Python**