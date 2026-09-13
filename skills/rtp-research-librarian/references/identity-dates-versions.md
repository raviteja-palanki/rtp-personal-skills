# Identity, dates, and versions

Use this reference after the main filing procedure. Record a filename's evidence rather than making the filename carry an unsupported certainty.

## Identify the source

Read the actual title and enough body to confirm it. A first page may contain another article's navigation, a browser print header, or an unrelated transcript panel. When title and body disagree, preserve the original file and describe what is identifiable. The historical “Founder Mindset / Tim Ferriss” capture contained a Cold Call conversation with George Serafeim and Dimitri Papalexopoulos about Titan Cement; identifying that body fixed the label while revealing that the intended article still needed recapture.

Likewise, 104 files described as weak-signal articles were progress markers, and three supposed logos were a shared trace-audit comparison. Inherited descriptions are useful leads, not verification.

## Establish date and precision

1. Look for the actual publication or edition dateline in the content.
2. If needed, check the publisher's current record, original episode page or a matching authoritative catalog record.
3. Use existing filename dates as leads to corroborate, especially for abbreviated years.
4. Treat PDF/DOCX/PPTX creation/modification metadata, EXIF, screenshot names and source-folder dates as evidence of capture, file creation or a broad period—not automatically publication.
5. Record what remains unknown. A date-scoped quarter folder does not establish a month; a two-digit year does not always mean the 2000s.

In the August 2, 2026 eval-resource batch, thirteen PDFs shared the capture line `8/2/26, 11:24 AM` while their actual publication dates ranged from March 2025 to July 2026. Taking the first printed date would erase the useful chronology. Repeated capture timestamps are a warning sign, not proof that all other dates are publication dates.

| Type | Useful publication evidence | Limit |
|---|---|---|
| PDF/web capture | Article dateline, publisher/edition page | Browser header and PDF metadata often describe saving |
| DOCX/PPTX | Title page/slide, authored date statement | Core properties can describe file creation or editing |
| Image/screenshot | Visible post/article date with identified source | EXIF/screenshot filename usually gives capture date |
| Transcript | Episode publication record or explicit header | Guest name and download date do not establish publication |
| Book | Exact edition's publisher record | Early release and final publication are different states |
| Markdown/text | Attributed frontmatter/header date | A synthesis-note date is not necessarily the source date |

Typical names:

```text
The Art of Asking Smarter Questions_Mar_2026.pdf
A Guide to Context Engineering for PMs - by Aakash Gupta_Nov_2025.pdf
2026 AI & Data Leadership Executive Benchmark Survey_Jan_2026.pdf
Framework Poster_undated.png
```

If a capture date is useful, label it explicitly as capture and retain publication as unknown in metadata. Do not silently put capture into a publication-date column. Keep an image set's date on the set folder; ordered members need not repeat it. Book chapters inherit the edition context and need not each repeat the year.

## Group versions and format variants

Identify explicit markers such as v1/v2, Rev B, Second Edition, Draft/Final or Updated, and compare substantive differences. Different size or date suggests investigation, not a conclusion about completeness or chronology.

Use the publisher's actual version label. Do not invent v1/v2 because two captures exist. A consistent new-name pattern is `Title_<version>_CURRENT_Mon_YYYY.ext`, keeping the publication month/year at the end; existing `Title_v2_Mon_YYYY_CURRENT.ext` records can remain until a scoped rename is warranted. `_CURRENT` identifies the established preferred reading artifact, not guaranteed present-day factual validity.

```text
04_ai-pm-os/strategy/AI Strategy Guide_versions/
  AI Strategy Guide_v2_CURRENT_Jan_2026.pdf
  AI Strategy Guide_v1_Apr_2025.pdf
  _VERSIONS.md
```

`_VERSIONS.md` records each filename, publication/revision/capture dates as applicable, source, edition/format, known differences and preferred-copy basis. Use “change not documented” when necessary. If currency is unresolved, say so and defer the marker. Move a prior marker only when the new artifact's relationship is established.

Keep superseded editions; they can show how a position changed. Format variants also remain together. The historical Hamel Husain/Shreya Shankar eval guide appeared as a 34-page web capture (11,328 extracted words including navigation) and a 39-page authored PDF (11,943 words with contents), both dated May 2025. These local observations illustrate why matching title/date does not establish byte identity. Prefer the clean authored copy only after checking that it is complete for the intended reading; retain and label the web capture.

Book editions remain separate complete folders, such as `Title, Second Edition by Author_Year/`, with cross-references where useful. Never scatter chapters between topical shelves to improve folder balance.

## Choose the right freshness test

Fast-moving claims about model capabilities, pricing and APIs need current verification; even a recent source can be superseded. The former roughly eighteen-month rule is a review prompt, not an expiration date. Foundational methods may remain useful for decades. Label historical evidence and early-release status accurately, compare relevant later corrections, and explain when age changes the conclusion.
