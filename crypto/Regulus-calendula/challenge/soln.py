import sympy
import sys
from pwn import *
import logging
from itertools import product
import random
sys.setrecursionlimit(10000)
pr = process(['python3', 'regulus-calendula.py'])
pr.recvuntil(": ")
pr.sendline("2")
pr.recvuntil(" = ")
n = int(pr.recvline().strip().decode('utf-8'))
p1 = []
for i in range(8):
    pr.recvuntil(": ")
    pr.sendline("4")
    pr.recvuntil(": ")
    pr.sendline(hex(i)[2:]*1024)
    p1.append(pr.recvline().strip().decode("utf-8"))
p2 = [" "]*1024
for i in range(8):
    for s in range(1024):
        if p1[i][s]=="1":
            p2[s]=hex(i)[2:]
q1 = []
for i in range(8):
    pr.recvuntil(": ")
    pr.sendline("4")
    pr.recvuntil(": ")
    pr.sendline(hex(i)[2:]*1024)
    q1.append(pr.recvline().strip().decode("utf-8"))
q2 = [" "]*1024
for i in range(8):
    for s in range(1024):
        if q1[i][s]=="1":
            q2[s]=hex(i)[2:]
def _int_to_bits(i, count): #script stolen from https://github.com/jvdsn/crypto-attacks/blob/master/factorization/branch_and_prune.py
    bits = []
    for _ in range(count):
        bits.append(i & 1)
        i >>= 1
    return bits
def _bits_to_int(bits, count):
    i = 0
    for k in range(count):
        i |= (bits[k] & 1) << k
    return i
def _tau(x):
    i = 0
    while x % 2 == 0:
        x //= 2
        i += 1
    return i
def _find_k(n, e, d_bits):
    best_match_count = 0
    best_k = None
    best_d__bits = None
    for k in range(1, e):
        d_ = (k * (n + 1) + 1) // e
        d__bits = _int_to_bits(d_, len(d_bits))
        match_count = 0
        for i in range(len(d_bits) // 2 - 2):
            if d_bits[-(i + 1)] == d__bits[-(i + 1)]:
                match_count += 1
        if match_count > best_match_count:
            best_match_count = match_count
            best_k = k
            best_d__bits = d__bits
    return best_k, best_d__bits
def _correct_msb(d_bits, d__bits):
    for i in range(len(d_bits) // 2 - 2):
        d_bits[-(i + 1)] = d__bits[-(i + 1)]
def _correct_lsb(e, d_bits, exp):
    inv = pow(e, -1, 2 ** exp)
    for i in range(exp):
        d_bits[i] = (inv >> i) & 1
def _branch_and_prune_pq(n, p, q, i):
    p_ = _bits_to_int(p, i)
    q_ = _bits_to_int(q, i)
    if i == len(p) or i == len(q):
        yield p_, q_
    else:
        c1 = ((n - p_ * q_) >> i) & 1
        p_prev = p[i]
        q_prev = q[i]
        p_possible = [0, 1] if p_prev is None else [p_prev]
        q_possible = [0, 1] if q_prev is None else [q_prev]
        for p_bit, q_bit in product(p_possible, q_possible):
            if (p_bit+q_bit)%2 == c1:
                p[i] = p_bit
                q[i] = q_bit
                yield from _branch_and_prune_pq(n, p, q, i + 1)

        p[i] = p_prev
        q[i] = q_prev

def factorize_pq(n, p_bits, q_bits):
    assert len(p_bits) == len(q_bits), "p and q bits should be of equal length."
    p_bits = p_bits[::-1]
    q_bits = q_bits[::-1]
    p_bits[0] = 1
    q_bits[0] = 1
    for p, q in _branch_and_prune_pq(n, p_bits, q_bits, 1):
        if p * q == n:
            return [int(p), int(q)]
p3 = []
for i in p2:
    if i==' ':
        p3.extend([1,None,None,None])
    else:
        p3.extend([int(j) for j in list(bin(int(i))[2:].zfill(4))])
q3 = []
for i in q2:
    if i==' ':
        q3.extend([1,None,None,None])
    else:
        q3.extend([int(j) for j in list(bin(int(i))[2:].zfill(4))])
ret = factorize_pq(n,p3,q3)
p = ret[0]
q = ret[1]
d = sympy.mod_inverse(65537,(p-1)*(q-1))
pr.recvuntil(": ")
pr.sendline("3")
pr.recvuntil(": ")
pr.sendline(str(d))
pr.recvline()
print(pr.recvuntil("}").strip().decode("utf-8")[2:])