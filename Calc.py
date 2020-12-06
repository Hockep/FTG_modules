#.calc <то, что нужно посчитать>(или реплай)
#╰самый простой калькулятор
#			** - возвести в степень
#			/ - деление
#			% - деление по модулю

from .. import loader, utils
class КукуляторMod(loader.Module):
	"""Кукулирует вырожения"""
	strings = {'name': 'Кукулятор'}
	
	async def calccmd(self, message):
		question = utils.get_args_raw(message)
		reply = await message.get_reply_message()
		if not question:
			if not reply:
				await utils.answer(message, "<b>2+2=5</b>")
				return
			else:
				question = reply.raw_text
		try:
			answer = eval(question)
			answer = f"<b>{question}=</b><code>{answer}</code>"
		except Exception as e:
			answer =  f"<b>{question}=</b><code>{e}</code>"
		await utils.answer(message, answer)
