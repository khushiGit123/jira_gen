#!/usr/bin/env python3
"""
Multi-Agent Business Analysis System
Main entry point for the CrewAI-powered automation system
"""

import os
import sys
from dotenv import load_dotenv
from crewai import Crew, Process
from utils.logger import setup_logger
from agents.business_analyst import BusinessAnalystAgent
from agents.project_manager import ProjectManagerAgent
from agents.architect import ArchitectAgent

# Load environment variables
load_dotenv()

# Setup logging
logger = setup_logger(__name__)


class BusinessAnalysisSystem:
    """Main system orchestrator for the multi-agent business analysis workflow"""

    def __init__(self):
        """Initialize the system with all agents"""
        self.business_analyst = BusinessAnalystAgent()

        # Create Architect with both previous task contexts
        self.architect = ArchitectAgent(context_tasks=[self.business_analyst.task])

        # Create Project Manager with BOTH Business Analyst and Architect task contexts
        self.project_manager = ProjectManagerAgent(
            business_analyst_task=self.business_analyst.task,
            architect_task=self.architect.task
        )
        
        # Create the crew with sequential process
        self.crew = Crew(agents=[
            self.business_analyst.agent, 
            self.architect.agent,
            self.project_manager.agent
        ],
                         tasks=[self.business_analyst.task, self.architect.task, self.project_manager.task],
                         process=Process.sequential,
                         verbose=True)

    def validate_environment(self):
        """Validate that all required environment variables are set"""
        required_vars = ['JIRA_SERVER', 'JIRA_USERNAME', 'JIRA_API_TOKEN']

        missing_vars = []
        for var in required_vars:
            if not os.getenv(var):
                missing_vars.append(var)

        if missing_vars:
            logger.error(
                f"Missing required environment variables: {', '.join(missing_vars)}"
            )
            return False

        return True

    def process_user_input(self, user_input: str, project_key: str = None):
        """
        Process user input through the multi-agent system
        
        Args:
            user_input: Raw user requirements or business description
            project_key: Optional Jira project key for epic/story creation
            
        Returns:
            dict: Results from all agents
        """
        try:
            logger.info(f"Processing user input: {user_input[:100]}...")

            # Execute the crew workflow
            logger.info("Starting multi-agent workflow...")
            result = self.crew.kickoff(inputs={
                'user_input': user_input,
                'project_key': project_key or 'DEFAULT'
            })

            logger.info("Multi-agent workflow completed successfully")

            # Extract text output from CrewOutput object
            business_req = ""
            jira_artifacts_raw = ""
            technical_doc = ""

            if hasattr(result, 'tasks_output') and result.tasks_output:
                if len(result.tasks_output) > 0:
                    business_req = str(result.tasks_output[0].raw) if hasattr(
                        result.tasks_output[0], 'raw') else str(
                            result.tasks_output[0])
                if len(result.tasks_output) > 1:
                    technical_doc = str(result.tasks_output[1].raw) if hasattr(
                        result.tasks_output[1], 'raw') else str(
                            result.tasks_output[1])
                if len(result.tasks_output) > 2:
                    jira_artifacts_raw = str(result.tasks_output[2].raw) if hasattr(
                        result.tasks_output[2], 'raw') else str(
                            result.tasks_output[2])

            # If no tasks_output, try to get the raw result
            if not business_req and hasattr(result, 'raw'):
                technical_doc = str(result.raw)

            # The Project Manager agent now has access to Business Analyst output through context
            # Parse the JSON output from Project Manager directly
            from tools.jira_tool import JiraTool
            jira_tool = JiraTool()
            jira_result = jira_tool.process_project_manager_output(
                jira_artifacts_raw)

            # Extract summary information
            epics_count = len(jira_result.get('epics', []))
            stories_count = len(jira_result.get('stories', []))
            jira_summary = f"Created {epics_count} epics and {stories_count} stories in Jira"
            jira_issues_created = jira_result

            return {
                'status': 'completed',
                'business_requirements': business_req,
                'jira_artifacts': jira_summary,
                'jira_artifacts_raw': jira_artifacts_raw,
                'jira_issues_created': jira_issues_created,
                'technical_documentation': technical_doc,
                'mermaid_diagrams':
                self._extract_mermaid_diagrams(technical_doc)
            }

        except Exception as e:
            logger.error(f"Workflow execution error: {e}")
            return {'status': 'error', 'error_message': str(e)}

    def _extract_mermaid_diagrams(self, text: str) -> list:
        """Extract Mermaid diagrams from text"""
        import re

        # Pattern to match Mermaid code blocks
        pattern = r'```mermaid\n(.*?)\n```'
        matches = re.findall(pattern, text, re.DOTALL)

        # If no mermaid blocks found, look for common diagram types
        if not matches:
            # Look for graph, sequenceDiagram, etc.
            diagram_patterns = [
                r'(graph (?:TB|TD|BT|RL|LR).*?)(?=\n\n|\n#|\nsequence|\ngraph|\nerDiagram|\nstateDiagram|$)',
                r'(sequenceDiagram.*?)(?=\n\n|\n#|\nsequence|\ngraph|\nerDiagram|\nstateDiagram|$)',
                r'(erDiagram.*?)(?=\n\n|\n#|\nsequence|\ngraph|\nerDiagram|\nstateDiagram|$)',
                r'(stateDiagram-v2.*?)(?=\n\n|\n#|\nsequence|\ngraph|\nerDiagram|\nstateDiagram|$)'
            ]

            for pattern in diagram_patterns:
                found = re.findall(pattern, text, re.DOTALL | re.MULTILINE)
                matches.extend(found)

        # Clean up matches
        cleaned_matches = []
        for match in matches:
            # Remove extra whitespace and ensure proper formatting
            cleaned = match.strip()
            if cleaned and len(cleaned) > 10:  # Basic validation
                cleaned_matches.append(cleaned)

        logger.info(
            f"Extracted {len(cleaned_matches)} Mermaid diagrams from text")
        return cleaned_matches


def main():
    """Main CLI interface for the system"""
    print("🚀 Business Analysis Multi-Agent System")
    print("=" * 50)

    # Initialize system
    system = BusinessAnalysisSystem()

    # Validate environment
    if not system.validate_environment():
        print("❌ Environment validation failed. Please check your .env file.")
        sys.exit(1)

    print("✅ Environment validated successfully")

    # Get user input
    print("\n📝 Please provide your business requirements:")
    user_input = input("> ")

    if not user_input.strip():
        print("❌ No input provided. Exiting.")
        sys.exit(1)

    # Optional project key
    project_key = input(
        "\n🎯 Jira Project Key (optional, press Enter to skip): ").strip(
        ) or None

    # Process the input
    print("\n🔄 Processing through multi-agent system...")
    print("This may take a few minutes...\n")

    result = system.process_user_input(user_input, project_key)

    # Display results
    if result.status == 'error':
        print(f"❌ Error: {result.error_message}")
        sys.exit(1)

    print("✅ Processing completed successfully!")
    print("\n" + "=" * 60)
    print("📊 RESULTS")
    print("=" * 60)

    if result.business_requirements:
        print("\n📋 BUSINESS REQUIREMENTS:")
        print("-" * 30)
        print(result.business_requirements)

    if result.jira_artifacts:
        print("\n🎯 JIRA ARTIFACTS:")
        print("-" * 20)
        for artifact_type, artifacts in result.jira_artifacts.items():
            print(f"\n{artifact_type.upper()}:")
            if isinstance(artifacts, list):
                for artifact in artifacts:
                    print(f"  - {artifact}")
            else:
                print(f"  {artifacts}")

    if result.technical_documentation:
        print("\n🏗️ TECHNICAL DOCUMENTATION:")
        print("-" * 35)
        print(result.technical_documentation)

    if result.mermaid_diagrams:
        print("\n📈 MERMAID DIAGRAMS:")
        print("-" * 25)
        for i, diagram in enumerate(result.mermaid_diagrams, 1):
            print(f"\nDiagram {i}:")
            print(diagram)


if __name__ == "__main__":
    main()
