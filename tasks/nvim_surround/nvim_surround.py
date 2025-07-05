"""
nvim-surround: Practice Exercises
---------------------------------
Each block contains:
- Initial text (DO NOT change manually)
- Instruction (do this in Neovim)
- Final text (what it should look like after the command)

Pro tip: Use a comment like "# TRY THIS" to place your cursor and practice!
"""

# === 1. Basic add with normal mode ys ===

def greeting():
    # TRY THIS: Place your cursor on "Hello" and run: ysiw"
    msg = Hello
    # Expected: msg = "Hello"

# === 2. Delete surround (ds) ===

def wrapped_values():
    # TRY THIS: Place cursor on 42 and run: ds)
    data = ({ 42 })
    # Expected: data = { 42 }

# === 3. Change surround (cs) ===

def quoting():
    # TRY THIS: cs'`
    string = 'important'
    # Expected: string = `important`

def taggy():
    # TRY THIS: Place cursor on paragraph and run: cstdiv
    html = <p>paragraph</p>
    # Expected: <div>paragraph</div>

# === 4. Visual mode surround (S) ===

def surround_me():
    # TRY THIS: visually select "world_is_crazy" and press S(
    text = world_is_crazy
    # Expected: text = (world_is_crazy)

# === 5. Insert mode surround (<C-g>s) ===

def insert_example():
    # TRY THIS: In insert mode between '=' and 'k', press <C-g>s'
    item = key
    # Expected: item = 'key'

# === 6. yss / yS / ySS line variants ===

def full_line():
    # TRY THIS: Put cursor anywhere and run yss"
    print("wow full")
    # Expected: "print("wow full")"

def block_tag():
    # TRY THIS: Place cursor and run ySStspan class="fruit"
    element = "banana"
    # Expected:
    # <span class="fruit">
    # element = "banana"
    # </span>

# === 7. Function call surround (f) ===

def args_surround():
    # TRY THIS: ysiwfmake_upper
    param = abc
    # Expected: param = make_upper(abc)

# === 8. HTML tag with attribute ===

def header():
    # TRY THIS: yssth1 id="main"
    Hello World
    # Expected: <h1 id="main">Hello World</h1>

# === 9. Aliases (b → ), r → ]) ===

def alias_example():
    # TRY THIS: yssb → expected: (stuff = item)
    stuff = item
    # TRY THIS: dsr → expected: more = another
    more = [another]

# === 10. Custom delimiters with 'i' ===

def custom_insert():
    # TRY THIS: yssi<CR>**<CR> (insert "**" on both sides)
    example = cool
    # Expected: example = **cool**

# === 11. Tabular alias (q → ', ", `) ===

def quotes_everywhere():
    # TRY THIS: Place cursor in middle and run: dsq 
    s = '"mixed \'quotes\' here"'
    # Expected: s = mixed 'quotes' here

# === 12. Multi-line surround with cursor movement ===

def multiline_test():
    # TRY THIS: put cursor on "check", do <C-g>S[
    if check:
        pass
    # Expected:
    # [
    # if check:
    #     pass
    # ]

"""
Once you finish these, you should be a Surround Sensei™️.
Bonus: Try mapping your own keymaps in `init.lua` to customize this even more.
"""