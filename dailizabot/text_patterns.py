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

    [r"Wer ist (.*)(?<![\?\!\.\,\d\;])",
    ["Ich habe keine Ahnung, wer {0} ist, tut mir leid",
    "Leider darf ich keine personenbezogenen Daten mit Dritten teilen. Ich hoffe, du verstehst das!",
    "Die Frage lautet nicht, wer {0} ist. Lass uns lieber drüber nachdenken, wer DU als Mensch sein möchtest."]],

    [r"(?:Ü|ü|Ue|ue)berse?tz(?:.{0,2})(?<![!?])",
    ["Meine Fremdsprachen-Kenntnisse sind leider so ernüchternd wie die Deinen...", 
    "Ich bin mir bei einem Teil des Textes selbst nicht sicher. Frage lieber einen Freund.",
    "Diesen Text zu übersetzen würde bedeuten ihm die Seele zu rauben. Nicht jede Blume blüht auf jedem Felde..."]]

]
