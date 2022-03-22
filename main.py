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

  if message.content == "김대표 사기 아니야?":
    await message.channel.send("사기 아니다 :sa~1: :bar:")

  if message.content == "김대표":
    await message.channel.send("안녕하세요. 팡머시티 회원 여러분. 업계 신용 보증수표. 저 김 대표가 팡머시티 회원 여러분들을 위해 화끈한 이벤트를 준비했습니다. 업계 최고 수준의 정확도와 신뢰도를 자랑하는 〈이상투자그룹〉과 협력하여 현재 무료 주식 정보 이벤트를 진행 중입니다. 최대 300% 수익률을 보장하는 확실한 정보를 모아 담은 〈이상투자그룹〉 서비스에 '무료 가입' 해주시면 저 김 대표가 여러분께 즉시 100만 원을 여러분에게 바로 쏴드리겠습니다. 저 믿고 〈이상투자그룹〉 가입하셔서 좋은 정보도 얻으시고 제가 드리는 100만 원도 꼭 받아가시기 바라겠습니다.")

  if message.content == "승트":
    await message.channel.send(":heart:")

  if message.content == "이상투자그룹":
    await message.channel.send("참 좋은 회사입니다. 이상투자그룹 오늘 무료 가입하시면 제가 바로 100만 원 쏩니다")

  if message.content == "인천대":
    await message.channel.send("죄송합니다")

  if message.content == "백대리":
    await message.channel.send("그 분은 백 대표입니다.")

  if message.content == "오대리":
    await message.channel.send("그 분은 오 대표입니다.")

  if message.content == "섹스":
    await message.channel.send("사이버수사대에 신고 완료했습니다.")

  if message.content == "김대표 그는 신인가?":
    await message.channel.send("김대표 그는 X신인가?")

  if message.content == "김광효":
    await message.channel.send("그 분은 저하고 관련 없는 사람입니다")

  if message.content == "야이":
    await message.channel.send("티비")

  if message.content == "야이씨발년아":
    await message.channel.send("야이 씨발년아?")

  if message.content == "십년아":
    await message.channel.send("야이 씨발년아")

  print("김 대표:",client.user.name,"954390234555109427:",client.user.id,"01:",discord.__version__)


client.run(os.environ['token'])