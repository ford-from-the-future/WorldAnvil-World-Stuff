# Copilot Instructions: Org Relationship POC

## POC Goal
Build a bare-bones proof of concept that displays a modal menu box showing the relationship between exactly two organizations over time.

## Scope (Keep It Minimal)
- One modal-style container as the main UI.
- Static sample data is acceptable for this POC.
- No backend, authentication, or persistence required.
- Focus on layout clarity and relationship graph behavior.
- Use whatever tech stack is simplest and fastest to demonstrate the idea. Vanilla HTML/CSS/JS in a single file is ideal. Lightweight libraries (e.g. Chart.js) are fine if they reduce effort. No frameworks required.
- The modal should be visible on page load — no trigger button needed for this POC.

## Required UI Structure
1. Diplomatic status banner (top of modal)
- Show the official diplomatic status text across the top.
- Example values:
  - Interjurisdictional Mutual Observer Accord
  - Bilateral Recognition with Special Observer Protocols
  - Strategic Partnership under UCE Oversight

2. Organization names row (below status)
- Left side: Organization A name.
- Right side: Organization B name.
- Keep both names visually balanced.

3. Relationship history line graph (center)
- Y-axis conceptually represents relation score from -100 to 100. Label at least the 0 mark.
- X-axis represents time points (examples: 1994, 2001, 2025). Show the year label below each dot.
- Draw a horizontal baseline at absolute 0 using gray.
- Plot one dot per time point using the score value.
- Dot color rules:
  - Score > 0: green
  - Score = 0: gray
  - Score < 0: red
- Connect all dots in chronological order with a black line.

4. Summary text (bottom)
- Display the `summary` field from the data object as 2-3 sentences describing the relationship trend and current state.

## Functional Expectations
- Modal opens and displays all four sections in order.
- Graph supports mixed positive, zero, and negative values.
- Colors must reflect sign of each score exactly.
- Time points must be shown in chronological order.

## Data Shape (Suggested)
Use a simple object/array model similar to:

- diplomaticStatus: string
- organizations: { leftName: string, rightName: string }
- history: array of points with:
  - year: number
  - score: number (assumed valid, within -100..100)
- summary: string (2-3 sentences)

## Bare-Bones Sample Data (Suggested)
- diplomaticStatus: Strategic Partnership under UCE Oversight
- organizations: Helion Compact (left), Nareth Assembly (right)
- history:
  - 1994: -35
  - 2001: 0
  - 2012: 28
  - 2025: 61
- summary: Relations improved from early distrust to structured cooperation. A formal oversight framework stabilized contact and raised confidence. Current ties are positive, with continued upward momentum.

## Non-Goals
- No specific framework or build toolchain required — a single HTML file is sufficient.
- No advanced chart library required; Chart.js or plain SVG/Canvas are both acceptable.
- No animation requirements.
- No responsiveness beyond basic readability.

## Definition of Done
- Modal contains: status, org names, graph, summary.
- Graph clearly shows gray zero line, colored dots, and black connecting line.
- At least three historical points are displayed.
- The POC is easy to read and demonstrates the concept end-to-end.
