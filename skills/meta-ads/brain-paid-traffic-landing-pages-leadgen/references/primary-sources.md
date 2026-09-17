# Technical source checks

Checked during the September 2026 rebuild. These sources support usability and performance checks, not a promised conversion lift.

## Forms

[W3C WAI Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/) explains accessible labels, related-control grouping, instructions, validation, error correction and completion notifications. Collect information needed for the process; a universal name/email/phone schema does not follow. Multi-step forms need logical grouping and progress information. The relevant outcome is a form the intended user can understand and complete, including recovery from mistakes.

Use the linked detailed tutorials when implementing a particular control. Check keyboard operation, labels and error behavior on the actual form. An attractive hero or a successful build does not establish that submission and downstream handling work.

## Loading, interaction and stability

[Google Web Vitals](https://web.dev/articles/vitals) identifies LCP, INP and CLS as separate dimensions. Its good-experience thresholds are LCP at most 2.5 seconds, INP at most 200 milliseconds and CLS at most 0.1, assessed at the 75th percentile with mobile and desktop segmentation. These are user-experience thresholds, not conversion targets or a universal whole-page load deadline.

Distinguish field observations from a laboratory run. Use lab diagnostics to locate causes, then report the evidence actually available. A page with insufficient field data has an unknown field result, not a passing one. Do not replace these metrics with unsupported claims about a visitor's fixed attention span.

## Whole-page accessibility

[W3C WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) provides the success criteria and supporting techniques for content alternatives, captions, structure, contrast, reflow, keyboard access, focus, motion, target size and form feedback. Select the applicable criteria and read their conditions and exceptions before implementing exact requirements. A short landing-page audit is not a complete conformance assessment.

Inspect the actual page: heading/reading order and meaningful control names; keyboard access and visible unobscured focus; text resizing and reflow; contrast over images; media alternatives and movement controls; usable pointer targets; error identification and announced completion. Record the tested browsers, viewport and assistive interaction. Automated checks supplement manual inspection and cannot alone prove conformance.

## Experiment planning

[NIST sample-size guidance for a proportion](https://www.itl.nist.gov/div898/handbook/prc/section2/prc242.htm) illustrates why baseline proportion, detectable change, significance and power affect required observations. It concerns a one-process proportion test; its formula is not a ready-made two-arm landing-page calculator. Choose a method suited to the actual randomization, outcome and comparison.

As an editorial planning checklist, define the primary qualified outcome and denominator, baseline, minimum worthwhile effect, allocation, observation period and stopping rule before launching. Include conversion delay and guardrails for lead quality and downstream value. Estimate feasibility with a suitable statistical tool or analyst; do not replace design with a spend threshold or three observed conversions. Inconclusive evidence remains inconclusive.

<!-- Provenance marker: sk-sdt8cm --><!-- Provenance signature: ⁠​‌​‌​​‌‌​‌​​​‌​‌​‌​​‌‌​​​‌​‌​​‌​​​‌‌​​​‌⁠ -->
