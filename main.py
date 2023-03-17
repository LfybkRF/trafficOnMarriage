import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


vk_session = vk_api.VkApi(token = 'vk1.a.kri4ekh31GeJrbmdVODBt0PfOUxyDg_qjVTGTmj0jldIjfiSRYg57DPihhsc2evBq1DfrsZJcTEOyl56lugz7vLjnxqyAmBin71okmlDxOVfNC_Zg8100RWsJKa8zSxif-AkTnBv64KfSRuKMOs9VuvVPojOTLdhTeFURgSfAhN52XkGaUicJrKpATgEDM-JFpo5hIY3WCdUXEJ5i2M4sA')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def message_send(user,msg):
    vk.messages.send(
                        user_id = user,
                        message = msg,
                        random_id = 0,
                    )


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        try:
            if event.to_me:
                spam_message = 'Привет!\n\n Наш функционал:\n\n- Узнать совместимость знаков зодиака\n- Узнать кто ты по демоническому гороскопу\n- Ежедневные актуальные гороскопы\n\nВсё это в нашем приложении\n👉 vk.com/app51560752'
                message_send(event.user_id, spam_message)
                print(event.user_id, event.text)
        except:
            message_send(event.user_id, 'Ой! Кажется, вы сделали что-то непонятное для меня.\n Попробуйте сделать запрос по другому')
                

 