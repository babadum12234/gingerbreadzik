import random

def mountains():
    s=random

def forest():
    s=2

input("Welcome to RPG!")
print("You see mountains in the left and forest in the right! Choose carefully!(L or R)")
print("                                   /\\                            ,,,.   ,@@@@@@/@@,  .oo8888o.")
print("                              /\\  //\\\\                        ,&%%&%&&%,@@@@@/@@@@@@,8888\\88/8o")
print("                       /\\    //\\\\///\\\\\        /\\            ,%&\\%&&%&&%,@@@\\@@@/@@@88\\88888/88'")
print("                      //\\\\  ///\////\\\\\\\\  /\  //\\\\           %&&%&%&/%&&%@@\\@@/ /@@@88888\\88888'")
print("         /\\          /  ^ \\/^ ^/^  ^  ^ \\/^ \\/  ^ \\           %&&%/ %&%%&&@@\\ V /@@' `88\\8 `/88'")
print("        / ^\\    /\\  / ^   /  ^/ ^ ^ ^   ^\\ ^/  ^^  \\           `&%\\ ` /%&'    |.|        \ '|8'")
print("       /^   \\  / ^\\/ ^ ^   ^ / ^  ^    ^  \\/ ^   ^  \\              |o|        | |         | |")
print("      /  ^ ^ \\/^  ^\ ^ ^ ^   ^  ^   ^         ^   ^  \\             |.|        | |         | |")
chose=input()
if chose == "L":
    mountains()
elif chose == "R":
    forest()
