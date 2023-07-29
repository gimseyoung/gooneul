
with open('./secret', 'r') as f:
    secret = {l.split('=')[0]: l.split('=')[1].strip() for l in f.readlines()}

token = secret['TELEGRAM_TOKEN']

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# hello command에 대해서 실행할 함수
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # reply_text를 하게되면 텍스트 메시지를 전송
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def myname(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'My Name is {update.effective_user.first_name}')

    await update.message.reply_photo(open('./museum_san.png', 'rb'))

fake_db = {
    '국내': ['울릉도', '여수', '남해', '속초', '원주'],
    '해외': ['일본', '미국', '이탈리아', '홍콩', '네덜란드']
}
async def trip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message.text)
    target = update.message.text.split()[-1]
    locations = []
    if target in fake_db:
        locations = fake_db[target]
        await update.message.reply_text(f'추천 여행지 ! {str(locations)}')
    else:
        await update.message.reply_text(f'어느 여행지를 추천해드릴까요? (국내, 해외)')


# bot token을 통해 앱 빌드(생성)
app = ApplicationBuilder().token(token).build()

# 앱이 처리할 명령어들을 정의 
# /hello -> hello 함수를 실행
# /myname -> myname 함수를 실행
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("myname", myname))
app.add_handler(CommandHandler("trip", trip))

if __name__ == '__main__':
    # print(token)

    # 봇을 실행
    app.run_polling()

# 실습
# 핸들러 추가
# 크롤링을 통해 데이터를 정리, 반환해주는 봇 만들기
