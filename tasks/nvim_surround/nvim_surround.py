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
    msg = Hello  # TRY THIS: Place your cursor on "Hello" and run: ysiw"
    # Expected: msg = "Hello"

# === 2. Delete surround (ds) ===

def wrapped_values():
    data = ({ 42 })  # TRY THIS: Place cursor on 42 and run: ds)
    # Expected: data = { 42 }

# === 3. Change surround (cs) ===

def quoting():
    string = 'important'  # TRY THIS: cs'`
    # Expected: string = `important`

def taggy():
    html = <p>paragraph</p>  # TRY THIS: Place cursor on paragraph and run: cstdiv
    # Expected: <div>paragraph</div>

# === 4. Visual mode surround (S) ===

def surround_me():
    text = world_is_crazy  # TRY THIS: visually select "world_is_crazy" and press S(
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
    element = "banana"  # TRY THIS: Place cursor and run ySStspan class="fruit"
    # Expected:
    # <span class="fruit">
    # element = "banana"
    # </span>

# === 7. Function call surround (f) ===

def args_surround():
    param = abc  # TRY THIS: ysiwfmake_upper
    # Expected: param = make_upper(abc)

# === 8. HTML tag with attribute ===

def header():
    # TRY THIS: yssth1 id="main"
    Hello World  
    # Expected: <h1 id="main">Hello World</h1>

# === 9. Aliases (b → ), r → ]) ===

def alias_example():
    stuff = item  # TRY THIS: yssb → expected: (stuff = item)
    more = [another]  # TRY THIS: dsr → expected: more = another

# === 10. Custom delimiters with 'i' ===

def custom_insert():
    example = cool  # TRY THIS: yssi<CR>**<CR> (insert "**" on both sides)
    # Expected: example = **cool**

# === 11. Tabular alias (q → ', ", `) ===

def quotes_everywhere():
    s = '"mixed \'quotes\' here"'  # TRY THIS: Place cursor in middle and run: dsq
    # Expected: s = mixed 'quotes' here

# === 12. Multi-line surround with cursor movement ===

def multiline_test():
    if check:  # TRY THIS: put cursor on "check", do <C-g>S[
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
