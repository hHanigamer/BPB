async def trader_task(client, recipient):
    """تریدر خودکار با حفظ وضعیت خرید/فروش"""
    has_tera = False  # وضعیت اولیه: ترا نداریم

    while True:
        try:
            await asyncio.sleep(60)

            sent = await client.send_message(recipient, 'بازار')
            print(f"[{datetime.now()}] درخواست بازار ارسال شد.")
            await asyncio.sleep(3)

            messages = await client.get_messages(
                recipient,
                limit=5,
                offset_id=sent.id
            )

            price = None
            for msg in messages:
                if msg.text and 'TERA' in msg.text and 'قیمت' in msg.text:
                    match = re.search(r'قیمت:\s*([\d.]+)', msg.text)
                    if match:
                        price = float(match.group(1))
                        break

            if price is not None:
                print(f"[{datetime.now()}] قیمت ترا: {price}")

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
            await asyncio.sleep(5)
