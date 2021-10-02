import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

json_object = json.loads('{"foo":"bar"}')
json_str = json.dumps(json_object, indent=4, sort_keys=True)
print(highlight(json_str, JsonLexer(), TerminalFormatter()))