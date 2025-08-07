# Project Dependencies

This document lists all the dependencies required for the Synovus AI SDLC Multi-Agent Business Analysis System.

## Core Dependencies

### AI and Multi-Agent Framework
- **crewai** - Core multi-agent orchestration framework
- **crewai-tools** - Additional tools and utilities for CrewAI

### Web Framework
- **flask** - Web application framework for the user interface

### Configuration and Environment
- **python-dotenv** - Load environment variables from .env files

### Data Validation
- **pydantic** - Data validation and serialization

### External Integrations
- **jira** - Python library for Jira API integration

### Optional Components
- **streamlit** - Alternative web interface framework (if needed)

## Installation Commands

To install these dependencies, you can use the following commands:

```bash
pip install crewai
pip install crewai-tools
pip install flask
pip install python-dotenv
pip install pydantic
pip install jira
pip install streamlit
```

Or install all at once:
```bash
pip install crewai crewai-tools flask python-dotenv pydantic jira streamlit
```

## Standard Library Modules Used

The following Python standard library modules are used (no installation required):
- os
- sys
- json
- time
- datetime
- threading
- uuid
- typing

## Current Installation Status

✅ All dependencies are currently installed and working in this Replit environment.

## Environment Variables Required

The following environment variables are needed for full functionality:
- `OPENAI_API_KEY` - Required for AI agent functionality
- `JIRA_SERVER` - Jira server URL
- `JIRA_USERNAME` - Jira username
- `JIRA_API_TOKEN` - Jira API token
- `JIRA_PROJECT` - Jira project key (optional, defaults to 'DEFAULT')