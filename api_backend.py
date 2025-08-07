#!/usr/bin/env python3
"""
API Backend for Synovus AI SDLC Multi-Agent System
Exposes the CrewAI agents functionality through REST endpoints
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json
import os
from main import BusinessAnalysisSystem
import re
import json
from utils.logger import setup_logger


logger = setup_logger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for Next.js frontend

# Initialize the business analysis system
try:
    business_system = BusinessAnalysisSystem()
    logger.info("Business analysis system initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize business analysis system: {e}")
    business_system = None

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Synovus AI SDLC API',
        'agents_available': business_system is not None
    })

@app.route('/analyze', methods=['POST'])
def analyze_requirements():
    """
    Main endpoint to analyze business requirements using multi-agent system
    """
    try:
        if not business_system:
            return jsonify({
                'error': 'Business analysis system not available'
            }), 500

        data = request.json or {}
        requirements = data.get('requirements', '')
        
        if not requirements:
            return jsonify({
                'error': 'Requirements field is required'
            }), 400

        logger.info(f"Starting analysis for requirements: {requirements[:100]}...")
        
        # Run the multi-agent workflow
        result = business_system.process_user_input(requirements)
        
        logger.info("Multi-agent workflow completed successfully")
        
        # Check if we got an error result
        if result.get('status') == 'error':
            return jsonify({
                'error': result.get('error_message', 'Unknown error occurred')
            }), 500
        
        # Process the results from the multi-agent system
        results = {
            'business_requirements': result.get('business_requirements', ''),
            'jira_artifacts': result.get('jira_issues_created', {}),
            'technical_design': result.get('technical_documentation', ''),
            'diagrams': []
        }
        
        # Extract diagrams from technical design
        tech_content = result.get('technical_documentation', '')
        if tech_content:
            results['diagrams'] = extract_mermaid_diagrams(tech_content)
        
        return jsonify({
            'status': 'success',
            'results': results
        })
        
    except Exception as e:
        logger.error(f"Error during analysis: {e}")
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/results/latest', methods=['GET'])
def get_latest_results():
    """Get the latest analysis results"""
    try:
        results = {
            'business_requirements': '',
            'jira_artifacts': {},
            'technical_design': '',
            'diagrams': []
        }
        
        # Load output files
        for filename in ['business_requirements.md', 'jira_artifacts.json', 'technical_design.md']:
            try:
                filepath = os.path.join('outputs', filename)
                if os.path.exists(filepath):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if filename.endswith('.json'):
                            try:
                                # Remove markdown code blocks if present
                                clean_content = content
                                if content.strip().startswith('```json'):
                                    # Extract JSON from markdown code block
                                    lines = content.strip().split('\n')
                                    if lines[0] == '```json' and lines[-1] == '```':
                                        clean_content = '\n'.join(lines[1:-1])
                                    elif '```json' in content:
                                        # Find JSON block within the content
                                        import re
                                        json_match = re.search(r'```json\s*\n(.*?)\n```', content, re.DOTALL)
                                        if json_match:
                                            clean_content = json_match.group(1)
                                
                                results[filename.replace('.json', '')] = json.loads(clean_content)
                            except json.JSONDecodeError as je:
                                logger.error(f"Error parsing JSON in {filename}: {je}")
                                logger.error(f"Content preview: {content[:200]}...")
                                # Store as text if JSON parsing fails
                                results[filename.replace('.json', '')] = content
                        else:
                            results[filename.replace('.md', '')] = content
            except Exception as e:
                logger.error(f"Error loading {filename}: {e}")
        
        # Extract diagrams from technical design
        tech_content = results.get('technical_design', '')
        if tech_content:
            results['diagrams'] = extract_mermaid_diagrams(tech_content)
        
        return jsonify({
            'status': 'success',
            'results': results
        })
        
    except Exception as e:
        logger.error(f"Error getting latest results: {e}")
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/status/<agent_name>', methods=['GET'])
def get_agent_status(agent_name):
    """Get status of a specific agent"""
    try:
        # This would be expanded to track agent execution status
        return jsonify({
            'agent': agent_name,
            'status': 'ready',
            'last_execution': None
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/outputs/<filename>', methods=['GET'])
def get_output_file(filename):
    """Retrieve generated output files"""
    try:
        filepath = os.path.join('outputs', filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            return jsonify({
                'filename': filename,
                'content': content
            })
        else:
            return jsonify({
                'error': 'File not found'
            }), 404
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/outputs', methods=['GET'])
def list_outputs():
    """List all available output files"""
    try:
        outputs_dir = 'outputs'
        if os.path.exists(outputs_dir):
            files = [f for f in os.listdir(outputs_dir) if f.endswith(('.md', '.json'))]
            return jsonify({
                'files': files
            })
        else:
            return jsonify({
                'files': []
            })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

def extract_mermaid_diagrams(text):
    """Extract Mermaid diagrams from text"""
    if not text:
        return []
    
    # Find all mermaid code blocks
    pattern = r'```mermaid\n(.*?)\n```'
    matches = re.findall(pattern, text, re.DOTALL)
    
    diagrams = []
    for i, match in enumerate(matches, 1):
        diagrams.append({
            'title': f'Diagram {i}',
            'code': match.strip()
        })
    
    return diagrams

if __name__ == '__main__':
    logger.info("Starting API Backend...")
    app.run(host='0.0.0.0', port=8000, debug=False)