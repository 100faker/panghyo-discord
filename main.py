import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="여러분께 100만 원 준비"))
  #await client.change_presence(activity=discord.Game(name="게임 하는중"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == "김 대표":
  embed=discord.Embed(title=김 대표가 화끈하게 쏩니다!, description=안녕하세요. 팡머시티 회원 여러분.<br><br>업계 신용 보증수표.<br>저 김 대표가 팡머시티 회원 여러분들을 위해 화끈한 이벤트를 준비했습니다.<br><br>업계 최고 수준의 정확도와 신뢰도를 자랑하는 〈이상투자그룹〉과 협력하여 현재 무료 주식 정보 이벤트를 진행 중입니다.<br><br>최대 300% 수익률을 보장하는 확실한 정보를 모아 담은<br>〈이상투자그룹〉 서비스에 '무료 가입' 해주시면<br><br>저 김 대표가 여러분께 즉시 100만 원을 여러분에게 바로 쏴드리겠습니다.<br><br>저 믿고 〈이상투자그룹〉 가입하셔서 좋은 정보도 얻으시고<br>제가 드리는 100만 원도 꼭 받아가시기 바라겠습니다., color=0xff0000)
  embed.set_image(url="https://cdn.discordapp.com/attachments/594909012181516301/954336734055915550/ef6ec30426b35c18.jpg")
  await ctx.send(embed=embed)

  if message.content == "김 대표 사기 아니야?":
    await message.channel.send("사기 아니다 :pinching_hand: :pinching_hand: :pinching_hand:")

  print("김 대표:",client.user.name,"954390234555109427:",client.user.id,"01:",discord.__version__)


client.run(os.environ['token'])