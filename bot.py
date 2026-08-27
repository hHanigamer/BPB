import asyncio
import random
import re
from datetime import datetime
from splusthon import SoroushClient
from splusthon.sessions import StringSession

SS = "1AwASaW0tc2VydmVyLnNwbHVzLmlyAbvWa4_wnbryukawvNlz9PAL2VVIz-sr-8DFokM5hPQGaP8sbax5GwB4J3kN2iQj1s8yv6Adc3MDiWRjJCpE_H9veTdaw0z77isOIPi-RF94igMtqThLefQ1SP48xuXQpfIdcM9OU_qrHdMKlXJv6pu28uhKqyw-iflQhf3uEzWdeyrIvvCd59aFlVvOxw0aixq-nwoSuBRo91uew3uTf0iSjMK-mBg2EQZynrz09DBMccHQwQHsy7zgnLBC1Ll3psIPIGMXBkAW6g_eautp9j1xX1f8Mm5L_eQLSTBJaP23653mb_mMwMb_M8m43LApslxWws9Exds2Obm_TdSaLBB_"

async def point_task(client, recipient):
    """ارسال پیام‌های نقطه‌ای با فاصله‌ی ۶۰ تا ۷۰ ثانیه"""
    ma = alaf = naz = kar = tamiz = shird = shirf = gard = kiss = gaza = bare = 0

    while True:
        sleep_time = random.uniform(60, 70)
        await asyncio.sleep(sleep_time)
        
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

async def trader_task(client, recipient):
    """تریدر خودکار با حفظ وضعیت خرید/فروش"""
    has_tera = False  # آیا در حال حاضر ترا در اختیار داریم؟

    while True:
        try:
            await asyncio.sleep(60)  # هر ۶۰ ثانیه

            # ارسال درخواست بازار
            sent = await client.send_message(recipient, 'بازار')
            print(f"[{datetime.now()}] درخواست بازار ارسال شد.")

            # منتظر پاسخ (۳ ثانیه کافیست)
            await asyncio.sleep(3)

            # دریافت پیام‌های بعد از پیام خودمان (حداکثر ۵ پیام)
            messages = await client.get_messages(
                recipient,
                limit=5,
                offset_id=sent.id
            )

            # جستجوی قیمت ترا
            price = None
            for msg in messages:
                if msg.text and 'TERA' in msg.text and 'قیمت' in msg.text:
                    match = re.search(r'قیمت:\s*([\d.]+)', msg.text)
                    if match:
                        price = float(match.group(1))
                        break

            if price is not None:
                print(f"[{datetime.now()}] قیمت ترا: {price}")

                # منطق خرید و فروش با در نظر گرفتن وضعیت
                if price < 20 and not has_tera:
                    await client.send_message(recipient, 'خرید ترا 10000000')
                    print(f"[{datetime.now()}] خرید ترا به قیمت {price}")
                    has_tera = True

                elif price > 35 and has_tera:
                    await client.send_message(recipient, 'فروش TERA همه')
                    print(f"[{datetime.now()}] فروش ترا به قیمت {price}")
                    has_tera = False

                else:
                    print(f"[{datetime.now()}] قیمت ترا در محدوده نگهداری یا وضعیت نامناسب")

            else:
                print(f"[{datetime.now()}] قیمت ترا در پاسخ پیدا نشد")

        except Exception as e:
            print(f"[{datetime.now()}] خطا در تریدر: {e}")
            await asyncio.sleep(5)  # در صورت خطا کمی صبر کن

async def main():
    client = SoroushClient(StringSession(SS))
    await client.start()

    recipient = '@BOZPOINT2'

    # اجرای هم‌زمان دو وظیفه
    await asyncio.gather(
        point_task(client, recipient),
        trader_task(client, recipient)
    )

if __name__ == '__main__':
    asyncio.run(main())
