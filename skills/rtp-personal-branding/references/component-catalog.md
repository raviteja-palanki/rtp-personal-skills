# Brand component catalog

These are **legacy V8/v2.1 reference mechanics**, preserved for adaptation. Read the current skill’s source-precedence, motion, contrast, and accessibility rules first. Snippets may depend on surrounding variables, classes, assets, or event setup and are not complete applications. No live website rendering is claimed by this wording revision.

## Nav — Two Variants

Choose homepage/profile/hub navigation or the article frosted CTA. These are partial CSS snippets; supply the complete positioning and focus treatment from the current shell. The older Newsreader italic nav wordmark is a template-specific choice.

```css
nav {
    position: fixed; top: 0; padding: 1.5rem var(--px);
    backdrop-filter: blur(12px);
    background: linear-gradient(to bottom, rgba(3,4,7,0.95), rgba(3,4,7,0));
    transition: padding 0.4s var(--ease-cinematic), background 0.4s var(--ease-cinematic);
}
nav.scrolled { padding: 1rem var(--px); background: rgba(3,4,7,0.85); }

.nav-brand {
    /* V8 update: Newsreader italic, not Inter */
    font-family: var(--font-body); font-style: italic; font-weight: 500;
    font-size: 1.5rem; letter-spacing: -0.01em;
    color: var(--text-pure);
}

.nav-link { font-family: var(--font-sans); font-weight: 600; font-size: 0.85rem; color: var(--text-main); }
.nav-link::after { /* cyan underline, scaleX 0→1 with origin flip */
    background: var(--color-env);  /* V8: cyan, not white */
}

.nav-cta {
    /* White pill with dark text */
    font-family: var(--font-mono); font-weight: 800; font-size: 0.72rem;
    background: var(--text-pure); color: var(--bg-base);
    padding: 0.7rem 1.5rem; border-radius: 50px;
    text-transform: uppercase; letter-spacing: 0.08em;
}
```

```css
.nav-cta {  /* Frosted variant for articles */
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(12px);
    color: #FFFFFF !important;
}
.nav-cta:hover {
    background: #FFFFFF; color: #000000 !important;
    border-color: #FFFFFF;
}
```

## Hero Name — `palankiReveal` + Cyan Ghost

The PALANKI echo uses a duplicated visual wordmark. Keep one accessible name and the real text visible. The four-second pulse is a legacy effect; disable or replace it under the current motion policy.

```css
.palanki-text { position: relative; display: inline-block; }
.palanki-text::after {
    content: attr(data-text);  /* Clones text via data-text attribute */
    position: absolute; left: 0; top: 0;
    color: transparent; -webkit-text-stroke: 2px var(--color-env);
    opacity: 0; animation: pulseCyan 4s ease-in-out infinite 1.5s;
    z-index: -1; pointer-events: none;
}
@keyframes pulseCyan {
    0%, 100% { opacity: 0.2; filter: blur(2px); transform: scale(1); }
    50% { opacity: 0.8; filter: blur(8px); transform: scale(1.02); }
}
```

## Suspension Bridge SVG (The Signature Under "Bridger.")

The bridge remains the Bridger signature: 180×45px placement, 300×70 viewBox, deck, towers, cable and eleven suspenders. The sample intentionally omits coordinates and is not a complete SVG. Locate the full project asset or draw a complete replacement; never export literal ellipses.

```html
<svg class="bridge-schematic" viewBox="0 0 300 70">
    <!-- Deck -->
    <line x1="0" y1="55" x2="300" y2="55" stroke="rgba(6,182,212,0.4)" stroke-width="1.5"/>
    <line x1="0" y1="60" x2="300" y2="60" stroke="rgba(6,182,212,0.2)" stroke-width="1"/>
    <!-- Towers -->
    <path d="M 75 10 L 75 65 M 225 10 L 225 65" stroke="var(--color-env)" stroke-width="1.5" opacity="0.8"/>
    <polyline points="70 65 75 10 80 65" stroke="var(--color-env)" stroke-width="0.5" fill="none" opacity="0.4"/>
    <polyline points="220 65 225 10 230 65" stroke="var(--color-env)" stroke-width="0.5" fill="none" opacity="0.4"/>
    <!-- Main sweeping cables -->
    <path d="M 0 45 Q 75 10 150 50 Q 225 10 300 45" stroke="var(--color-env)" stroke-width="1.5" fill="none" opacity="0.7"/>
    <!-- 11 vertical suspenders at varying heights -->
    <line x1="20" y1="36" ... />  <!-- See homepage-final.html for full coords -->
</svg>
```

```css
.bridge-schematic path, .bridge-schematic line, .bridge-schematic polyline {
    stroke-dasharray: 600; stroke-dashoffset: 600;
}
.reveal-up.is-visible .bridge-schematic path,
.reveal-up.is-visible .bridge-schematic line,
.reveal-up.is-visible .bridge-schematic polyline {
    animation: drawBridge 2.5s var(--ease-cinematic) forwards 0.8s;
}
@keyframes drawBridge { to { stroke-dashoffset: 0; } }
```

## 3D Isometric Stack with Floating Planes + Data Stream

The four planes retain offsets 110/40/−30/−100px, twelve-pixel float, 0/0.5/1/1.5-second delays, four-pixel beam, and three staggered data packets. This is a schematic illustration, not a live data feed. Use a static state or current compliant motion for new editorial pages.

```css
@keyframes floatIso { 0%, 100% { transform: translateZ(var(--tz)); } 50% { transform: translateZ(calc(var(--tz) + 12px)); } }
.iso-layer {
    animation: floatIso 6s ease-in-out infinite;
    /* Each layer gets a staggered animation-delay: 0s, 0.5s, 1s, 1.5s */
}
.iso-strategy { --tz: 110px; animation-delay: 0s; }
.iso-product { --tz: 40px; animation-delay: 0.5s; }
.iso-engineering { --tz: -30px; animation-delay: 1s; }
.iso-delivery { --tz: -100px; animation-delay: 1.5s; }
```

```css
.core-beam {
    /* 4px vertical laser through the stack */
    width: 4px; height: 450px;
    background: linear-gradient(to bottom, transparent 0%, #FFF 20%, var(--color-env) 50%, #FFF 80%, transparent 100%);
    box-shadow: 0 0 20px var(--color-env), 0 0 40px rgba(6,182,212,0.8), 0 0 60px rgba(6,182,212,0.5);
    border-radius: 50px;
    animation: pulseBeam 3s ease-in-out infinite;
}
.data-packet {
    position: absolute; left: -1px; width: 6px; height: 35px; background: #FFF;
    box-shadow: 0 0 15px #FFF, 0 0 30px var(--color-env), 0 0 50px var(--color-env);
    animation: dataStream 2.5s linear infinite;
    border-radius: 10px;
}
.data-packet:nth-child(2) { animation-delay: 0.8s; height: 45px; }
.data-packet:nth-child(3) { animation-delay: 1.6s; height: 25px; }

@keyframes dataStream {
    0% { top: -10%; opacity: 0; transform: scaleY(0.8); }
    15% { opacity: 1; transform: scaleY(1.5); }
    85% { opacity: 1; transform: scaleY(1.5); }
    100% { top: 110%; opacity: 0; transform: scaleY(0.8); }
}
```

## Sticky Card Stack (Frosted Glass, V8)

Frosted folder cards use 32px blur, a light top edge, identity accents, and serif titles. Treat sticky 75vh height as a legacy layout; allow content growth and remove stickiness on short or narrow displays. Default current editorial cards use hairlines without resting shadows.

```css
.folder-card {
    position: sticky; height: 75vh;
    backdrop-filter: blur(32px); -webkit-backdrop-filter: blur(32px);
    border: 1px solid rgba(255,255,255,0.1);
    border-top: 1px solid rgba(255,255,255,0.25);  /* Brighter top edge = light catching */
    box-shadow: inset 0 1px 1px rgba(255,255,255,0.15), 0 30px 60px rgba(0,0,0,0.8);
    border-radius: 12px;
}
/* Identity-colored gradient top */
.card-1 { border-top: 2px solid var(--color-env); background: linear-gradient(145deg, rgba(6,182,212,0.08) 0%, rgba(10,11,16,0.6) 100%); }
.card-2 { border-top: 2px solid var(--color-model); background: linear-gradient(145deg, rgba(157,78,221,0.08) 0%, rgba(10,11,16,0.6) 100%); }
.card-3 { border-top: 2px solid var(--color-tools); background: linear-gradient(145deg, rgba(245,158,11,0.08) 0%, rgba(10,11,16,0.6) 100%); }

/* Titles: Instrument Serif on homepage, NOT Inter */
.folder-card h3 {
    font-family: var(--font-display);
    font-size: clamp(3rem, 5vw, 4.5rem);
    font-weight: 400;
    letter-spacing: -0.02em;
}
```

## Telemetry Stat Grid (V8 Dashboard Framing)

Telemetry keeps the four-column grid, mono metric/unit labels, strong value and hover emphasis. Collapse to two then one column where necessary. The 1.2-second scramble is a visual-only legacy demonstration with undeclared counter/target variables; expose the true number as accessible text and do not announce random values.

```css
.telemetry-grid {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 1px;  /* 1px gap creates thin divider lines */
    background: var(--border-dim);
    border: 1px solid var(--border-dim);
}
.telemetry-box {
    background: radial-gradient(circle at top right, rgba(255,255,255,0.02), transparent 80%), var(--bg-surface);
    padding: 4rem 2rem;
    transition: all 0.5s var(--ease-cinematic);
}
.telemetry-box:hover {
    background: radial-gradient(circle at top right, rgba(255,255,255,0.08), transparent 80%), var(--bg-surface);
    border-color: rgba(255,255,255,0.15);
    transform: translateY(-8px); z-index: 10;
    box-shadow: 0 20px 40px rgba(0,0,0,0.6);
}
.t-header {
    /* V8 signature: "Metric_01" + "[Years]" mono dashboard framing */
    font-family: var(--font-mono); font-size: 0.7rem;
    color: var(--text-faint); text-transform: uppercase; letter-spacing: 0.15em;
    display: flex; justify-content: space-between;
}
.t-value {
    font-family: var(--font-sans); font-size: clamp(3rem, 4vw, 4.5rem);
    font-weight: 900; letter-spacing: -0.04em;
}
```

```js
const duration = 1200;
const startTime = performance.now();
function updateCounter(currentTime) {
    const elapsed = currentTime - startTime;
    if (elapsed < duration) {
        counter.innerText = Math.floor(Math.random() * target * 2);  // Scramble
        requestAnimationFrame(updateCounter);
    } else {
        counter.innerText = target;  // Lock final value
    }
}
```

## The Why — Scroll-Written Quote + Hand-Drawn Highlight

Quote illumination and marker sweep are optional pacing ideas. All words must remain readable and available without scrolling or JavaScript. The purple-to-rose gradient and 2.5-second sweep conflict with the current series/motion rules; use a permitted single-color treatment. The progress sample depends on defined geometry.

```css
.q-word {
    opacity: 0.15;  /* Dim until activated */
    transition: opacity 0.4s ease, text-shadow 0.4s ease;
    display: inline-block;
}
.q-word.lit {
    opacity: 1;
    text-shadow: 0 0 15px rgba(255,255,255,0.4);
}
```

```js
// JS: based on container's rect.top, calculate progress 0-1, light that many words
const progress = Math.min(1, Math.max(0, (start - rect.top) / (start - end)));
const activeWords = Math.floor(progress * qWords.length);
qWords.forEach((word, i) => word.classList.toggle('lit', i <= activeWords));
```

```css
.hand-drawn-highlight::before {
    content: ''; position: absolute; bottom: 0.08em; left: -2%;
    width: 0; height: 45%;
    background: linear-gradient(90deg, var(--color-model), #F43F5E);
    opacity: 0.85; z-index: -1;
    transform: rotate(-1deg);  /* Handwritten feel — slight angle */
    border-radius: 6px;
    transition: width 2.5s var(--ease-cinematic) 0.3s;
}
.highlight-wrapper.is-visible .hand-drawn-highlight::before {
    width: 104%;  /* Slightly overshoot — authentic marker feel */
}
```

## Premium Glass Cards — Recession Stacking

The two-path recession stack retains the 40px top curve, inset edge, initial flat card and transform relationships. Clamp progress to 0–1, define the variables, and ensure the outgoing card cannot hide focused or essential content. Use a static stack when viewport height or motion preference requires it.

```css
.path-hero {
    position: sticky; top: 0; height: 100vh;
    background: var(--bg-base);
    border-top: 1px solid rgba(255,255,255,0.2);   /* Light edge */
    border-radius: 40px 40px 0 0;                  /* Physical card feel */
    box-shadow:
        0 -40px 100px rgba(0,0,0,1),               /* Massive drop shadow */
        inset 0 1px 2px rgba(255,255,255,0.3);     /* Light catching top */
}
.path-hero:first-child {
    /* First card integrates with page — no curve */
    border-radius: 0; border-top: none; box-shadow: none;
}
```

```js
progress = 1 - (Math.max(0, nextRect.top) / window.innerHeight)
scale = 1 - (progress * 0.08)
y = progress * 40
opacity = 1 - (progress * 0.8)
contentWrapper.style.transform = `translate3d(0, ${y}px, 0) scale(${scale})`
contentWrapper.style.opacity = opacity
```

## 3D Pop Browser Frame (V8)

The legacy browser mock enters from rotateX(15deg), translateY(100px), scale(0.9), with 1200px perspective and a 1.2-second transition. Keep its static state visible before enhancement. Browser chrome dots are decorative and must not imply functional window controls.

```css
.browser-container { perspective: 1200px; }
.browser-pop {
    opacity: 0;
    transform: rotateX(15deg) translateY(100px) scale(0.9);
    transition: all 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.1);  /* Spring */
    transform-origin: bottom center;
}
.browser-pop.is-visible {
    opacity: 1;
    transform: rotateX(0deg) translateY(0) scale(1);
}
```

```css
.browser-chrome {
    background: linear-gradient(to bottom, #2a2d36, #1a1c23);
    border-bottom: 1px solid #000;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
}
.browser-dot.r { background: #FF5F56; }
.browser-dot.y { background: #FFBD2E; }
.browser-dot.g { background: #27C93F; }
```

## Neon Highlight (Dark Mode Articles Inside Browser Frame)

Neon highlights are for dark mock/article surfaces. Recompute contrast through the actual gradient and preserve the text if effects are disabled.

```css
mark.neon-highlight {
    background: transparent;
    background-image: linear-gradient(110deg, transparent 2%, rgba(157,78,221,0.2) 5%, rgba(157,78,221,0.4) 95%, transparent 98%);
    color: #FFF;
    padding: 0.1em 0.3em; border-radius: 4px;
}
```

## Pastel Highlight (Light Mode Articles — Paper Canvas)

Pastel highlights supply a restrained paper treatment. Their scroll trigger is optional; the text and emphasis must survive a static render. Use the appropriate series tint.

```css
mark.pastel-highlight {
    background-image: linear-gradient(110deg, transparent 2%, var(--color-model-light) 5%, var(--color-model-light) 95%, transparent 98%);
    background-size: 0% 100%;  /* Animates to 100% on scroll */
    transition: background-size 1.2s var(--ease-cinematic);
    mix-blend-mode: multiply;  /* Ink-on-paper */
    padding: 0.1em 0.2em; border-radius: 4px;
}
mark.pastel-highlight.visible { background-size: 100% 100%; }
```

## Product Signature Footer (V8)

The footer preserves the authored signature and serif name. Replace website-specific copy when adapting to another medium; do not falsely imply Ravi authored externally supplied material.

```html
<footer>
    <div class="footer-links">...</div>
    <div class="footer-signature">
        <div>This website is my product work.</div>
        <div>Crafted with intent by <span class="sig-name">Ravi Teja Palanki</span></div>
    </div>
</footer>
```

```css
.footer-signature {
    font-family: var(--font-body); font-style: italic;
    color: var(--text-faint); font-size: 1.15rem;
}
.sig-name {
    font-family: var(--font-display);
    font-size: 2rem;
    color: var(--text-pure);
    font-style: normal;  /* The name is strong, not italic */
}
```

## Other Core Components

Additional components retained: topic pill, credential badge, article rocket progress, mistake card, terminal spec card, blueprint/VS diagram, practice pass/fail comparison, Up Next card, and magnetic back button. Use complete assets from a verified current project template. Progress must reflect real position; credentials and pass/fail labels need factual support.

## Component #31 — Live Trace Observability Engine

Live Trace (#31) is a simulated observability background for a technical hub, normally one per page. Keep the 600×800 viewBox, branches, pulse, nodes and labels. Parameters include series-compatible gradient stops, opacity 0.8 or lower, 0.2-second stagger, and a suggested three to five nodes. Hide or simplify on small devices and measure blur cost; no fixed LCP penalty is established. A static export is valid when the diagram is useful. Label it as illustrative if it could be mistaken for live status.

```html
<svg class="trace-engine" viewBox="0 0 600 800" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="traceGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%"   stop-color="#06B6D4" stop-opacity="0"/>
      <stop offset="20%"  stop-color="#06B6D4" stop-opacity="0.8"/>
      <stop offset="50%"  stop-color="#9D4EDD" stop-opacity="0.8"/>
      <stop offset="80%"  stop-color="#F59E0B" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#F59E0B" stop-opacity="0"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <g stroke="url(#traceGrad)" stroke-width="2" fill="none" filter="url(#glow)">
    <path d="M 300 50 L 300 750" class="trace-path"/>
    <path d="M 300 200 C 400 200 450 250 450 300" class="trace-path" style="animation-delay: 0.7s;"/>
    <path d="M 300 400 C 200 400 150 450 150 500" class="trace-path" style="animation-delay: 0.9s;"/>
    <path d="M 300 600 C 400 600 400 650 400 700" class="trace-path" style="animation-delay: 1.1s;"/>
  </g>
  <path d="M 300 50 L 300 750" stroke="#FFF" stroke-width="3" fill="none" class="trace-pulse"/>
  <g fill="rgba(10,11,16,0.8)" stroke="rgba(255,255,255,0.2)" stroke-width="1">
    <rect x="240" y="80"  width="120" height="30" rx="4" class="trace-node"/>
    <rect x="390" y="285" width="120" height="30" rx="4" class="trace-node"/>
    <rect x="90"  y="485" width="120" height="30" rx="4" class="trace-node"/>
    <rect x="340" y="685" width="120" height="30" rx="4" stroke="#06B6D4" class="trace-node"/>
  </g>
  <g fill="#6B7280" class="trace-text">
    <text x="250" y="100">span: INPUT</text>
    <text x="400" y="305">span: RETRIEVE</text>
    <text x="100" y="505">span: GENERATE</text>
    <text x="350" y="705" fill="#06B6D4">EVAL: PASS</text>
  </g>
</svg>
```

```css
.trace-engine {
    position: absolute; top: 5%; right: -5vw;
    width: 60vw; height: 90vh; max-width: 800px;
    pointer-events: none; z-index: 0; opacity: 0.8;
    filter: drop-shadow(0 0 20px rgba(157,78,221,0.2));
}
.trace-path  { stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: drawTrace 3s var(--ease-cinematic) forwards 0.5s; }
.trace-pulse { stroke-dasharray: 20 100; animation: flowData 2s linear infinite; }
.trace-node  { transform-origin: center; transform-box: fill-box; animation: nodePulse 3s ease-in-out infinite; }
.trace-node:nth-child(even) { animation-delay: 1.5s; }
.trace-text  { font-family: var(--font-mono); font-size: 10px; font-weight: 700; letter-spacing: 0.1em; opacity: 0; animation: fadeIn 1s forwards 2s; }

@keyframes drawTrace { to { stroke-dashoffset: 0; } }
@keyframes flowData  { from { stroke-dashoffset: 120; } to { stroke-dashoffset: 0; } }
@keyframes nodePulse { 0%, 100% { transform: scale(1); opacity: 0.6; } 50% { transform: scale(1.1); opacity: 1; filter: drop-shadow(0 0 10px currentColor); } }
@keyframes fadeIn    { to { opacity: 0.7; } }

/* Mobile — hide or heavily fade */
@media (max-width: 1024px) { .trace-engine { opacity: 0.3; right: -20vw; } }
@media (max-width:  768px) { .trace-engine { display: none; } }
```

## Component #32 — Per-Level Semantic Animated SVG Badges

Semantic badges (#32) retain L1 reticle, L2 network, L3 layers and L4 waveform. Keep a visible level/title; an unfamiliar metaphor is not a reason to remove information. These four describe this curriculum, not a universal four-level cognitive limit or the AI autonomy ladder. Do not collapse a real fifth level to fit the artwork. The source snippets show an 80px container; implement and verify a 60px mobile variant if desired. Keep series-color precedence explicit rather than reassigning colors silently.

```html
<div class="level-badge">
    L1  <!-- visible label behind the SVG -->
    <svg class="badge-svg" viewBox="0 0 100 100">
      <!-- level-specific content — see below -->
    </svg>
</div>
```

```css
.level-badge {
    flex-shrink: 0; width: 80px; height: 80px; border-radius: 20px;
    background: var(--level-bg);            /* per-level tint at 5% opacity */
    border: 1px solid rgba(255,255,255,0.1);
    display: flex; align-items: center; justify-content: center;
    font-family: var(--font-mono); font-size: 1.5rem; font-weight: 800;
    color: var(--level-color);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5), inset 0 1px 1px rgba(255,255,255,0.2);
    position: relative; overflow: hidden;
}
.badge-svg { position: absolute; inset: 0; width: 100%; height: 100%; opacity: 0.6; z-index: -1; }

/* Per-level color + background mapping */
#level-1 { --level-color: #06B6D4; --level-bg: rgba(6, 182, 212, 0.05); }
#level-2 { --level-color: #9D4EDD; --level-bg: rgba(157, 78, 221, 0.05); }
#level-3 { --level-color: #F59E0B; --level-bg: rgba(245, 158, 11, 0.05); }
#level-4 { --level-color: #F43F5E; --level-bg: rgba(244, 63, 94, 0.05); }
```

```html
<svg class="badge-svg" viewBox="0 0 100 100">
  <pattern id="gridL1" width="10" height="10" patternUnits="userSpaceOnUse">
    <path d="M 10 0 L 0 0 0 10" fill="none" stroke="currentColor" stroke-width="0.5" opacity="0.2"/>
  </pattern>
  <rect width="100" height="100" fill="url(#gridL1)"/>
  <g class="l1-reticle" style="transform-origin: 50% 50%;">
    <circle cx="50" cy="50" r="20" fill="none" stroke="currentColor" stroke-width="1.5"/>
    <circle cx="50" cy="50" r="10" fill="none" stroke="currentColor" stroke-width="0.5"/>
    <line x1="20" y1="50" x2="40" y2="50" stroke="currentColor" stroke-width="1.5"/>
    <line x1="60" y1="50" x2="80" y2="50" stroke="currentColor" stroke-width="1.5"/>
    <line x1="50" y1="20" x2="50" y2="40" stroke="currentColor" stroke-width="1.5"/>
    <line x1="50" y1="60" x2="50" y2="80" stroke="currentColor" stroke-width="1.5"/>
    <circle cx="50" cy="50" r="2" fill="currentColor"/>
  </g>
</svg>
```

```css
.l1-reticle { transform-origin: center; animation: l1Scan 4s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite; }
@keyframes l1Scan { 0%, 100% { transform: scale(1) rotate(0deg); } 50% { transform: scale(0.6) rotate(90deg); stroke: #FFF; } }
```

```html
<svg class="badge-svg" viewBox="0 0 100 100">
  <path d="M 20 50 L 40 30 L 70 40 L 85 70" stroke="currentColor" stroke-width="1.5" fill="none" opacity="0.3"/>
  <path d="M 20 50 L 40 70 L 70 60 L 85 30" stroke="currentColor" stroke-width="2" fill="none" class="l2-path"/>
  <circle cx="20" cy="50" r="4" fill="currentColor" opacity="0.5"/>
  <circle cx="40" cy="30" r="4" fill="currentColor" opacity="0.5"/>
  <circle cx="70" cy="40" r="4" fill="currentColor" opacity="0.5"/>
  <circle cx="85" cy="70" r="4" fill="currentColor" opacity="0.5"/>
  <circle cx="40" cy="70" r="5" fill="currentColor" class="l2-node" style="animation-delay: 0s;"/>
  <circle cx="70" cy="60" r="5" fill="currentColor" class="l2-node" style="animation-delay: 0.5s;"/>
  <circle cx="85" cy="30" r="5" fill="currentColor" class="l2-node" style="animation-delay: 1s;"/>
</svg>
```

```css
.l2-path { stroke-dasharray: 50; stroke-dashoffset: 50; animation: l2Flow 2s ease-in-out infinite; }
.l2-node { animation: l2Pulse 2s ease-in-out infinite; }
@keyframes l2Flow  { to { stroke-dashoffset: -50; } }
@keyframes l2Pulse { 50% { fill: #FFF; filter: drop-shadow(0 0 5px #FFF); } }
```

```html
<svg class="badge-svg" viewBox="0 0 100 100" style="transform: translateY(5px);">
  <g class="l3-layer-bot"><path d="M 50 60 L 80 75 L 50 90 L 20 75 Z" fill="none" stroke="currentColor" stroke-width="2" opacity="0.3"/></g>
  <g class="l3-layer-mid"><path d="M 50 40 L 80 55 L 50 70 L 20 55 Z" fill="none" stroke="currentColor" stroke-width="2" opacity="0.6"/></g>
  <g class="l3-layer-top"><path d="M 50 20 L 80 35 L 50 50 L 20 35 Z" fill="currentColor" opacity="0.5"/></g>
</svg>
```

```css
.l3-layer-top { animation: l3Float 3s ease-in-out infinite alternate; }
.l3-layer-mid { animation: l3Float 3s ease-in-out infinite alternate 0.5s; }
.l3-layer-bot { animation: l3Float 3s ease-in-out infinite alternate 1s; }
@keyframes l3Float { 0% { transform: translateY(0); } 100% { transform: translateY(-4px); } }
```

```html
<svg class="badge-svg" viewBox="0 0 100 100">
  <line x1="10" y1="50" x2="90" y2="50" stroke="currentColor" stroke-width="1" opacity="0.3"/>
  <path d="M 10 50 Q 20 50 30 50 T 45 50 T 50 20 T 55 50 T 70 50 T 90 50" fill="none" stroke="currentColor" stroke-width="2" class="l4-wave"/>
  <circle cx="50" cy="20" r="4" class="l4-spike"/>
</svg>
```

```css
.l4-wave  { stroke-dasharray: 200; stroke-dashoffset: 200; animation: l4Sweep 3s linear infinite; }
.l4-spike { opacity: 0; animation: l4Alert 3s linear infinite; }
@keyframes l4Sweep { to { stroke-dashoffset: 0; } }
@keyframes l4Alert { 45%, 55% { opacity: 1; fill: #FFF; } }
```

## Component #33 — Card Laser on Hover

Card laser (#33) is an optional top-edge hover/focus cue. Suggested dimensions are 50% width and 2px height, normally 0.5–0.8 seconds; these are design preferences, not perception measurements. A card remains clearly interactive without it. Avoid looping or stacking many competing effects. Pairing with a subtle ring/glow can work after review; it is not categorically prohibited.

```html
<a href="..." class="topic-card">
    <div class="card-laser"></div>
    <!-- card contents -->
</a>
```

```css
.topic-card { position: relative; overflow: hidden; }

.card-laser {
    position: absolute;
    top: 0; left: -100%;
    width: 50%; height: 2px;
    background: linear-gradient(90deg, transparent, var(--level-color), #FFF);
    opacity: 0; z-index: 5;
}

.topic-card:hover .card-laser {
    animation: shootLaser 0.8s ease-out forwards;
    opacity: 1;
}

@keyframes shootLaser {
    0%   { left: -50%; }
    100% { left: 150%; }
}
```

## Component #34 — Status Ring Indicator

Status ring (#34) distinguishes coming, published and updated. The original 14px ring, 6px center, dashed coming state and amber update variant remain. Add visible status text where useful and an accessible name or accompanying text. The faint decorative ring must not be the only status cue. Hover must not make a draft appear published. More states require an understandable representation, not removal of real states.

```html
<div class="topic-num-wrapper">
    <div class="status-ring"></div>
    <span class="topic-num">TOPIC_01</span>
</div>
```

```css
.status-ring {
    width: 14px; height: 14px; border-radius: 50%;
    border: 2px solid rgba(255,255,255,0.1);
    position: relative;
    display: flex; align-items: center; justify-content: center;
}
.status-ring::after {
    content: '';
    width: 6px; height: 6px; border-radius: 50%;
    background: transparent;
    transition: all 0.3s ease;
}

/* Hover state — fills the ring center with level color */
.topic-card:hover .status-ring {
    border-color: var(--level-color);
    box-shadow: 0 0 10px var(--level-color);
}
.topic-card:hover .status-ring::after {
    background: var(--level-color);
}
```

```css
.status-ring.published::after { background: var(--level-color); }      /* Default filled */
.status-ring.updated          { border-color: #F59E0B; }                /* Amber border — "new" */
.status-ring.updated::after   { background: #F59E0B; animation: pulseDot 2s ease-in-out infinite; }
.status-ring.coming           { border-style: dashed; }                 /* Draft/upcoming */

@keyframes pulseDot { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
```

## Component #35 — Spotlight 3D Tilt Card

Spotlight tilt (#35) is an optional fine-pointer treatment for a small group of navigation cards. Retain ±4deg tilt, 1.02 scale, 800px spotlight at 0.06 opacity, and 20px content lift as starting values. Use an anchor/button for navigation. Gate mouse tracking by hover/fine-pointer capability and reduced-motion preference; width alone does not detect touch. Coalesce updates with requestAnimationFrame when needed and measure performance, regardless of card count. Parent perspective shares a scene; the perspective() transform on an element is also valid. Choose deliberately rather than declaring one invalid.

```html
<div class="guide-grid">
    <div class="guide-card">
        <span class="guide-label">Path 01</span>
        <p class="guide-desc"><strong>New to evals?</strong><br>Start at Level 1, Topic 1.</p>
    </div>
    <!-- more cards -->
</div>
```

```css
.guide-grid {
    display: grid; grid-template-columns: repeat(2, 1fr);
    gap: 2rem; max-width: 1000px; margin: 0 auto;
    perspective: 1000px;                           /* REQUIRED — enables 3D on children */
}

.guide-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid var(--border-dim); border-radius: 16px;
    padding: 3rem;
    display: flex; flex-direction: column; gap: 1rem;
    backdrop-filter: blur(12px);
    position: relative; overflow: hidden;
    transform-style: preserve-3d;                   /* REQUIRED */
    transition: transform 0.1s ease, box-shadow 0.3s ease;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    will-change: transform;
}
.guide-card:hover { box-shadow: 0 20px 50px rgba(0,0,0,0.8); border-color: rgba(255,255,255,0.15); }

/* Spotlight — radial gradient following mouse via CSS custom props */
.guide-card::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(800px circle at var(--mouse-x) var(--mouse-y), rgba(255,255,255,0.06), transparent 40%);
    opacity: 0; transition: opacity 0.3s;
    z-index: 0; pointer-events: none;
}
.guide-card:hover::before { opacity: 1; }

/* Lift card contents into 3D — gives depth */
.guide-card > * { position: relative; z-index: 1; transform: translateZ(20px); }
```

```js
document.querySelectorAll('.guide-card').forEach(card => {
    card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        // Spotlight follow
        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);

        // 3D tilt (disable on mobile)
        if (window.innerWidth > 768) {
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = ((y - centerY) / centerY) * -4;  // -4 to +4 deg
            const rotateY = ((x - centerX) / centerX) *  4;
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
        }
    });
    card.addEventListener('mouseleave', () => {
        if (window.innerWidth > 768) {
            card.style.transform = `perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)`;
        }
    });
});

```

```css
/* Mobile — disable transform entirely */
@media (max-width: 768px) { .guide-card { transform: none !important; } }
```

## Complete the examples before use

Provide missing tokens (including --px, identity colors and the font families), actual URLs, complete SVG paths and unique IDs, runtime variables, observer setup and cleanup. Keep base text visible; animate only after successful initialization. Prefer focus-visible alongside hover and preserve a static state for print/export. Reset transforms and cancel animation frames when preferences change.

A status dot is not a button and does not itself need a 44px box; its clickable parent does. Static exports can preserve useful semantics even when an effect cannot travel to Word, Gamma or PowerPoint.

## Legacy motion inventory

Retained animation concepts: floatIso, dataStream, pulseBeam, drawBridge; blurReveal, palankiReveal, pulseCyan, drawLine, scaleYIn, enginePulse, noiseShift, slowZoom; trace draw/flow/node pulse, reticle scan, network flow/pulse, layered float, waveform sweep/alert, laser sweep, and update dot. Scroll concepts include reveal-up/reveal-lines, 1.2-second scramble, quote illumination, recession, 3D pop, nav tightening past 50px, and magnetic offsets 0.15/0.08. The old Lenis 1.0.42 package reference is historical, not a current dependency requirement.

## Page recipes and historical locations

Homepage: nav → Bridger hero/bridge → architecture → telemetry → Why quote → Two Paths → article teaser → signature. Profile: sequential product cards. Writing landing: hero → architecture → anti-patterns → deep dives → quote → reading transition → archive. Series hub: hero → levels → reading guide → CTA; the older Harness layout has eight episodes. Article: progress → paper/learning objectives → body/exhibits → next article → back navigation → signature. Adapt these to the current project specification.

The former paths below were named by v2.2 but were **not found at those locations during this pass**. Preserve them as migration clues, not verified current files:

- `1_Projects/my-personal-website/FOR-LOVABLE/02-reference-html/homepage-final.html`
- `1_Projects/my-personal-website/reference/BLOG-POST-TEMPLATE.html`
- `1_Projects/my-personal-website/03-articles-ai-evals/index.html`
- `1_Projects/my-personal-website/reference/production-landing.html`
- `1_Projects/my-personal-website/scripts/apply-gold-template.py`
- `1_Projects/my-personal-website/lovable/`
- `1_Projects/my-personal-website/FOR-LOVABLE/01-lovable-specs/04-PROFILE-PAGE-SPEC.md`
- `1_Projects/my-personal-website/FOR-LOVABLE/01-lovable-specs/09-CONTENT-MAP.md`

Older responsive recipes: short desktop below 850px height compacts hero (6rem padding, 5.5rem title, 3.2rem serif, 0.85 illustration scale); 1024px tablet uses one-column hero, two-column telemetry, non-sticky paths; 768px mobile uses one-column telemetry, wrapping highlight and stacked signature. These are starting recipes; current magazine layout uses 640/900/1200/1440px breakpoints. Test content rather than applying both sets mechanically.

## Additional legacy surface and motion snippets

Retained noise/glow, paper canvas, and keyframe/easing mechanics. These require the same current-spec, visibility, motion, and contrast review as the catalog above. The abbreviated SVG data URL is a placeholder, not a usable asset.

```css
.noise-overlay {
    position: fixed; inset: 0;
    background: url("data:image/svg+xml,...fractalNoise baseFrequency=0.8 numOctaves=3...");
    opacity: 0.04;
    mix-blend-mode: screen;   /* V8 change — was multiply. Screen is lighter. */
    pointer-events: none;
}
```

```css
.glow-bg {
    position: fixed; inset: 0; pointer-events: none;
    background:
        radial-gradient(circle at 80% 0%, rgba(157, 78, 221, 0.08) 0%, transparent 50%),
        radial-gradient(circle at 20% 100%, rgba(6, 182, 212, 0.06) 0%, transparent 50%);
}
```

```css
.paper-canvas {
    background: var(--bg-paper);
    margin-top: -12vh;                       /* Overlaps dark hero */
    border-radius: 40px 40px 0 0;
    padding: 6rem var(--px) 8rem;
    box-shadow:
        0 -40px 100px rgba(0,0,0,0.8),
        inset 0 1px 1px rgba(255,255,255,1),
        inset 0 2px 4px rgba(255,255,255,0.5);
    /* Dot grid — notebook texture */
    background-image: radial-gradient(rgba(0,0,0,0.03) 1px, transparent 1px);
    background-size: 32px 32px;
}
```

```css
--ease-cinematic: cubic-bezier(0.16, 1, 0.3, 1);        /* Apple deceleration */
--ease-spring:    cubic-bezier(0.175, 0.885, 0.32, 1.1); /* Spring overshoot */
```

```css
@keyframes floatIso { 0%, 100% { transform: translateZ(var(--tz)); } 50% { transform: translateZ(calc(var(--tz) + 12px)); } }

@keyframes dataStream {
    0% { top: -10%; opacity: 0; transform: scaleY(0.8); }
    15% { opacity: 1; transform: scaleY(1.5); }
    85% { opacity: 1; transform: scaleY(1.5); }
    100% { top: 110%; opacity: 0; transform: scaleY(0.8); }
}

@keyframes pulseBeam {
    0%, 100% { opacity: 0.7; box-shadow: 0 0 15px var(--color-env), 0 0 30px rgba(6,182,212,0.5); }
    50% { opacity: 1; box-shadow: 0 0 30px var(--color-env), 0 0 60px rgba(6,182,212,0.9); }
}

@keyframes drawBridge { to { stroke-dashoffset: 0; } }
```
