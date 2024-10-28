"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"Ich brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],

    [r"Magst du (.*)",
    ["Ja, {0} kann wirklich interessant sein!",
    "Manchmal mag ich {0}, es hängt ganz vom Kontext ab.",
    "Erzähl mir, warum du {0} magst."]],

    [r"Ich fühle mich (.*)",
     ["Warum fühlst du dich {0}?",
    "Seit wann fühlst du dich {0}?",
    "Fühlst du dich oft {0}?"]],


]
