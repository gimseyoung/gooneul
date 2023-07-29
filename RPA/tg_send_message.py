# 특정 채팅방에 메시지 보내기 (자동화 프로그램 개발 시)
# chat_id는 update.message.chat_id로 확인
import requests

def send_to_telegram(message):

    token = 'YOUR-TOKEN-HERE'
    chat_id = 'CHAT-ROOM-ID'
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    try:
        res = requests.post(url, 
                            json={'chat_id': chat_id, 'text':message})
        print(res.text)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    send_to_telegram('hello from python')