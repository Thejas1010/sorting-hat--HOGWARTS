
print("Welcome to Hogwarts!", end ="  ")
print("the sorting hat will ask some questions to find a suitable house for u")

a = int(0)
b = int(0)
c = int(0)
d = int(0)

print("Q1) do u like dawn or dusk\n     1)dawn\n     2)dusk")
q1 = int(input("enter integer 1 or 2:"))

if q1 ==1:
  a = a+1
  b = b+1
elif q1==2:
  c = c+1
  d = d+1


print("Q2) when i am dead, i want people to remember me as:\n    1)the good\n    2)the great\n    3)the wise\n    4)the bold")
q2 = int(input("enter input 1 0r 2 0r 3 0r 4:"))

if q2 ==1:
  c=c+2
elif q2==2:
  d=d+2
elif q2==3:
  b=b+2
elif q2==4:
  a=a+2


print("Q3) which kind of instrument most pleases your ear?\n    1)the violin\n    2)the trumpet\n    3) the paino\n    4)the drum")
q3 = int(input("enter the input 1 0r 2 0r 3 0r 4:"))

if q3==1:
  c=c+4
elif q3==2:
  d =d+4
elif q3==3:
  b=b+4
elif q3==4:
  a=a+4


z = "your house is:"


if a >b and a> c and a>d:
  print(z,"gryffindor")
elif b>a and b> c and b> d:
  print(z,"ravenclaw")
elif c>a and c>b and c> d:
  print(z,"hufflepuff")
elif d>a and d>b and d>c:
  print(z,"slytherin")



