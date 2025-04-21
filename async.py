
import asyncio
# await asyncio.sleep(2)  # 2 second ke liye rukega, lekin CPU free hoga
# await asyncio.gather(func1(), func2(), func3())

# -------------------------------------------------------------------------------------
# Iska use hota hai jab aap ek task ko background mein chalaana chahte ho:
# task = asyncio.create_task(mera_function())

# Phir aap dusra kaam kar sakte ho, aur baad mein task ka result le sakte ho.
# await task

async def mera_function():
    print("Kaam shuru")
    await asyncio.sleep(5)  # 5 second rukega bina block kiye
    print("Kaam khatam")

asyncio.run(mera_function())

async def kaam1():
    print("Kaam 1 shuru")
    await asyncio.sleep(1)
    print("Kaam 1 khatam")

async def kaam2():
    print("Kaam 2 shuru")
    await asyncio.sleep(2)
    print("Kaam 2 khatam")

async def main():
    await asyncio.gather(kaam1(), kaam2())  # Dono kaam parallel chalu honge

asyncio.run(main())

