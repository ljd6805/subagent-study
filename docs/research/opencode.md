# OpenCode subagents — research notes (opencode.ai/docs + anomalyco/opencode dev, 2026-10-02)
Sources: https://opencode.ai/docs/agents/ , /docs/permissions/ , /docs/config/ , /docs/cli/
- mode: primary | subagent | all (default all). Tab cycles primary.
- Built-in primary: build (all tools), plan (edit/bash = ask); hidden: compaction, title, summary.
- Built-in subagent: general (multi-step, can edit, parallel units), explore (read-only fast), scout (experimental, OPENCODE_EXPERIMENTAL_SCOUT; external docs/deps).
- Declare: opencode.json "agent": {name: {...}} or markdown .opencode/agents/*.md, ~/.config/opencode/agents/*.md (singular agent/ still works). filename = name, body = prompt.
- Fields: description (required), mode, model (provider/model-id; subagent default = invoking primary's model), prompt ({file:...}), temperature, top_p, steps (maxSteps deprecated), color, hidden (only hides from @ autocomplete), disable, permission (allow/ask/deny; keys read, edit, glob, grep, list, bash, task, external_directory, webfetch, websearch, skill, ...), tools deprecated. Extra keys pass to provider.
- task tool params: description, prompt, subagent_type, task_id (resume), command.
- @general mention manual. permission.task glob rules (last match wins; deny removes from tool description; user @ still works).
- Child session "<desc> (@agent subagent)"; keybinds <Leader>+Down enter child, Left/Right cycle, Up parent.
- Context: fresh session with only prompt (unless task_id). Child inherits only parent's deny + external_directory rules. task/todowrite denied by default in subagents.
- Return: last message text wrapped <task id=... state="completed"><task_result>..</task_result></task>; parent must summarize to user.
- subagent_depth default 1 (no nesting); 2 = one more level; 0 = none.
- Parallel: multiple task calls in one message. background: true needs OPENCODE_EXPERIMENTAL_BACKGROUND_SUBAGENTS=true.
- CLI: opencode agent create (--path --description --mode --permissions -m), opencode agent list; opencode run --agent <name>.
