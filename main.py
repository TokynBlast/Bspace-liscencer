# This does not work yet, I still need to fix replacing, BUT I have an idea for making it simpler!

liscence = '''Bspace Liscence
v0.0.0.1
Bspace Liscence by Tokyn Blast is licensed under Attribution-ShareAlike 4.0 International

You may modify('modify/variation' is as defined below) or rewrite the source code, if it is modified and published, it must stay under the main name([project name]), unless you are given permission by the person/team([creator(s) names)]) that created the [product type]. You must also keep the same liscence.

If a a variation is made of [project name] it is the variations creator to manage that variation.

You may profit(even without profiting, this stil applys) off of a variation you make as long as the creator([project creator(s)]) does not prohibit, stop or deny, (or any other form of prevention) you from making money off of the variation.

You own the rights to youre variation, however the creator(s) may use youre variation for anything, including but not limited to promotion, ideas, examples

A MODIFY/VARIATION IS (but not limited to)
    - Based off of the [product type]([project name])
    - Modified source code
    
When a variation of [project name] is published
On the download page, you must follow the rules below for the quotes below:
"This is a variation of the [project type] [project name] (Licensed under Bspace v0.0.0.1) by [project creator(s)]"
"To get [project name]: [link to f]"
"For [project name] source code: [link to e]"
Rules
[rules for liscencing]'''

open(str(input('File Name? ')) + '.txt.', 'x')

typ = str(input('What is youre project? (EX: game, tool, etc.)? '))
name = str(input(f"What is the {typ}'s name? "))
members = str(input(f'Who developed the {typ} {name}? '))
download = str(input(f'What is the link to download the {typ} {name}? '))
code = str(input(f'What is the link to the source code of the {typ} {name}? '))
rules = str(input(f'''What are the rules to these quotes?
"This is a variation of the {typ} {name} (Licensed under Bspace v0.0.0.1) by {members}"
"To get {name}: {download}"
"For {name} source code: {code}"
'''))

liscence.replace('[project name]', name).replace('[product type]', typ).replace('[project creator(s)]', members).replace('[link to f]', download).replace('[link to e]', code).replace('[rules for liscencing]', rules)
