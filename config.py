"""
Configuration settings for the multi-agent system
"""

import os
from typing import Dict, Any

class Config:
    """Configuration class for system settings"""
    
    # API Keys and Credentials
    JIRA_SERVER = os.getenv("JIRA_SERVER", "")
    JIRA_USERNAME = os.getenv("JIRA_USERNAME", "")
    JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "")
    
    # Agent Configuration
    AGENT_CONFIG = {
        "business_analyst": {
            "role": "Senior Business Analyst",
            "goal": "Analyze business requirements and create comprehensive documentation",
            "backstory": "You are an experienced business analyst with expertise in requirements gathering, stakeholder management, and business process optimization.",
            "max_execution_time": 300,
            "verbose": True
        },
        "architect": {
            "role": "Senior System Architect",
            "goal": "Design comprehensive system architecture and create technical documentation with syntactically correct Mermaid diagrams including flowcharts, sequence diagrams, and ER diagrams",
            "backstory": "You are an expert system architect with 15+ years of experience in designing scalable, secure enterprise systems. You are highly skilled in creating syntactically correct Mermaid diagrams and clear technical documentation that guide development teams. You always validate Mermaid syntax before output.",
            "max_execution_time": 600,
            "verbose": True
        },
        "project_manager": {
            "role": "Senior Project Manager",
            "goal": "Create structured project artifacts including epics and user stories",
            "backstory": "You are a seasoned project manager with extensive experience in Agile methodologies, story writing, and project planning. Use the business requirements and technical design document to generate crisp user stories",
            "max_execution_time": 300,
            "verbose": True
        }
    }
    
    # Task Configuration
    TASK_CONFIG = {
        "business_analysis": {
            "description": "Analyze the user input and generate comprehensive business requirements",
            "expected_output": "Structured business requirements document with functional and non-functional requirements"
        },
        "architecture": {
            "description": "Generate technical design documentation including system architecture and data flow diagrams",
            "expected_output": "Technical design document with Mermaid diagrams and C4 architecture"
        },
        "project_management": {
            "description": "Create Jira epics and user stories based on business requirements and technical design document containing mermaid diagrams",
            "expected_output": "Created Jira epics and user stories with proper acceptance criteria"
        }
    }
    
    # Jira Configuration
    JIRA_CONFIG = {
        "default_project_key": "BA",
        "epic_issue_type": "Epic",
        "story_issue_type": "Story",
        "priority": "Medium",
        "timeout": 30
    }
    
    # Template Paths
    TEMPLATE_PATHS = {
        "business_requirements": "templates/business_requirements.md",
        "technical_design": "templates/technical_design.md"
    }
    
    # Logging Configuration
    LOGGING_CONFIG = {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "file": "system.log"
    }
    
    @classmethod
    def validate_config(cls) -> Dict[str, Any]:
        """Validate configuration and return status"""
        validation_result = {
            "valid": True,
            "missing_keys": [],
            "warnings": []
        }
        
        # Check required API keys
        required_keys = ["JIRA_SERVER", "JIRA_USERNAME", "JIRA_API_TOKEN"]
        for key in required_keys:
            if not getattr(cls, key):
                validation_result["missing_keys"].append(key)
                validation_result["valid"] = False
        
        # Check Jira server format
        if cls.JIRA_SERVER and not cls.JIRA_SERVER.startswith(("http://", "https://")):
            validation_result["warnings"].append("JIRA_SERVER should include protocol (http:// or https://)")
        
        return validation_result
