with open('index.html', 'r') as f:
    lines = f.readlines()

# Find key line numbers (0-indexed)
wonder_for_line = None
origin_comment_line = None

for i, line in enumerate(lines):
    if 'const wonderOrbs = [];' in line:
        wonder_for_line = i + 1  # next line is the for loop
    if '// ORIGIN zone - seeds of creation' in line:
        origin_comment_line = i

print(f"wonderOrbs for loop at line {wonder_for_line + 1}")
print(f"ORIGIN comment at line {origin_comment_line + 1}")

# Lines 1599-1612 (0-indexed: 1598-1611) contain array declarations
# They need to move to before wonderOrbs for loop (before line 1583)

# First, extract the lines we need to move (the array declarations)
# Looking at line 1596-1612 in 1-indexed = 1595-1611 in 0-indexed
# The structure is:
# 1594: });  (close wonderOrbs push)
# 1595: empty
# 1596: // ORIGIN zone comment  
# 1597: const ORIGIN_ZONE_CENTER
# 1598: const originSeeds = [];
# 1599-1612: const shadowWisps, harmonyNotes, etc.
# 1613: for originSeeds loop

# We need to:
# 1. After line 1594, add } to close wonderOrbs
# 2. Move array declarations (shadowWisps through depthParticles) before wonderOrbs for loop

# Find the closing }); of wonderOrbs push (after glowIntensity)
for i, line in enumerate(lines):
    if 'glowIntensity: 0.7 + Math.random() * 0.3' in line:
        wonder_push_close = i + 1  # next line should be });
        print(f"wonderOrbs push close at line {wonder_push_close + 1}: {lines[wonder_push_close].strip()}")
        break

# Find the array declarations to extract
array_decl_start = None
array_decl_end = None
for i, line in enumerate(lines):
    if 'const shadowWisps = [];' in line:
        array_decl_start = i
    if 'const depthParticles = [];' in line:
        array_decl_end = i
        break

print(f"Array declarations: lines {array_decl_start + 1} to {array_decl_end + 1}")

# Extract array declarations
array_decls = lines[array_decl_start:array_decl_end + 1]
# Normalize indentation to 2 spaces
array_decls_normalized = ['  ' + line.strip() + '\n' for line in array_decls]

print("Array declarations to move:")
for line in array_decls_normalized:
    print(f"  {line.strip()}")

# Now build the fixed file
# Step 1: Remove the array declarations from their current position
# Step 2: Insert them before the wonderOrbs for loop
# Step 3: Add closing } after wonderOrbs push

# Find the line with "const wonderOrbs = [];"
for i, line in enumerate(lines):
    if 'const wonderOrbs = [];' in line:
        insert_before = i
        print(f"Will insert arrays before line {insert_before + 1}")
        break

# Build new content
new_lines = []
i = 0
while i < len(lines):
    # Insert array declarations before wonderOrbs declaration
    if i == insert_before:
        for decl in array_decls_normalized:
            new_lines.append(decl)
        new_lines.append('\n')
    
    # Skip the original array declarations
    if i >= array_decl_start and i <= array_decl_end:
        i += 1
        continue
    
    new_lines.append(lines[i])
    
    # Add closing brace after wonderOrbs push
    if 'glowIntensity: 0.7 + Math.random() * 0.3' in lines[i]:
        # Next line should be });
        new_lines.append(lines[i + 1])  # the });
        new_lines.append('  }\n')  # close the for loop
        i += 2
        continue
    
    i += 1

with open('index.html', 'w') as f:
    f.writelines(new_lines)

print("Fix applied!")
