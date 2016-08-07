from flask import Flask
from app import create_app
from werkzeug.urls import url_join
from werkzeug.routing import _rule_re, ValidationError
from werkzeug._compat import iteritems
from re import escape
import re
'''
a = 1
b = 1
c = 'aaaa'
d = ''
print((not a or not b) and c or d)
'''
bb = '/api/v1.0/posts/<int:id>/comments/'
app = create_app('default')
print(app.error_handler_spec)

'''
print(app.url_map._rules[-2])
print(app.url_map._rules[-2]._regex)
print(app.url_map._rules[-2]._trace)
a = app.url_map._rules[-2]._regex
print(_rule_re.match(bb).groupdict())
print(escape('/api/v1.0/posts/'))
y = [escape('/api/v1.0/posts/')]
print(u''.join(y))
s = '\/api\/v1\.0\/posts\/'
p = re.compile(r'\/api\/v1\.0\/posts\/', re.UNICODE)
print(p)

b = '|/api/v1.0/posts/50/comments/'
x = a.search(b)
print(x)
m = x.group()

n = x.groupdict()
print(m)
print(n)

if 1 and not 0 and not n.pop('__suffix__'):
    print(n)

for kk, vv in iteritems(n):
    print(kk + ':' + vv)
print(app.url_map._rules[-2].match(b))

print(app.url_map._rules[-2].is_leaf)
print(app.url_map._rules[-2].strict_slashes)
'''
'''
print(app.url_map._rules[38].defaults)
print(len(''))
print(app.url_map)
print(app.url_map._rules)
print(app.url_map._rules_by_endpoint)
'''
'''
print(app.url_map._rules[38]._trace)
print(app.url_map._rules[38]._converters)

print(app.url_map._rules[38].arguments)
print(app.url_map._rules[38].host)
'''
'''
rule = '/auth/<id>'
pos = 0
do_match = _rule_re.match
'''
'''
end = len(rule)
do_match = _rule_re.match
used_names = set()
while pos < end:
'''
'''
m = do_match(rule, pos)

data = m.groupdict()
print(data['static'])
print(data['variable'])
print(data['converter'])
print(data['args'])
'''

'''
print(url_join('', './' + 'post/15'))
'''
'''
print(app.view_functions)
print(app.error_handler_spec)
print(app.url_build_error_handlers)
print(app.before_request_funcs)
print(app.teardown_request_funcs)
print(app.url_value_preprocessors)
print(app.url_default_functions)
print(app.template_context_processors)
print(app.blueprints)
print(app.extensions)
print(app.url_map)
print(app.error_handlers)
print(app.config)
print(app.propagate_exceptions)
print(app.logger)
print(app.jinja_env)
print(app.open_instance_resource())
print(dict(app.jinja_options))
print(app.create_jinja_environment().globals)'''

