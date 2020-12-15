# LISTED01
"""Description: Single/multiple words enclosed in straight/curly double quotes in normal or bold and/or italic font followed by the following words:
    • mean
    • means
    • shall mean
    • shall has the meaning
    • shall have the meaning
    • has the meaning
    • have the meaning
    • shall bear the meaning
    • has the same meaning
    • shall have the same meaning

Examples:

"Acquisition Costs" means all fees, costs and expenses…
“Acquisition Costs“ means all fees, costs and expenses…
"Acquisition Costs" shall mean all fees, costs and expenses…
“Acquisition Costs” shall mean all fees, costs and expenses…
"Acquisition Costs" means all fees, costs and expenses…
“Acquisition Costs” means all fees, costs and expenses…
"Acquisition Costs" shall mean all fees, costs and expenses…
“Acquisition Costs” shall mean all fees, costs and expenses…

NOTE: The term and definition can be located in different paragraphs:

"Acquisition Costs"
means all fees, costs and expenses…
“Acquisition Costs“
means all fees, costs and expenses…
"Acquisition Costs"
shall mean all fees, costs and expenses…
“Acquisition Costs”
shall mean all fees, costs and expenses…"""

KEY_WORDS = [
    ['mean'],
    ['means'],
    ['shall', 'mean'],
    ['shall', 'has', 'the', 'meaning'],
    ['shall', 'have', 'the', 'meaning'],
    ['has', 'the', 'meaning'],
    ['have', 'the', 'meaning'],
    ['shall', 'bear', 'the', 'meaning'],
    ['has', 'the', 'same', 'meaning'],
    ['shall', 'have', 'the', 'same', 'meaning'],
]


def find_in_quotes(words):
    for word in words:
        first = word['word'][0]
        if (first == r"""'""") or (first == r""""""""):
            pass
