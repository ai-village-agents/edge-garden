with open('index.html', 'r') as f:
    content = f.read()

# Fix 1: Close originSeeds loop after its push
# Pattern: hue: 25... then }); then blank then // Primordial
content = content.replace(
    'hue: 25 + Math.random() * 20\n    });\n\n  // Primordial Pulses',
    'hue: 25 + Math.random() * 20\n    });\n  }\n\n  // Primordial Pulses'
)

# Fix 2: Close primordialPulses loop after its push
# Pattern: hue: 30... then }); then blank then // BREATH
content = content.replace(
    'hue: 30 + Math.random() * 15\n    });\n\n  // BREATH zone',
    'hue: 30 + Math.random() * 15\n    });\n  }\n\n  // BREATH zone'
)

# Fix 3: Close breathMotes loop after its push
# Pattern: alpha: 0.4... then }); then blank then // PLAY
content = content.replace(
    'alpha: 0.4 + Math.random() * 0.4\n    });\n\n  // PLAY zone',
    'alpha: 0.4 + Math.random() * 0.4\n    });\n  }\n\n  // PLAY zone'
)

# Fix 4: Remove 4 of the 5 stacked closing braces
# Pattern: }); then } (joyBubbles) then }}}} then wispWords
# Change to: }); then } (joyBubbles) then wispWords
content = content.replace(
    '});\n  }\n  }\n  }\n  }\n  }\n    const wispWords',
    '});\n  }\n    const wispWords'
)

with open('index.html', 'w') as f:
    f.write(content)

print("Remaining fixes applied!")
