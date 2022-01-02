### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# it should be == rather than =. = is used to assign value to a variable whereas == checks for equality, semicolon missing after else
  def check_for_ace(self, card):
    if card.value = 1: 
      return True
    else
      return False
   
# Comma missing between card 1 and card 2; 
# In return statement it should be card1. Card is undefined. 
# Function is declared by def rather than dif. 
# Indentation is incorrect, if and else statements should be indented, as well as  return statements accordingly

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# total is not initialized as a variable
# the whole function should be indented
# return statement should be indented on the lever with for statement
# only strings can be concatenated, the total in return statement has to be converted into string
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
