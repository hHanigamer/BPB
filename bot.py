import asyncio
import random
from splusthon import SoroushClient
from splusthon.sessions import StringSession

SS = "1AwASaW0tc2VydmVyLnNwbHVzLmlyAbvWa4_wnbryukawvNlz9PAL2VVIz-sr-8DFokM5hPQGaP8sbax5GwB4J3kN2iQj1s8yv6Adc3MDiWRjJCpE_H9veTdaw0z77isOIPi-RF94igMtqThLefQ1SP48xuXQpfIdcM9OU_qrHdMKlXJv6pu28uhKqyw-iflQhf3uEzWdeyrIvvCd59aFlVvOxw0aixq-nwoSuBRo91uew3uTf0iSjMK-mBg2EQZynrz09DBMccHQwQHsy7zgnLBC1Ll3psIPIGMXBkAW6g_eautp9j1xX1f8Mm5L_eQLSTBJaP23653mb_mMwMb_M8m43LApslxWws9Exds2Obm_TdSaLBB_"

async def point_task(client, recipient):
    """Send dot‑messages every 60–70 seconds."""
    ma = alaf = naz = kar = tamiz = shird = shirf = gard = kiss = gaza = bare = 0

    while True:
        await asyncio.sleep(random.uniform(60, 70))
        
        ma += 1
        alaf += 1
        naz += 1
        kar += 1
        tamiz += 1
        shird += 1
        shirf += 1
        gard += 1
        kiss += 1
        gaza += 1
        bare += 1

        if ma >= 5:
            await client.send_message(recipient, 'مع')
            ma = 0
        if alaf >= 7:
            await client.send_message(recipient, 'علف')
            alaf = 0
        if gaza >= 35:
            await client.send_message(recipient, 'غذا بده همه')
            gaza = 0
        if naz >= 9:
            await client.send_message(recipient, 'نازش کن')
            naz = 0
        if tamiz >= 10:
            await client.send_message(recipient, 'تمیزش کن')
            tamiz = 0
        if shird >= 10:
            await client.send_message(recipient, 'شیر بز')
            shird = 0
        if gard >= 10:
            await client.send_message(recipient, 'گردش')
            gard = 0
        if kiss >= 10:
            await client.send_message(recipient, 'بوسش کن')
            kiss = 0
        if bare >= 15:
            await client.send_message(recipient, 'برداشت بره ناقلا')
            bare = 0
        if kar >= 15:
            await client.send_message(recipient, 'جمع آوری کارخانه')
            kar = 0
        if shirf >= 30:
            await client.send_message(recipient, 'فروش شیر')
            shirf = 0

async def main():
    client = SoroushClient(StringSession(SS))
    await client.start()
    recipient = "@bozpoint2"   # ⬅️ Replace with actual recipient
    await point_task(client, recipient)

if __name__ == '__main__':
    asyncio.run(main())
