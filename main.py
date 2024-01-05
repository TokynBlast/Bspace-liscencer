mult = int(input('How many things do you want to liscence?'))

for i in range(mult):
	fName = str(input('File Name? (Dont add the extension type yet!)'))
	end = str(input('File ending? '))
	# Check if a '.' was added to the beginning of the file extension type input
	if not end.startswith('.'): end = '.' + end
	# Finish the naming of the file
	fName += end
# remove!! fjeroawqeioukjweqi9rueikjfo3i9r8guijkfl	9i4uitjkli9rfeuijkli	329rfeuijkfelo	e2i9rofjefjvhui bgj n3jiuhfrygevbn
	try: open(fName, 'x')
	except: None

	# Get inputs
	typ = str(input('What is youre project (EX: game, tool, etc.)? '))
	name = str(input(f"What is the {typ}'s name? "))
	members = str(input(f"Who developed the {typ} {name} (Digital or real names, not 'me')? "))
	download = str(input(f'What is the link to download the {typ} {name}? '))
	code = str(input(f'What is the link to the source code of the {typ} {name}? '))
	ver = 'v0.0.0.2'
	print(f'''What are the rules to these quotes?
	"This is a variation of the {typ} {name} (Licensed under Bspace {ver}) by {members}"
	"To get {name}: {download}"
	"For {name} source code: {code}"
	''')
	# Create and write to file
	with open(fName, 'w') as d:
		d.write(f'''Bspace Liscence
	{ver}
	Bspace Liscence by Tokyn Blast is licensed under Attribution-ShareAlike 4.0 International
	
	You may modify('modify/variation' is as defined below) or rewrite the source code, if it is modified and published, it must stay under the main name({name}), unless you are given permission by the person/team({members}) that created the {typ}. You must also keep the same liscence.
	
	If a a variation is made of {name} it is the variations creator to manage that variation.
	
	You may profit(even without profiting, this stil applys) off of a variation you make as long as atleast one of the creator(s)({members}) does not prohibit, stop or deny, (or any other form of prevention) you from making money off of the variation.
	
	You own the rights to youre variation, however {members} may use youre variation for anything, including but not limited to promotion, ideas, examples
	
	A MODIFY/VARIATION IS (but is not limited to)
	    - Based off of the {typ}({name})
	    - Modified source code
	    
	When a variation of {name} is published
	On the download page, you must follow the rules below for the quotes below:
	"This is a variation of the {typ} {name} (Licensed under Bspace {ver}) by {members}"
	"To get {name}: {download}"
	"For {name} source code: {code}"
	Rules
	[rules]''')
	
	print('It is done!\nYou will have to enter the rules manually, as this feature is not in v0.2')
