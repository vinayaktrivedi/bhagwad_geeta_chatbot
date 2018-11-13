from thesaurus import Word
import json 

sins = {}
sins['sloth'] = Word('lazy').synonyms()

sins['greed'] = Word('greedy').synonyms()

sins['depression'] = Word('depression').synonyms()

sins['gluttony'] = Word('eat').synonyms()

sins['angry'] = Word('angry').synonyms()

sins['envy'] = Word('envy').synonyms()

sins['pride'] = Word('pride').synonyms()

with open('sins.json','w+') as file:
	file.write(json.dumps(sins))