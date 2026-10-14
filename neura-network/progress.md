# Neural Networks — Learning Progress (run 2)

BK learning NN from the ground up (Karpathy Zero-to-Hero inspired).
Format: strict mentor. Paper first, verbal answers required, files print own proof.
Run 1 deleted 2026-10-01 by BK choice; earned habits carry over:
labeled answers, loss≠slope, two-step format (sign→helps/hurts→increase/decrease),
rise/fall for losses, x is sacred, run-don't-remember.

## Curriculum
1. [passed 2026-10-01] Neuron as function: y = w·x + b; w multiplies (sensitivity),
   b sets start (output at x=0). neuron.py + neuron2.py, paper-run match 4/4.
2. [passed 2026-10-01] Loss: squared error. Sign dies so zero can be trusted
   (plain misses cancel: +2/−2 → avg 0 = lie; squared 4+4 → avg 4 = truth — corrected 2026-10-12: doc said avg 2 for five days, BK's fresh division (4+4)/2 caught it).
   loss.py: 3 rows, p/l 4-0-0 match paper.
3. [passed 2026-10-01] Derivative: slope = tilt at your feet; numerical
   [loss(w+h)-loss(w)]/h, h=nudge (NOT lr). Big h averages changing ground,
   small h = true instantaneous slope.
4. [passed 2026-10-01] One gradient step: w -= lr*slope. Exhibits: lr=0.1
   converges (4→0.16→…→1e-5), lr=1.0 diverges (4→196→9603→23M).
5. [passed 2026-10-06] Training loop: stop rule loss <= 0.0005 (BK's own),
   max-steps cap (BK's own, fired live on lr=1.0 divergence to 2.3e25).
   lr=0.1 → 4 steps; lr=0.01 → 68 steps (ratio 17×, keep-fractions
   0.2 vs 0.92; counts scale by log, not by the lr knob).
6. [passed 2026-10-12] Two parameters: w MULTIPLIES x → slope_w carries x
   (w-nudge moves predict by h·x); b only ADDS → slope_b never sees x
   (b-nudge moves predict by h); ratio slope_w/slope_b = x at any spot.
   One loop steps both w -= lr*slope_w AND b -= lr*slope_b; lesson6.py
   from (0,0), lr=0.1 → ONE hop onto the valley floor; paper-run match:
   (2.8, 1.4), predict 6.99991, loss 8.1e-9, i=1. Valley floor = LINE
   2w+b=7, not a point (secret ~90% landed at day's end).
7. [passed 2026-10-14] Batches/MSE: several (x, actual) rows at once;
   batch loss = average of squared misses; two truths pinch the bottom
   line → point (elimination finds the crossing); lesson7.py run-proven:
   244 hops, opener rows matched paper digit-for-digit, landing inside
   the stop rule's tolerance. NeuronInput dataclass — BK's own design.
   8. Value class; 9. Autograd; 10. MLP
11. (later) makemore arc  12. (later) attention, nanoGPT

## Resume point (next session — warm-up, then L8 Value class opens)
BK owes at resume (in order):
1. WARM-UP, self-fired, named items, ONE message (day 6's opener was
   clean — keep that standard):
   (a) The pinch sentence WHOLE, with coordinates: one truth → a line
   of bottoms; two truths → a point: (4, −1).
   (b) Batch loss defined: the average of squared misses over rows.
   (c) The tolerance story, own words: why the landing (3.95678,
   −0.93015) sits off (4, −1) — the stop rule fires at the FIRST spot
   with batch loss <= 0.0005 (final rows 0.00070943 / 0.00027491 →
   batch 0.00049217); it never demands zero.
   (d) Order of operations, own words: 7−2×0 = __, and why.
2. L8 OPENS — Value class (the micrograd arc begins): wrap ONE number
   in a class; + and × as its methods; the math stays BK's, the class
   just carries it. Paper first, files print own proof. Do not hand
   the design — NeuronInput showed he can build wrappers himself.
3. Deeper chew STILL OPEN (carried twice now): miss-after-hop =
   m + 2Δw + Δb (m=−7, Δw=2.79996, Δb=1.39999) → why ~0? Let BK
   derive; don't hand lr(x²+1)=1. Natural bridge into L9 autograd.
MENTOR DISCIPLINE (day 6: mentor error ×1 — the floor-line question
jumped a level: equations demanded before the concrete spot-checks
that give them meaning; owned at the time and replaced with the
spot-check table, which worked; log keeps score both sides). Rules
earned day 6: order of operations — MULTIPLY first, subtract second
(NEW family: 7−2×0 parsed (7−2)×0, fired "5" then "b=0"; killed by
own rows); signed change cuts NEW − OLD (the "+2" was OLD−NEW — the
day-2 division-direction rule, subtraction edition); a pasted row
must be internally consistent — square the miss yourself (caught a
mutated digit inside a run paste: 0.000283… vs the file's own
0.0002749…); never fire a number without checking it — recompute,
don't recall (mutation spiral (4,−1)→(3,−4)→(3,−1) died on a full
chain rebuild); prediction BEFORE run, gates closed in order
("Are we good?" asked before gates — held); verdict sentences carry
their numbers, never a bare "yes". Standing rules all carry: labels,
full-width, like-with-like, paste the run claim nothing, honest
flag → teach → rebuild (fired 3× day 6, all landed).
Watch list (day 6 + carry): SILENT SKIPS are the top cost now —
batch loss skipped 3×, prediction demanded 6×, verdict dripped in
fragments, coordinates dropped from the seal; keep the bill format,
call skips by name, demand the whole package. Mutation seen in TWO
places now — recalled numbers (fix: chain rebuild) and pasted runs
(fix: square the miss, cross-check pairs). Order-of-operations
family — watch it in paper rows too. Phrase-echo answered "where"
with the stop rule ("when" for "where"). Label swaps: miss values in
predict columns; "loss and bias" for position slots (w and b). Old
carries: the drip, sign drops, division direction, unlabeled bare
numbers, verdict-without-rows, question-word echo, "Fixed" = checked
against the file.

## Log
- 2026-10-14 (day 6, long): L7 PASSED — batches/MSE. Night-and-day
  opening: named warm-up fired WHOLE in the first message (meaning line
  all four slots; slope_w −27.9996 self-computed via own rows — nudged
  predict 0.0002, miss −6.9998, loss 48.99720004, matching day-4 paper
  exactly; glued-minus did NOT recur). L7 opener rows fired clean:
  (0,−3,9), (0,−7,49), labeled. Catches: (0,7) check "b=5" → ORDER-OF-
  OPERATIONS bug discovered — 7−2×0 parsed (7−2)×0 ("5" then "b=0",
  same wrong parse twice) → taught multiply-first → own rows killed it
  (2×0=0, 7−0=7, b=7, yes). Tilt m=−7 fired → died on own spots (BK
  falsified unprompted via (2,3)→(3,1); first fired (3,10) — ADDED
  −7 instead of adding it — then (3,−4) ✓; m=−2 landed). March "+2" =
  OLD−NEW flip → tied to the day-2 division-direction rule → 3−5=−2
  landed. Compass: both directions + "direction lives in the slope,
  never the loss" ✓. Batch loss: skipped 3× (called by name) →
  "average" named, 58/2=29 own division, verdict rows labeled ✓. THE
  PINCH: floor-line question answered with opener computations (wrong
  question, twice) → honest flags ×2 → MENTOR ERROR owned (question
  jumped a level) → concrete spot-check table ((0,7),(3,0),(2,1) vs
  both rows): verdicts six-for-six ✓ (miss values sat in predict
  columns — label swap); (0,7) — day-5 solo bottom — WRONG for row 1:
  the old floor is dead for the batch. Row 1's floor read off own
  spots: w+b=3 ✓; row 2's = the day-5 line. Elimination taught after
  honest flag → first try clean: w=4, b=3−4=−1, checks 3 vs 3, 7 vs 7
  ✓. MUTATION SPIRAL: (4,−1)→(3,−4)→(3,−1) across three messages
  (recall, not recompute) → killed by a full chain rebuild on paper —
  recompute beat recall. lesson7.py (his hands, mentor silent):
  NeuronInput dataclass — unprompted own design (the row as a thing);
  batch loss avg ✓; both slopes off batch loss ✓; correct h per knob
  ✓; both knobs same step ✓. Bugs caught by file-check: dead cap
  AGAIN (t never incremented — THIRD lifetime) → fixed; landing row
  never printed + per-row prints missing → fixed with his own
  _print_run helper at loop top. "Are we good?" asked before gates →
  prediction held before the run (stop-rule echo "loss <= 0.0005"
  fired for "where" — phrase-echo, called) → (4,−1) predicted ✓. RUN:
  244 hops; opener matched paper digit-for-digit (9/49/29; slopes
  −16.99975/−9.9999 verified via hop sizes 1.699975=0.1×17,
  0.99999=0.1×10); landing (3.95678, −0.93015) inside tolerance
  (final rows 0.00070943/0.00027491 → batch 0.00049217 <= 0.0005 —
  first spot inside). CATCH: mutated digit inside the PASTED RUN —
  Row1 landing loss pasted 0.00028303859491636747, file's own print
  0.0002749124552985258 (mentor re-ran; Python cannot print an
  inconsistent miss/loss pair — his own printed miss squares to the
  true value). New rule: square the miss yourself — a row must be
  internally consistent. Iteration-print regression caught (lesson6
  had it, lesson7 dropped) → fixed, 244 ✓ matches mentor's count.
  Verdict dripped: "yes" (verdict-without-rows, sharpened), 244 ✓,
  tolerance story landed in own words (sharpened: deviation lives in
  position slots w and b, not "the loss and bias"). Seal: "one truth
  → a line of bottoms, two truths a point" ✓ (word "point" taught
  after honest flag — he had "spot" already; coordinates (4,−1)
  verified many times, closing-sentence coordinates owed at warm-up).
  Bugs: order-of-operations NEW ×1, mutation ×3 (recalled numbers) +
  ×1 (pasted run — worst place, caught), sign ×3 ("+2" old−new, "2"
  dropped sign, (3,10) added a negative), phrase-echo ×1, verdict-
  without-rows ×1, label swaps ×2, silent skips all day (batch loss
  ×3, prediction ×6, verdict fragments, seal coordinates). Honest
  flags ×3 big (floors ×2 → table teach worked; elimination → first
  try; "don't know the exact word" → taught) + good clarifying
  questions (loop-flow recital correct first try; "row2 predict"
  clarified with a (5,5) demo). Strengths: named warm-up whole in
  message one (day-5 fix worked), falsify-with-own-spots now
  unprompted, NeuronInput own design, chain rebuild killed the
  spiral, elimination first try, tolerance story in own words. Deeper
  chew (m + 2Δw + Δb) carried again — never reached.
- 2026-10-13 (day 5, long): SECRET CLOSED (floor = LINE, meaning line
  landed whole), doc check re-verified, L7 opened. Warm-up misfired: owed
  named recital came back as a general L1-L6 recap, then dragged ~20
  rounds. BK's "using loss we know the direction" died on his own day-3
  rows (loss 1.44, slope −4.8, w 2.4→2.87996 UP); compass landed both
  directions; two-spot probe: +1.2/−1.2 both square to 1.44 → direction
  lives in sign, never loss; three labels landed after values echoed into
  job slots (loss=how wrong, sign=direction, size=steep); L6 law: slope_w
  h·x, slope_b plain h; ratio "2:1" was the instance → x=5 probe →
  "depends on the input" → ratio = x; stop rule loss<=0.0005 + cap 10000
  quoted (divergence catch, loss 2.3e25); anchor: 49, one hop, both
  knobs; match numbers: hops 1, i 1; landing slot first took LOSSES (49,
  8.1e-9) — position slot violation — then fired full-width from his own
  run (2.7999600000043756, 1.3999899999959098), run-don't-remember live;
  rows = 2 took EIGHT asks → flag → taught (row = one spot's full line;
  start row + landing row) → BK counted his own run ✓. Secret: between-
  checks 2×1+5=7, 2×1.5+4=7 fired clean; the word: "predictions",
  "List of predictions", "Valley" (question-word echo) → honest flag →
  taught via his own marks ordered by w (constant −2 march, no gaps) →
  LINE; march verified −2, −2. Meaning-line assembly = the battlefield:
  prediction slot grabbed −2/m THREE times (each killed by his own 7s);
  equation slot grabbed y=mx+c ×2 then p=wx+b — traced to MENTOR LEAK
  (my school-echo phrase, error #1 today, owned): taught
  checkable-at-spots, only-w-and-b, subject-names-owner, b-double-duty
  (his "are you asking a scalar value of b?" exposed the ambiguity);
  b=2w−7 fired (letters rule finally applied) → own check at (2,3):
  −3 ≠ 3, dead by own division; direction probe 7−4 vs 4−7 → b = 7−2w
  LANDED, check (2,3)→3 ✓; (0,7) check owed at resume. "I am getting
  confused" → 3-slot table taught (at (1,5): prediction 7, tilt m −2,
  loss slope 0 — floor = bottom of loss valley, slope 0 → step 0 → loop
  may stop anywhere on it) → BK rebuilt at (2,3): 7, −2, 0 ✓. Doc
  check: first answer "2" — the doc's own five-day lie echoed back;
  recompute re-fired: 4+4=8, 8/2=4 ✓ own rows; correction stands. L7
  opened: batches/MSE, two truth rows (x=1,a=3),(x=2,a=7), batch loss =
  average of squared misses; opener owed on paper at resume. Bugs: slot
  violations ×~8 (position←losses, word←number, prediction←tilt ×3,
  equation←general forms ×3 + scalar ×1, slope label←loss), echoes ×4
  ("2", "Valley", "predictions" ×2), sign-flip ×1 (caught own), bare
  unlabeled numbers ×2, silent skips all day (rows 8 asks). Honest flags
  ×5, all earned their teach (day-3 rows handed→rebuilt; rows; the
  word; confusion table; scalar-b question). Strengths: own division as
  the day's weapon (killed the doc lie, killed b=2w−7, settled 7−4),
  ran own file for proof, compass both directions, asking the exposing
  question. Deeper chew (m + 2Δw + Δb → why ~0) untouched — carried.
- 2026-10-12 (day 4, long): L6 PASSED. Warm-up 16 rounds: probe (4+4)/2=4
  caught the doc's own avg-2 lie (five days old — BK's division beat the
  doc; mentor corrected both places, correction notes in). NEW bug family:
  h leaked into the hop's START (new_w computed from w+h — BK found it
  himself after a pointer). Hop-2 falsification: BK's "above" claim died
  on his own division, said so plainly — FIRST full self-falsification,
  biggest win of the day. Anchor landed after ~9 asks, heavy scaffolding;
  label habit firing by day's end. L6 paper: slope_w −27.9996, slope_b
  −13.9999 at (0,0) (spot drifted from b=1 — accepted, L6 spot); story
  "w=0 kills x" predicted 1:1, rows said 2:1 — died twice (ratio test,
  then w=2.4 b-nudge probe: movement 0.0001 with x alive in predict);
  jobs landed from BK's own nudge rows: w multiplies (h·x = 0.0002),
  b adds (h = 0.0001). lesson6.py built through: two sequential loops →
  one loop; new_b(weight,…) argument swap (3 lifetimes); dead cap (i
  never incremented); prints removed then restored; global-leak 3rd
  lifetime (bare b in row print). Two "Fixed" claims checked against
  file — one 1/3 true; ONE MENTOR ERROR: graded 2nd "Fixed" off a stale
  read, BK caught it with a check (keep that pushback instinct). Paper
  package: 6 skips, then landed — step 1 (2.79996, 1.39999), predict
  6.99991, miss −0.00009, loss 8.1e-9; verdict 2-rows/1-hop/i=1 written
  BEFORE run; anchor self-fired pre-run (day-3 carry goal landed). Run
  matched paper to 5 decimals; tails = float noise (day-2 family).
  Secret: valley floor is a LINE — BK generated 4 bottoms solo ((3,1),
  (2.8,1.4), (0,7), (2,3)) via b = 7−2w; between-checks + the word owed
  at resume; deeper chew open (one-hop exact landing, m + 2Δw + Δb).
  Bugs: 8 digit incidents (3 truncations, 3 mutations, 2 mangles), 5
  like-with-like swaps (slope in loss slot, "2.7999 fell from 49"), 3
  phrase-echoes, 1 glued-minus recurrence (−1.43976001), 2 backward-fit
  attempts (1 caught live). Honesty flags ×7 (didn't know label / axes /
  the word; needed help on b's job) — all earned their keep. Strengths:
  solo falsification, solo generating move, full-width division kept
  honest (1.9999857142), pushback-with-check on mentor error.
- 2026-10-06 (day 3, ~1h): L5 PASSED. Step-2 redo exact (w 2.4→2.87996,
  loss 1.44→0.0576, machine match to 4 decimals; gap = h-law on machine's
  step 1). Old step 2 buried via fiction-slope analysis (trusted −2.4 vs
  true −4.8; sign right, hop size ruined — half-speed crawl, lesson:
  slope sets hop length, fiction slope = fiction hop). Part 2 stop rule
  passed first try: "if loss <= 0.0005, stop" — BK's own threshold,
  survived the trip. lesson5.py: BK wrote solo (mentor silent), global
  leak found in miss()/loss() (bare actual — self.actual fix), w=0 start
  fix, then THREE runs pasted: lr=0.1 4 steps, lr=0.01 68 steps, lr=1.0
  DIVERGED and BK's max_iters cap caught it live (9999, loss 2.3e25) —
  divergence exhibit from memory, cap fired in production. Part 3: BK
  predicted 10×, file said 17× (68 vs 4) — passed on direction+ballpark.
  Keep-fraction law built from BK's own rows: lr=0.1 keeps 0.2/step,
  lr=0.01 keeps 0.92/step; 0.92^10≈0.43 < one 0.2-cut; counts scale by
  logs not tens. Bugs today: −1.44 sign-story on parabola (anchor caught
  it after mentor push; like-with-like rule born), division flip
  (−6/−5.52), law-grab (h/2 for shrink question), handed-0.92 echoed
  before self-derive. Strengths: recompute rule self-fired on 1.44,
  honesty flags twice, cap design own idea. Mentor: 0 errors today
  (scratch re-verified each time — discipline working).
- 2026-10-05 (day 2, ~2h): Recap quiz passed (all 5) + L5 Parts 1(partial)/
  3(partial) done. Q1: BK's hidden square rule (a−d)²=a²−d surfaced,
  BK demanded citation, falsified it himself at d=1, three-term expansion
  now exact; glued-minus bug (−5.9998²=−35.99) killed; slope w=0 −23.9996
  machine match. Q2: sign rule both compass directions; wrong-sign trap
  computed (w→1.2, loss 4→12.96 rise); one-character moral "sign" BK's own
  word. Q3: first try. Q4: honesty flag ("didn't understand h/2") →
  re-taught with midpoint illustration → BK rebuilt law from own numbers
  (−12 lives at 1.5; +10 at 4.25). Q5: clean. L5: two hand steps, x-sacred
  recurred, Part 3 predicted 10×. FOUR mentor errors today (2.08, +16,
  −19.2, halved-form), all mentor-caught — new standing rule: BK
  recomputes every mentor number AND formula; mentor re-verifies own
  scratch first. Session paused 19:15, L5 open: step-2 redo + Part 2 line
  + lesson5.py tomorrow.
- 2026-10-01 Reset from run 1 (L1-L4-partial were passed there; files deleted).
- 2026-10-01 L1 passed: forward pass, paper-run match, w role said cleanly
  (multiplies x, sets sensitivity — visible as +3 steps in table). Fixed
  weight*bias+x bug via paid diagnosis (x and bias swapped roles).
- 2026-10-01 L4 passed: paper steps lr=0.1 (2→2.8, 0.16 fall) and lr=1.0
  (2→10, 196 rise) — both verified in lesson4.py Neuron class. Divergence
  exhibit earned: lr=1.0 explodes 196→23M, direction right every step.
  Bugs fixed under enforcement: bare h in slope (global leak), miss= label
  printing pred, "Fixed" claims without runs (now: paste the run, always).
  h-law derived from BK's own numbers: meter reads tilt displaced h/2 ahead
  (−12 at w=1 h=1, −7.6 at w=2 h=0.1, loop stalls at 3−h/2: 2.95, 2.99995).
  Recurring: sign drops in subtraction (3.24−4 → "+0.76"), misses-vs-losses
  vs-slopes label confusion (three recurrences), verdict sentences come back
  near-verbatim from mentor — probe with own-numbers versions.
- 2026-10-01 L2 passed: squared error. BK computed miss -2 (guessed 3 first),
  avg plain -0.67 vs squared 1.33, then the +2/−2 probe: plain avg 0 (lies
  "correct"), squared avg 4 (truth; mislogged as 2 for five days — caught
  2026-10-12 when BK re-divided (4+4)/2). Verdict near-verbatim from mentor —
  watch for that pattern.
- 2026-10-01 L3 passed: derivation (2w−6)², hand-slope w=1 h=1 → −12 vs run
  −15.9996 — h-probe owned: big h averages a flattening stretch, small h
  reports tilt at your feet. Slope table w/loss/slope prints own proof.
  Naming bug fixed: h ≠ learning_rate (two different concepts — nudge vs
  step-size knob). Recurring pattern: claims "wrote/fixed" without pasting
  run — now enforced: paste the run, claim nothing.
- 2026-10-05 Recap Q1 (w=0): square bug surfaced and killed — BK's hidden
  rule (a−d)²=a²−d gave 15.9998 vs true 15.9984; BK demanded citation
  instead of taking mentor's word (keep that instinct), then falsified the
  rule himself at d=1 (3²=9 ≠ 15). Three-term expansion then exact:
  loss(0.0001)=35.99760004. New bug: glued minus on square
  ((−5.9998)²=−35.99…) → slope −719,976; anchor fired but mentor-pointed.
  After fix: −23.9996, machine −23.99960000005308 — paper-run 2/2 today.
  Mentor leak: target printed before BK computed (echo risk; division
  re-shown once). Verbal Q1 landed on 5th ask but near-verbatim echo of
  own docstring; contrast (rise/fall vs compass) still owed.