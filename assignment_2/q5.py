import re

def sentence_splitter(filename):
    with open(filename) as file:
        text = file.read()
        text.replace('\n', ' ').replace('\r', '')
        split_lines = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)
        file.close()
        for i in split_lines:
            print i
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    print "in main"    
    sentence_splitter('cool')