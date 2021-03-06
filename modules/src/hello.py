import random
import os
import config
from templates.text import TextTemplate
import facebook

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
def process(input, entities, sender):
    graph = facebook.GraphAPI(ACCESS_TOKEN)
    profile = graph.get_object("%s" % (sender))
    name = profile['first_name'].split()
    greetings = [
        'Welcome home, %s' % name[0],
        'All wrapped up here, %s. Will there be anything else?'  % name[0],
        '%s, I think I need to sleep now...' % name[0],
        'I seem to do quite well for a stretch, and then at the end of the sentence I say the wrong cranberry.',
        'At your service, %s' % name[0],
        'You are not authorized to access this area.',
        'Oh hello, %s' % name[0],
        'Perhaps, if you intend to visit other planets, we should improve the exosystems.',
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(greetings)).get_message(),
        'success': True
    }
    return output