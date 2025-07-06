# Visual-Multi Interactive Practice File
#
# This file is designed like `vimtutor`. Open it in Neovim and work through each section.
# Use it to learn and practice the Visual-Multi plugin.
#
# INSTRUCTIONS:
# - Follow the steps listed under each exercise.
# - Add your own notes, edits, and test cases inline.
# - Use Neovim with Visual-Multi installed!

################################################################################
# SECTION 1: Basic Selection & Navigation
################################################################################

# EXERCISE 1.1: Select all instances of the word 'foo'
# INSTRUCTIONS:
# 1. Move cursor to any 'foo'
# 2. Press <C-n> repeatedly to select all
# 3. Use 'n', 'N' to move through
# 4. Use 'Q' to remove current region
foo
foo
bar
foo


# EXERCISE 1.2: Skip every other 'bar' using 'q'
# INSTRUCTIONS:
# 1. Search for 'bar' using <C-n>
# 2. Use 'q' to skip every other
# 3. Try 'Q' to remove one
bar
bar
bar
bar


# EXERCISE 1.3: Use \A to select all instances of 'hello'
# INSTRUCTIONS:
# 1. Place cursor on 'hello'
# 2. Press \\A to select all occurrences
hello
world
hello
hi
hello


################################################################################
# SECTION 2: Column Cursors with <C-Down> / <C-Up>
################################################################################

# EXERCISE 2.1: Prefix each item with '- '
# INSTRUCTIONS:
# 1. Place cursor on first item
# 2. Press <C-Down> three times
# 3. Type '- ' to add prefix
milk
eggs
cheese
bread


# EXERCISE 2.2: Number the tasks
# INSTRUCTIONS:
# 1. Select all lines with <C-Down>
# 2. Run \\n and input: 1/1/.  (for 1. 2. 3.)
task one
task two
task three


# EXERCISE 2.3: Append text using A
# INSTRUCTIONS:
# 1. Select column with <C-Down>
# 2. Press A and type ' - done'
# 3. Press <Esc> to exit insert
fix bug
write tests
refactor code


################################################################################
# SECTION 3: Regex Selection
################################################################################

# EXERCISE 3.1: Match all foo+numbers
# INSTRUCTIONS:
# 1. Press \\/ and input: foo\d+
# 2. Press 'n' to navigate matches
# 3. Use R to replace with something
foo1
foo22
foo333
notfoo
bar2


# EXERCISE 3.2: Match emails
# INSTRUCTIONS:
# 1. Use regex: [\w.%+-]+@[\w.-]+\.[a-z]{2,}
# 2. Use \\/ to find and \f to filter domains
user@example.com
admin@localhost
test@test.org


# EXERCISE 3.3: Replace phone numbers
# INSTRUCTIONS:
# 1. Regex: \(\d{3}\) \d{3}-\d{4}
# 2. Replace with R and custom format
Call me at (123) 456-7890 or (987) 654-3210.


################################################################################
# SECTION 4: Run Commands at Cursors
################################################################################

# EXERCISE 4.1: Delete words using daw
# INSTRUCTIONS:
# 1. Select each 'const' line with <C-n>
# 2. Run \\z then type: daw
const a = 1;
const b = 2;
const c = 3;


# EXERCISE 4.2: Run macro on each cursor
# INSTRUCTIONS:
# 1. Record a macro in register 'a'
# 2. Select lines, then run \\@ and enter 'a'
echo 'hi'
echo 'bye'
echo 'end'


# EXERCISE 4.3: Use ex command across cursors
# INSTRUCTIONS:
# 1. Select lines
# 2. Run \\x and enter :s/foo/bar/
foo one
foo two
foo three


################################################################################
# SECTION 5: Transformations & Case Conversion
################################################################################

# EXERCISE 5.1: Convert numbers to percentages
# INSTRUCTIONS:
# 1. Select numbers with <C-n>
# 2. Run \\e and input: string(%f*100).'%'
0.1
0.25
0.75


# EXERCISE 5.2: Convert to PascalCase
# INSTRUCTIONS:
# 1. Select camelCase words
# 2. Press \\C and choose 'P'
multiCursorMagic
helloWorld
visualMultiPower


# EXERCISE 5.3: Uppercase every other region
# INSTRUCTIONS:
# 1. Select regions
# 2. Use \\e and input: %i%2 ? toupper(%t) : %t
first
second
third
fourth


################################################################################
# SECTION 6: Advanced Filters
################################################################################

# EXERCISE 6.1: Keep lines starting with 'enable'
# INSTRUCTIONS:
# 1. Select all lines
# 2. Run \\f and use pattern: ^enable.*
disable_cache
enable_feature
enable_logging
skip_check


# EXERCISE 6.2: Remove every 3rd region
# INSTRUCTIONS:
# 1. Select regions
# 2. Use \\e and input: %i%3-2 ? %t : ''
one
two
three
four
five
six


# EXERCISE 6.3: Use \R to remove every 2nd
# INSTRUCTIONS:
# 1. Select regions
# 2. Press \\R and input 2
apple
banana
cherry
date
elderberry
fig
