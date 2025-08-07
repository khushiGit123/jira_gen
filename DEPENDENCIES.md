# Python Dependencies

This project uses **uv** for dependency management. All dependencies are defined in `pyproject.toml`.

## Core Dependencies

### Multi-Agent Framework
- **crewai** (>=0.148.0) - Core multi-agent orchestration framework
- **crewai-tools** (>=0.55.0) - Additional tools for CrewAI agents

### Web Framework
- **flask** (>=3.1.1) - Lightweight web framework for API backend
- **flask-cors** (>=6.0.1) - Cross-Origin Resource Sharing support

### External Integrations
- **jira** (>=3.8.0) - Python client for Jira API integration
- **requests** (>=2.32.4) - HTTP library for API calls

### Data & Utilities
- **pydantic** (>=2.11.7) - Data validation and serialization
- **python-dateutil** (>=2.9.0.post0) - Date/time utilities
- **python-dotenv** (>=1.1.1) - Environment variable management

## Installation

### Using uv (Recommended)
```bash
uv sync
```

### Using pip (Alternative)
```bash
pip install crewai>=0.148.0 crewai-tools>=0.55.0 flask>=3.1.1 flask-cors>=6.0.1 jira>=3.8.0 pydantic>=2.11.7 python-dateutil>=2.9.0.post0 python-dotenv>=1.1.1 requests>=2.32.4
```

## Node.js Dependencies

Frontend dependencies are managed via npm and defined in `package.json`:

### Core Framework
- **next** - React framework for production
- **react** & **react-dom** - React library
- **typescript** - TypeScript support

### UI & Styling  
- **tailwindcss** - Utility-first CSS framework
- **@heroicons/react** - Icon library
- **lucide-react** - Additional icons

### HTTP Client
- **axios** - Promise-based HTTP client

### Development Tools
- **@types/node**, **@types/react**, **@types/react-dom** - TypeScript definitions
- **autoprefixer**, **postcss** - CSS processing