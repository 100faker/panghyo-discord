import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="100만 원 준비"))
  #await client.change_presence(activity=discord.Game(name="게임 하는중"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == "김 대표":
  embed = discord.Embed(title="김 대표가 화끈하게 쏩니다!", description="설명", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
  embed.set_footer(text="안녕하세요. 팡머시티 회원 여러분.")
  embed.set_footer(text="업계 신용 보증수표. 저 김 대표가 팡머시티 회원 여러분들을 위해 화끈한 이벤트를 준비했습니다.")
  embed.set_footer(text="〈이상투자그룹〉 무료 가입 즉시 100만 원을 여러분에게 바로 쏴드리겠습니다.")
  embed.set_footer(text="저 믿고 〈이상투자그룹〉 가입하셔서 좋은 정보도 얻으시고")
  embed.set_footer(text="100만 원 꼭 받아가시기 바라겠습니다.")
  await message.channel.send(embed=embed) 

  if message.content == "김 대표 사기 아니야?":
    await message.channel.send("싫어요 :pinching_hand: :pinching_hand: :pinching_hand:")

  print("김 대표:",client.user.name,"954390234555109427:",client.user.id,"01:",discord.__version__)


client.run(os.environ['token'])