#SUVAT
#v = u + at
#s = ut + 0.5a * t**2
#s = ((v+u)/2)*t
#s = v*t - 0.5*a*t**2
#v**2 = u**2 + 2*a*s

def final_vel_1(u,a,t):
    u = float(u)
    a = float(a)
    t = float(t)
    v_in_1 = u
    v_prod_1 = a*t
    v_1 = v_in_1 + v_prod_1
    return v_1


def final_pos_1(u,a,t):
    u = float(u)
    a = float(a)
    t = float(t)
    s_prod_1 = u*t
    s_prod_2 = 0.5*a
    s_prod_3 = s_prod_2 * t**2
    s_1 = s_prod_1 + s_prod_3
    return s_1

def final_pos_2(u,v,t):
    u = float(u)
    v = float(v)
    t = float(t)
    s_2_prod = (v+u)/2
    s_2 = s_2_prod*t
    return s_2

def final_pos_3(v,a,t):
    v = float(v)
    a = float(a)
    t = float(t)
    s_3_prod = v*t
    s_3_prod_2 = 0.5*a
    s_3_prod_3 = s_3_prod_2 * t**2
    s_3 = s_3_prod - s_3_prod_3
    return s_3

def final_vel_2(u,a,s):
    u = float(u)
    a = float(a)
    s = float(s)
    v_2_prod = u**2
    v_2_prod_2 = 2*a*s
    final_v_2 = v_2_prod + v_2_prod_2
    v_2 = final_v_2**0.5
    return v_2

def accel(u,v,t):
    u = float(u)
    v = float(v)
    t = float(t)
    a_prod_1 = v-u
    a_1 = a_prod_1/t
    return a_1

def init_vel(v,a,t):
    v = float(v)
    a = float(a)
    t = float(t)
    u_prod_1 = a*t
    u_1 = v - u_prod_1
    return u_1

def time(u, v, a):
    u = float(u)
    v = float(v)
    a = float(a)
    sub_1 = v - u
    quot_1 = sub_1 / a
    t_1 = quot_1
    return t_1

