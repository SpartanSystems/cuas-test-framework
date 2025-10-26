#!/usr/bin/env python3
"""
Load SME Agent Profiles for Assessment
Connects ai-agent-profiles repository with cuas-test-framework
"""

import json
import os
from pathlib import Path

class AgentProfileLoader:
    def __init__(self):
        # Get the path to agent profiles repository
        self.base_path = Path(__file__).parent.parent.parent
        self.agent_profiles_path = self.base_path.parent / "ai-agent-profiles"
        self.config_path = self.base_path / "config/agents/agent_profiles_link.json"
        
    def load_config(self):
        """Load the agent configuration"""
        with open(self.config_path, 'r') as f:
            return json.load(f)
    
    def load_agent_profile(self, agent_name):
        """Load a specific agent profile"""
        agent_file = self.agent_profiles_path / f"agents/{agent_name}.md"
        if agent_file.exists():
            with open(agent_file, 'r') as f:
                return f.read()
        return None
    
    def get_phase_agents(self, phase):
        """Get agents assigned to a specific phase"""
        config = self.load_config()
        return config.get("phase_mapping", {}).get(phase, [])
    
    def load_personas_json(self):
        """Load the personas.json file"""
        personas_file = self.agent_profiles_path / "personas.json"
        if personas_file.exists():
            with open(personas_file, 'r') as f:
                return json.load(f)
        return None

if __name__ == "__main__":
    loader = AgentProfileLoader()
    
    # Test loading
    print("Loading agent profiles configuration...")
    config = loader.load_config()
    print(f"Found {len(config['active_agents'])} active agents")
    
    # Test loading personas
    personas = loader.load_personas_json()
    if personas:
        print(f"Loaded {len(personas)} personas from personas.json")
    
    # Show phase mapping
    print("\nPhase to Agent Mapping:")
    for phase, agents in config['phase_mapping'].items():
        print(f"  {phase}: {', '.join(agents)}")
