# Synovus AI SDLC - Multi-Agent Business Analysis System

## Overview
Synovus AI SDLC is a multi-agent business analysis system built with CrewAI that automates the Software Development Lifecycle process. It converts business requirements into structured project artifacts using three specialized AI agents: a Business Analyst for requirements analysis, a Project Manager for creating Jira artifacts, and a System Architect for technical design documentation. The system aims to streamline the initial phases of software development by providing a coherent, end-to-end analysis pipeline.

## User Preferences
Preferred communication style: Simple, everyday language.

## System Architecture
The system employs a **sequential multi-agent workflow** orchestrated by CrewAI. Each agent builds upon the previous agent's output.

### Agent Workflow:
1.  **Business Analyst Agent**: Analyzes user input to generate comprehensive business requirements.
2.  **System Architect Agent**: Produces technical design documentation and system diagrams (e.g., C4, sequence, data flow using Mermaid) based on business requirements.
3.  **Project Manager Agent**: Creates Jira epics and user stories based on BOTH the business requirements AND technical design documentation from previous agents.

### Technical Implementation:
-   **Core Framework**: CrewAI for multi-agent orchestration, Python 3.x as the primary runtime.
-   **User Interface**: A modern Next.js (React/TypeScript) frontend provides a professional web interface with real-time status tracking, responsive design, and download functionality for generated artifacts. It features glass morphism effects, gradient backgrounds, and smooth animations.
-   **Backend**: A dedicated Python Flask API backend handles multi-agent orchestration and data processing, serving RESTful endpoints for the frontend.
-   **Data Models**: Pydantic is used for data validation and serialization, ensuring data integrity across `UserInput`, `BusinessRequirements`, and `JiraArtifact` models.
-   **Clean Output Management**: Generates structured outputs (business requirements, Jira artifacts, technical designs, diagrams) in text/JSON formats for easy integration with external tools.

### Key Features:
-   **Jira Integration**: Direct API integration for creating epics and user stories.
-   **Diagram Generation**: Utilizes a `DiagramTool` to generate Mermaid diagrams for various architectural views.
-   **Output Management**: Structured outputs (business requirements, Jira artifacts, technical designs, diagrams) are generated and made available for download in text and JSON formats.
-   **Error Handling**: Comprehensive error handling is implemented for Mermaid syntax, API communication, and document generation.

## External Dependencies
-   **OpenAI API**: Powers the underlying AI agents.
-   **Jira Cloud/Server**: Used for integrating with Jira to create project artifacts.
-   **crewai**: Multi-agent framework.
-   **jira**: Python client for Jira API.
-   **pydantic**: Data validation and modeling.
-   **python-dotenv**: Environment variable management.

-   **Next.js**: Frontend framework.
-   **Flask**: Backend API framework.