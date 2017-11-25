from fetch_data import train
from markov_python.cc_markov import MarkovChain
# The above comes from https://github.com/ReagentX/markov_python
import re


# Get the text from a webpage
data = train('http://www.gutenberg.org/files/135/135-h/135-h.htm')

# Clean the page to remove any pesky bits
data = re.sub('<.*?>', '', data)
data = re.sub('&rsquo', '\'', data)
data = re.sub('&rdquo|&ldquo', '\"', data)

# Make a markov chain object
mc = MarkovChain(4)

# Add the data
mc.add_string(data)
text = mc.generate_text(30)
result = ''
for word in text:
    result += word + ' '

print(result)