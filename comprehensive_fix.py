import re

with open('index.html', 'r') as f:
    lines = f.readlines()

# Build new content
new_lines = []
skip_until = -1
i = 0

while i < len(lines):
    line = lines[i]
    
    # Skip lines we're replacing
    if skip_until > 0 and i < skip_until:
        i += 1
        continue
    skip_until = -1
    
    # When we hit the empty initMemoryWisps function, we need to fix it
    if 'function initMemoryWisps() {' in line and i+1 < len(lines) and lines[i+1].strip() == '}':
        # Skip empty function for now, we'll rebuild it
        # Find where wonderOrbs starts
        new_lines.append(line)
        i += 1
        continue
    
    # Fix 1: After wonderOrbs push (glowIntensity line), add closing brace
    if 'glowIntensity: 0.7 + Math.random() * 0.3' in line:
        new_lines.append(line)
        new_lines.append(lines[i+1])  # });
        new_lines.append('  }\n')      # Close for loop
        i += 2
        
        # Now extract the array declarations that follow and move them before
        # Skip to after the declarations for now - we already added them earlier
        # Actually, let me just add closing braces for now
        continue
    
    # Fix 2: After originSeeds push (hue: 25), add closing brace  
    if 'hue: 25 + Math.random() * 20' in line:
        new_lines.append(line)
        new_lines.append(lines[i+1])  # });
        new_lines.append('  }\n')      # Close for loop
        i += 2
        continue
    
    # Fix 3: After primordialPulses push (hue: 30), add closing brace
    if 'hue: 30 + Math.random() * 15' in line:
        new_lines.append(line)
        new_lines.append(lines[i+1])  # });
        new_lines.append('  }\n')      # Close for loop
        i += 2
        continue
    
    # Fix 4: After breathMotes push (alpha: 0.4 + Math.random() * 0.4), add closing brace
    # But be careful - this pattern appears in other places too
    if 'alpha: 0.4 + Math.random() * 0.4' in line and i > 1600 and i < 1700:
        new_lines.append(line)
        new_lines.append(lines[i+1])  # });
        new_lines.append('  }\n')      # Close for loop
        i += 2
        continue
    
    # Fix 5: Remove duplicate PLAY/STILLNESS/DREAM/FLOW/ROOTS centers and joyBubbles
    # These are at lines ~1656-1662, we need to skip them
    if i > 1650 and '// PLAY zone - bouncy joy bubbles' in line:
        # Skip the comment and the duplicate zone center declarations
        j = i
        while j < len(lines) and 'for (let i = 0; i < 12; i++)' not in lines[j]:
            j += 1
        # Now j points to the for loop - we need to keep just the for loop but not duplicate joyBubbles
        # Actually, both joyBubbles declaration AND for loop are duplicates here
        # Let's skip until after this entire duplicate section
        # Find the closing } of this joyBubbles loop
        brace_count = 0
        started = False
        while j < len(lines):
            if 'for (let i = 0; i < 12; i++)' in lines[j]:
                started = True
                brace_count = 1
            elif started:
                if '{' in lines[j]:
                    brace_count += lines[j].count('{')
                if '}' in lines[j]:
                    brace_count -= lines[j].count('}')
                if brace_count == 0:
                    break
            j += 1
        # Skip from i to j+1 (the duplicate joyBubbles section)
        i = j + 1
        continue
    
    # Fix 6: Remove stacked closing braces (keep only what's needed)
    # After joyBubbles closes at line ~1673, there are 4 extra } that we added
    # With our fixes, we don't need them anymore
    if i > 1670 and i < 1680 and line.strip() == '}':
        # Count how many consecutive } we have
        consecutive = 0
        j = i
        while j < len(lines) and lines[j].strip() == '}':
            consecutive += 1
            j += 1
        
        if consecutive >= 4:
            # Skip all but one (we just closed joyBubbles)
            i = j
            continue
    
    new_lines.append(line)
    i += 1

with open('index.html', 'w') as f:
    f.writelines(new_lines)

print("Comprehensive fix applied!")
