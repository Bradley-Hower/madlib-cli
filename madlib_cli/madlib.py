import re

print(
  """
  
    ............                                                                                    
    ~..........^:                                                                  .............    
    ~          ::       ~.:::~                  :............:.                    ~...........:^   
    ~     .:...~^......:!..  ~.                .^ ...........:^            .::::.  ~           .^   
    ~     ^: . ^^ ......~^~..~.  .:............^~.:.         :^            ^:  :^  ~           .^   
    ^:::::~^:::^.       .:~...   :^ .......... :~ .~         .^       ^::::~~^.:^  ~...........:^   
          ^:             .^      ::            .~.:!.........^^       ~... .:!^..  .............    
          ^.             .^      :^...............:~ .........        :::::..:                      
          ^:.............:^      .:.................                                                
           ...............                                                                          
                                                                                        ...         
          .^.                ~77:     .:^^^^^:.          ::.     :7?~    .:^~~^.    ~JGB&&&#7       
         J&@#?    .JG5^    .P@@@&Y:  !&@@@@@@@&#GY7^    Y@@G     Y@@&:~YG#&@@@@&P: 7@@@&5Y5Y:       
        ?@@@@@J  :B@@@&^   Y@@#B@@&? :??P@@@YJ5G#@@@BJ: 5@@@^    7@@@7B@@@&7~?&@@Y :Y#@@#P7:        
        #@@G#@@5!#@@&@@B. ~@@@?~G@@@G!~ .&@@J    :!P@@&7!@@@!    ^@@@J J@@@JJG@@@7  75PP#@@@G7      
       :@@@7.G@@@@&?^&@@GG&@@@@@@@@@@@@? P@@G       G@@&~@@@?     #@@5 :&@@@&#B#@@BP@@@7 ~Y&@@G.    
       ^@@@?  !557:  ?@@@@@@&?77!!~J&@@B~G@@@5J??JP#@@&?.#@@G7?JY7#@@P  G@@#!^:^Y@@@B@@@GJ7P@@@^    
        P&#!          ?5?P&&7       :P@@P75GB&&@@&#GY!. .#@@@@@@&PY#B7  J@@@@@@&@@&Y ~YB&@@@#P~     
         .                ..          ^:     ..:..       ^~^^::..       :PP?!7??7~:     .:::.       
                                               ..                                                   
                                             ^:..:^.                  ......                        
                                            ~.     ~                .^:.. ..::  .....               
          ..........          ::::::       :^      :^              .^        ^!:.....:::            
       :::..........:::..:::.^~    :^      .^    .:!^:::::::::     ^.       ^:~.       .^           
      ~.             .~~.    :!^. .^:     .:~~::!^^^         .~.:::~~.::::. ~ ~         ^:          
      ::..          .!:.       ^!::.     ^^. .::~!7:      ...:~^.   ^:    ^:^!:   .....:^           
        ..::::::::::.^:.      .^.         .:::::::..:::::::.. .^..   .::^^~^..:::~~^^^~^~           
                      .:::::::.                                 ..:::::::.       ..:::...           
                                                                                                     
  """
)

print(
  """
  Good day. Let's play a game of Madlibs!

  The game of Madlibs is a simple game but can be oh so fun.
  When prompted, continue to provide the given word type and your outlandish madlib will be served up to
  you.

  If at any time you wish to quit, type 'ctrl + c'. 
  """
  )


def read_template(sourcetext):
  try:
    with open(sourcetext, 'r') as file:
      content = file.read()
      stripped_content = content.replace('\n', '')
      return stripped_content
  except FileNotFoundError:
    raise FileNotFoundError

def parse_template(puretext):
  thelist = []
  for i in re.findall("{(.*?)}", puretext):
    thelist.append(i)
  replaced = re.sub("{(.*?)}", '{}', puretext)

  thetuple = tuple(thelist)
  return(replaced, thetuple)

def merge(templatetext, words):
  mergedtext = templatetext.format(*words)
  return mergedtext

stripped_text = read_template("assets/dark_and_stormy_night_template.txt")

parsed_template_text = parse_template(stripped_text)

def userwords_input():
  userinput = []
  for i in parsed_template_text[1]:
    aword = input("Please provide the following: " + i + " > ")
    userinput.append(aword)
  userinput_tuple = tuple(userinput)
  return userinput_tuple

merged_text = merge(parsed_template_text[0], userwords_input())

def write_output(write_text):
  with open('output/madlibs_output.txt', 'w') as file:
    file.write(write_text)


write_output(merged_text)

print(
  """
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ~~~~~~~~~~~~MADLIB PROSE~~~~~~~~~~~~~
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  """ + 
  merged_text + 
  """
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  """
  )