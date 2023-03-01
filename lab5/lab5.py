import re

# #1
# def a_more_b(string):
#     match = re.fullmatch(r"ab*", string)
#     return (match is not None)

# print(a_more_b(input("напиши один a и 1 или более b: ")))


# #2
# def a_more_b(string):
#     match = re.fullmatch(r"ab{2,3}", string)
#     return (match is not None)

# print(a_more_b(input("напиши один a и 2 или 3 b: ")))


# #3
# def a_more_b(string):
#     match = re.findall(r"[a-z]_", string)
#     return (match)

# print(a_more_b(input("напиши один a и 2 или 3 b: ")))


# # 4
# def a_more_b(string):
#     match = re.findall(r"[A-Z][a-z]*", string)
#     return (match)
# #AgaiEtoRabotaTochnoNaPyatBallov
# print(a_more_b(input("напиши один a и 2 или 3 b: ")))


# #5
# def a_more_b(string):
#     match = re.fullmatch(r'a.*b',string)
#     return (match is not None)

# print(a_more_b(input("напиши один a и 2 или 3 b: ")))


# #6
# def a_more_b(string):

#     match = re.sub(r'[ |,|.]',":",string)
#     return (match)

# print(a_more_b(input("напиши один a и 2 или 3 b: ")))


#7
# def a_more_b(string):
#     x=[]
#     match = (re.split(' ',string))
#     # (match for i in match: match[i].capitalize())
#     # match.capitalize()
#     for i in match:
#         x.append(i.capitalize())
#         # match[1].upper()
#     return (' '.join(x))

# print(a_more_b(input("напиши один a и 2 или 3 b: ")))


#8
# def a_more_b(string):

#     match = re.findall(r"[a-zA-Z][^A-Z]*",string)
#     return (match)

# print(a_more_b(input("напиши один a и 2 или 3 b: ")))


# #9
# def a_more_b(string):

#     match = re.sub(r'[A-Z]'," ",string)
#     return (match)

# #AagaiNneNnuEeTtoZzhelezoBbetonnoRrabotaNna5Bballov
# print('\n',a_more_b(input("напиши один a и 2 или 3 b: ")),'\n')


# #9
# def a_more_b(string):

#     match = re.findall(r'[A-Z][a-z]*|[A-Z]',string)
#     return ' '.join(match)

# print('\n',a_more_b(input("напиши один a и 2 или 3 b: ")),'\n')

#10

# def a_more_b(string):
#     x=[]
#     match = (re.split(' ',string))
   
#     for i in match:
#         x.append(i.lower())
#         # match[1].upper()
#     return (' '.join(x))

# print(a_more_b(input("напиши один a и 2 или 3 b: ")))

