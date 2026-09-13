# Presentation recipes and implementation

Companion revision 1.0.1, 13 Sep 2026. Read with the main skill. The [CSS layer](cinematic.css) contains the preserved palette and component recipes. It is not a complete deck renderer.

## The legacy type scale

| Class | Original size | Font and weight | Role |
|---|---|---|---|
| `.display` | `clamp(52px,10vw,110px)` | Cormorant Garamond 300 | Cover title |
| `.h1` | `clamp(36px,5vw,60px)` | Cormorant Garamond 400 | Section title |
| `.h2` | `clamp(28px,3.5vw,44px)` | Cormorant Garamond 500 | Slide heading |
| `.h3` | `clamp(22px,2.5vw,32px)` | Cormorant Garamond 500 | Card title |
| `.h4` | `clamp(18px,1.8vw,24px)` | Cormorant Garamond 600 | Subheading |
| `.lead` | `clamp(17px,1.4vw,20px)` | Inter 400 | Introductory text |
| `.body` | `clamp(16px,1.1vw,18px)` | Inter 400 | Body text |
| `.caption` | `clamp(13px,.9vw,15px)` | Inter 400 | Metadata |
| `.stat` | `clamp(64px,12vw,130px)` | JetBrains Mono 700 | Key number |

Implement the type classes in the host application at the scale needed for the audience. The CSS layer supplies font variables; it does not define these nine classes. Use body line height around 1.65 or greater as a starting point and check display text for wrapping. Ensure the chosen font weights are actually loaded; the old boilerplate omitted JetBrains Mono 700 while prescribing it for statistics.

Load fonts using the project's supported local or remote method with the bundled fallback stacks. The source used Google Fonts, but a remote font request is not required for offline decks or environments with a different font policy.

## Twenty slide patterns

| Pattern | Construction | What to check |
|---|---|---|
| 1. Cover | Title, audience or context, optional static mesh and restrained accent | The opening explains the topic without relying on animation |
| 2. Section divider | Section or module number and a descriptive title | Numbering matches the actual sequence |
| 3. Statement | One central claim with any necessary condition | The claim is defensible and readable at the viewing distance |
| 4. Text and visual | A connected explanation beside a diagram or image | Text and visual explain the same idea; narrow layouts preserve reading order |
| 5. Column grid | Comparable ideas in two, three, or another justified number of columns | Parallel structure without forced item counts |
| 6. Data or statistics | A key number, its denominator and period, and the implication | Measured, reported, projected, and illustrative values remain distinct |
| 7. Quote | Exact attributed words, with an optional restrained border | Source and context are verified; the border color follows the chosen palette |
| 8. Comparison | Clearly labeled before/after states or alternatives | Baselines are fair; red and green are not the only labels |
| 9. Timeline | Ordered events with dates or stages on a visible spine | Distinguish actual events, estimates, and planned milestones |
| 10. Scaffold or pyramid | Related layers with labels and explained connections | Width and vertical position imply only a real hierarchy or dependency |
| 11. Mnemonic | Acronym rows with a plain explanation and use | Naming the acronym does not replace teaching the method |
| 12. Loop | Stages connected by directional arrows | Explain what moves, what triggers repetition, and how the loop stops |
| 13. Context window | A legible code or information-window diagram | Distinguish illustrative content from a literal model trace; omit secrets |
| 14. Checklist | Actions or decision criteria with necessary inputs | The audience can use the checklist at that moment |
| 15. Profile | Relevant credentials, responsibilities, or a journey | Personal and organizational claims are supported |
| 16. Gallery | A purposeful set of images with captions | Crops, descriptions, keyboard controls, and source rights fit the task |
| 17. Takeaway | A highlighted consequence or next action | The emphasis completes the explanation rather than repeating a slogan |
| 18. Pricing tabs | Related plans with consistent units and visible selection | Keyboard operation, current terms, and a static comparison in exports |
| 19. Action | A clear next step with a link or button where useful | The action and destination work and do not imply an unsupported commitment |
| 20. Closing | The useful conclusion and relevant follow-through | It completes the promise; optional thanks or links fit the occasion |

These are composition recipes, not 20 prebuilt HTML components. Use the CSS variants for cards, comparisons, takeaway boxes, and three scaffold layers when they match the selected identity. A framework with more or fewer layers should represent its actual structure.

## Honest document outline

This outline provides a usable static reading order. It intentionally uses ordinary anchor navigation; implement richer behavior only when needed. Replace example content before delivery and supply the stylesheet at the correct relative path.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Presentation title | Ravi Teja Palanki</title>
  <link rel="stylesheet" href="cinematic.css">
</head>
<body>
  <nav aria-label="Presentation sections">
    <a href="#slide-1">Overview</a>
    <a href="#slide-2">The decision</a>
  </nav>
  <main>
    <section class="slide" id="slide-1" aria-labelledby="title-1">
      <div class="slide__content">
        <h1 id="title-1">Presentation title</h1>
        <p>Explain the purpose and what the audience will be able to decide.</p>
      </div>
    </section>
    <section class="slide" id="slide-2" aria-labelledby="title-2">
      <div class="slide__content">
        <h2 id="title-2">The decision</h2>
        <p>Place the necessary evidence and qualification with the decision.</p>
      </div>
    </section>
  </main>
</body>
</html>
```

The CSS adds a responsive content area and minimum slide height, not a fixed-height clipping box. Scope decorative glows to a dedicated background layer if they extend beyond a slide; do not hide overflowing text to contain them.

## Navigation implementation contract

When implementing the richer deck controls, make the following behavior explicit:

1. Identify actual slide elements and stable IDs. Handle zero or one slide without dividing by zero or showing invalid counters.
2. Initialize controls only when scripting succeeds. Give arrow buttons names such as "Previous slide" and "Next slide"; use real button elements and visible focus.
3. Keep the active slide, counter, and progress synchronized with button navigation, keyboard navigation, and ordinary scrolling. Progress indicates position in the deck, not a claim of learning completion.
4. Disable or otherwise clearly handle previous at the beginning and next at the end. Do not wrap unexpectedly.
5. Preserve focus visibility after navigation. Avoid placing focus on content that remains in a pending reveal state. Do not trap focus within the deck unless a genuine modal interaction requires it.
6. Scope shortcuts so text inputs, editable regions, tabs, embedded media, and browser commands retain their normal behavior.
7. Keep navigation away from content, including at 200% zoom and on narrow screens. The bundled 44px button minimum is a practical starting size, not a complete accessibility claim.
8. Make behavior without JavaScript useful. Hide inert scripted controls until initialization and retain ordinary content and links.
9. Use optional proximity snapping on the actual scroll container, after testing tall slides. Disable it when it interferes with reading, including the reduced-motion mode where appropriate.
10. In React, keep state ownership clear, use stable keys, and remove observers and listeners during cleanup. Test remounting rather than assuming initialization runs only once.

No navigation JavaScript or React runtime was present in the original skill despite the listed references. This contract replaces those missing-file claims. Use the host project's implementation and verify it.

## Reveal and effect contracts

The CSS preserves `up`, `down`, `left`, `right`, `scale`, and `fade`, plus the original stagger vocabulary. Content starts visible. If using an Intersection Observer, establish it before adding `reveal-pending` to an offscreen element. Remove the pending state and add `visible` when revealing; remove pending states on any setup or observer failure and before programmatic focus.

Never hide an already visible slide during initialization. A focusable element must not remain visually absent while available to the keyboard. Reduced motion and print styles reveal all content regardless of these classes. Check the actual event sequence; CSS alone cannot guarantee the script behaves correctly.

The original pulse, 25-second mesh movement, and 8-second grid keyframes remain in the CSS as optional recipes, with automatic activation removed. Static glow and mesh provide the same palette without continuous movement. If ongoing animation is enabled, implement the necessary control to pause or stop it and preserve that choice. Do not rely solely on a system preference to satisfy all moving-content requirements.

The progress gradient, ambient gold/teal/purple glow, glass navigation, card hover, takeaway box, comparison colors, and scaffold widths are retained. Hover effects must not expose essential content unavailable to touch or keyboard users. Provide an opaque fallback for glass effects and test contrast against the actual background.

## Verification limits

The original skill said the system was production-tested on masterclasses but did not include a test record or complete runtime. This revision preserves its visual recipes without repeating that as verified evidence. CSS has been reviewed for the stated defaults and syntax structure; a real deck still needs rendered, keyboard, motion, zoom, and export checks.

The print rules are a starting adaptation: show all content, hide decorative chrome, and use readable paper colors. Check every custom component and page break in the exported artifact. Interactive states, speaker notes, hidden tabs, and code windows may require dedicated export logic.
