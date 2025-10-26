#!/bin/bash

echo "=== Repository Connection Status ==="
echo ""

# Check both repositories exist
echo "1. Repository Status:"
for repo in ai-agent-profiles cuas-test-framework; do
    if [ -d "$HOME/$repo/.git" ]; then
        echo "  ✅ $repo: Connected"
        cd "$HOME/$repo"
        echo "     Branch: $(git branch --show-current)"
        echo "     Remote: $(git remote get-url origin)"
    else
        echo "  ❌ $repo: Not found"
    fi
done

echo ""
echo "2. Agent Profiles Available:"
if [ -d "$HOME/ai-agent-profiles/agents" ]; then
    echo "  Found $(ls $HOME/ai-agent-profiles/agents/*.md 2>/dev/null | wc -l) agent profiles"
    ls $HOME/ai-agent-profiles/agents/*.md 2>/dev/null | xargs -n1 basename | sed 's/^/    - /'
fi

echo ""
echo "3. SpartanCore Phases Found:"
find $HOME/ai-agent-profiles -name "*[Pp]hase*" -type f 2>/dev/null | xargs -n1 basename | sed 's/^/    - /'

echo ""
echo "4. Integration Status:"
if [ -f "$HOME/cuas-test-framework/config/agents/agent_profiles_link.json" ]; then
    echo "  ✅ Agent profile link configured"
else
    echo "  ⚠️  Agent profile link not configured"
fi

if [ -f "$HOME/cuas-test-framework/src/spartancore/phase_workflow.py" ]; then
    echo "  ✅ Phase workflow integration ready"
else
    echo "  ⚠️  Phase workflow not set up"
fi
