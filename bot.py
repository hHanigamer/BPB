import asyncio
from datetime import datetime
from splusthon import SoroushClient
from splusthon.sessions import StringSession

SS = "1AwASaW0tc2VydmVyLnNwbHVzLmlyAbvWa4_wnbryukawvNlz9PAL2VVIz-sr-8DFokM5hPQGaP8sbax5GwB4J3kN2iQj1s8yv6Adc3MDiWRjJCpE_H9veTdaw0z77isOIPi-RF94igMtqThLefQ1SP48xuXQpfIdcM9OU_qrHdMKlXJv6pu28uhKqyw-iflQhf3uEzWdeyrIvvCd59aFlVvOxw0aixq-nwoSuBRo91uew3uTf0iSjMK-mBg2EQZynrz09DBMccHQwQHsy7zgnLBC1Ll3psIPIGMXBkAW6g_eautp9j1xX1f8Mm5L_eQLSTBJaP23653mb_mMwMb_M8m43LApslxWws9Exds2Obm_TdSaLBB_"

async def main():
    client = SoroushClient(StringSession(SS))
    await client.start()

    recipient = '@BOZPOINT'
    
    ma = 0
    alaf = 0
    naz = 0
    kar = 0
    
    while True:

        await asyncio.sleep(60.5)
        ma += 1 
        alaf += 1
        naz += 1
        kar += 1
            
        if ma >= 5:
            try:
                await client.send_message(recipient, 'مع')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            ma = 0

        if alaf >= 7:
            try:
                await client.send_message(recipient, 'علف')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
                await client.send_message(recipient, 'بهش غذا بده')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            alaf = 0

        if naz >= 9:
            try:
                await client.send_message(recipient, 'نازش کن')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            naz = 0

        if kar >= 15:
            try:
                await client.send_message(recipient, 'جمع آوری کارخانه')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            kar = 0


if __name__ == '__main__':
    asyncio.run(main())
