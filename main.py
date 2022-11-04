#  SUVAT
#  v = u + at
#  s = ut + 0.5a * t**2
#  v**2 = u**2 + 2*a*s
#  s = ((v+u)/2)*t
#  s = v*t - 0.5*a*t**2
import sys
from suvat import *

s = input("Give the value for position, enter UNK if the quantity is unknown: ")
u = input("Give the value for initial velocity, enter UNK if the quantity is unknown: ")
v = input("Give the value for final velocity, enter UNK if the quantity is unknown: ")
a = input("Give the value for acceleration, enter UNK if the quantity is unknown: ")
t = input("Give the value for time, enter UNK if the quantity is unknown: ")

quantities = [s, u, v, a, t]
i = 0
while i <= 4:
    if quantities[i].lower() == "unk":
        quantities[i] = "UNK"

    elif quantities[i].isnumeric():
        quantities[i] = float(quantities[i])
    else:
        quantities[i] = "Bad Input"
        print("Bad input!")
    i += 1
if "Bad Input" in quantities:
    print("Sorry, one of your inputs is invalid, please make sure all values are a number, or UNK.")
    sys.exit()
if u != "UNK" and v != "UNK" and a != "UNK":
    t = time(u,v,a)
    final_pos_2(u,v,t)
    s_out0 = final_pos_2(u,v,t)
    s = s_out0

if u != "UNK" and a != "UNK" and t != "UNK":
    final_pos_1(u, a, t)
    s_out1 = final_pos_1(u, a, t)
    s = s_out1
    final_vel_1(u, a, t)
    v_out1 = final_vel_1(u, a, t)
    v = v_out1
    print("First s is: " + str(s))
    print("First v is: " + str(v))

elif u != "UNK" and v != "UNK" and t != "UNK":
    final_pos_2(u, v, t)
    s_out2 = final_pos_2(u, v, t)
    s = s_out2
    print("Second s is: " + str(s))
    a = accel(u,v,t)


elif v != "UNK" and a != "UNK" and t != "UNK":
    final_pos_3(v, a, t)
    s_out3 = final_pos_3(v, a, t)
    s = s_out3
    print("Third s is: " + str(s))
    u = init_vel(v, a ,t)

if u != "UNK" and a != "UNK" and s != "UNK":
    final_vel_2(u, a, s)
    v_out2 = final_vel_2(u, a, s)
    v = v_out2
    print("Second v is: " + str(v))
    t = time(u, v, a)
v_out = v
s_out = s

print("The final values are: " + str(s_out) + "," + str(u) + "," + str(v_out) + "," + str(a) + "," + str(t) + ".")

