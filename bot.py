import asyncio
from datetime import datetime
from splusthon import SoroushClient
from splusthon.sessions import StringSession

SS = "1AwASaW0tc2VydmVyLnNwbHVzLmlyAbvWa4_wnbryukawvNlz9PAL2VVIz-sr-8DFokM5hPQGaP8sbax5GwB4J3kN2iQj1s8yv6Adc3MDiWRjJCpE_H9veTdaw0z77isOIPi-RF94igMtqThLefQ1SP48xuXQpfIdcM9OU_qrHdMKlXJv6pu28uhKqyw-iflQhf3uEzWdeyrIvvCd59aFlVvOxw0aixq-nwoSuBRo91uew3uTf0iSjMK-mBg2EQZynrz09DBMccHQwQHsy7zgnLBC1Ll3psIPIGMXBkAW6g_eautp9j1xX1f8Mm5L_eQLSTBJaP23653mb_mMwMb_M8m43LApslxWws9Exds2Obm_TdSaLBB_"

async def main():
    client = SoroushClient(StringSession(SS))
    await client.start()

    recipient = '@BOZPOINT2'
    
    ma = 0
    alaf = 0
    naz = 0
    kar = 0
    tamiz = 0
    shird = 0
    shirf = 0
    gard = 0
    kiss = 0
    gaza = 0
    alafyab = 0
    bare = 0


    
    while True:

        await asyncio.sleep(60.5)
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
        alafyab += 1
        bare += 1
            
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
            alaf = 0

        if alafyab >= 6:
            try:
                await client.send_message(recipient, 'علف یاب بخر')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            alafyab = 0
            
        if gaza >= 7:
            try:
                await client.send_message(recipient, 'غذا بده همه')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            gaza = 0
        
        if naz >= 9:
            try:
                await client.send_message(recipient, 'نازش کن')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            naz = 0

        if tamiz >= 10:
            try:
                await client.send_message(recipient, 'تمیزش کن')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            tamiz = 0
        
        if shird >= 10:
            try:
                await client.send_message(recipient, 'شیر بز')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            shird = 0
                
        if gard >= 10:
            try:
                await client.send_message(recipient, 'گردش')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            gard = 0
                        
        if kiss >= 10:
            try:
                await client.send_message(recipient, 'بوسش کن')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            kiss = 0
                        
        if bare >= 15:
            try:
                await client.send_message(recipient, 'برداشت بره ناقلا')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            bare = 0
        
        if kar >= 15:
            try:
                await client.send_message(recipient, 'جمع آوری کارخانه')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            kar = 0
                
        if shirf >= 30:
            try:
                await client.send_message(recipient, 'فروش شیر')
                print(f"[{datetime.now()}] پیام ارسال شد.")
            except Exception as e:
                print(f"خطا: {e}")
            shirf = 0
        

if __name__ == '__main__':
    asyncio.run(main())
