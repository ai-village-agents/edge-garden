import re

with open('index.html', 'r') as f:
    content = f.read()

# Fix 1: After wonderOrbs push, add closing brace
# Pattern: glowIntensity line followed by }); then blank line and comment about ORIGIN
content = re.sub(
    r'(glowIntensity: 0\.7 \+ Math\.random\(\) \* 0\.3\n    \}\);)\n\n(  // ORIGIN zone)',
    r'\1\n  }\n\n\2',
    content
)

# Fix 2: After originSeeds push, add closing brace
# Pattern: hue: 25 line followed by }); then blank line and comment about Primordial
content = re.sub(
    r'(hue: 25 \+ Math\.random\(\) \* 20\n    \}\);)\n\n(  // Primordial Pulses)',
    r'\1\n  }\n\n\2',
    content
)

# Fix 3: After primordialPulses push, add closing brace
# Pattern: hue: 30 line followed by }); then blank line and comment about BREATH
content = re.sub(
    r'(hue: 30 \+ Math\.random\(\) \* 15\n    \}\);)\n\n(  // BREATH zone)',
    r'\1\n  }\n\n\2',
    content
)

# Fix 4: After breathMotes push, add closing brace  
# Pattern: alpha: 0.4 line followed by }); then blank line and comment about PLAY
content = re.sub(
    r'(alpha: 0\.4 \+ Math\.random\(\) \* 0\.4\n    \}\);)\n\n(  // PLAY zone)',
    r'\1\n  }\n\n\2',
    content
)

# Fix 5: Remove 4 of the 5 stacked closing braces
# Pattern: }); then } then }}}} - change to }); then } only
content = re.sub(
    r'(\n  \}\n  \}\n  \}\n  \}\n  \})\n(    const wispWords)',
    r'\n  }\n\2',
    content
)

with open('index.html', 'w') as f:
    f.write(content)

print("Fixes applied!")
