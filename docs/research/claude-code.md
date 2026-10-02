# Claude Code subagents — research notes (code.claude.com, 2026-10)
Sources: https://code.claude.com/docs/en/sub-agents , /hooks , /agent-teams , /agent-sdk/subagents
- Scope precedence: managed > --agents JSON > .claude/agents (project, walk up, --add-dir) > ~/.claude/agents > plugin agents/ (plugin ignores hooks/mcpServers/permissionMode). Recursive scan, identity = name field. Hot reload.
- /agents wizard removed v2.1.198 (edit files or ask Claude).
- Frontmatter: name, description (required); tools, disallowedTools, model (sonnet/opus/haiku/fable/full id/inherit), permissionMode, maxTurns, skills (preload), mcpServers, hooks, memory(user|project|local), background, omitClaudeMd, effort, isolation: worktree, color, initialPrompt.
- Model resolution: call param > frontmatter > CLAUDE_CODE_SUBAGENT_MODEL > main.
- Built-ins: Explore (read-only, skips CLAUDE.md, one-shot), Plan (read-only, plan mode), general-purpose (all tools), claude, statusline-setup, claude-code-guide, fork (inherits full conversation, /subtask).
- Agent tool (renamed from Task v2.1.63): subagent_type, model, name, isolation, run_in_background. Auto delegation by description ("use proactively"); @agent-<name> guarantees; claude --agent <name> runs session as agent.
- Background: Ctrl+B; completion notification. Resume via SendMessage to agent ID. Transcripts ~/.claude/projects/.../subagents/agent-{id}.jsonl
- Nesting allowed up to 3 levels (CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH), max 20 concurrent.
- Gets: own system prompt + env, delegation message, CLAUDE.md/AGENTS.md (except Explore/Plan/omitClaudeMd), git status, preloaded skills. Not: parent history. Returns: final report only (+agent ID).
- Hooks: SubagentStart (agent_id, agent_type; additionalContext), SubagentStop (decision:block keeps running; last_assistant_message, agent_transcript_path).
- Agent Teams experimental: CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1; lead + teammates share task list, message directly.
- SDK: agents option {name: AgentDefinition{description,prompt,tools,model,...}}, "Agent" in allowedTools.
