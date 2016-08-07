from jinja2.lexer import Lexer, compile_rules
from jinja2.environment import Environment
from jinja2.parser import Parser
from jinja2 import nodes
import re


env = Environment()
le = Lexer(env)
source = r'''{% for user in users %}\n<html>\n    Hello {{ user }}\n</html>\n{% endfor %}'''
pas = Parser(env, source)
token = le.tokenize(source)

for x in token:
    print((x.lineno, x.type, x.value))
m = pas.subparse()
print(m)

result = nodes.Template(m, lineno=1)
print(result)

rex = r'(?P<raw_begin>(?:\{\%\+?)\s*raw\s*(?:\%\}\+?))'
s = '{% raw %}'
rec = re.compile(rex)
m = rec.match(s)
print(m.groupdict())

rule = compile_rules(env)
print(rule)

from jinja2 import _stringdefs
rec1 = re.compile('(.*?)(?:(?P<block_begin>\{\%))')
n = rec1.match(r'''<html>     Hello {{ user }} </html> {% endfor %}''')
print(n.group(2))

mm = 'ss'

bbs = 'new'